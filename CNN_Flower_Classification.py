# Databricks notebook source
# https://www.tensorflow.org/tutorials/images/classification
# We use a CNN to classify images of flowers. No, they're not from the famous Iris dataset!
%pip install tensorflow

# COMMAND ----------

import pathlib
import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

# COMMAND ----------

# Download the Data
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file('flower_photos', origin=dataset_url, untar=True)
data_dir = pathlib.Path(data_dir)

# COMMAND ----------

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

# COMMAND ----------

# Don't forget to stop and smell the roses :)
roses = list(data_dir.glob('roses/*'))
PIL.Image.open(str(roses[0]))

# COMMAND ----------

PIL.Image.open(str(roses[1]))

# COMMAND ----------

# and tulips :D
tulips = list(data_dir.glob('tulips/*'))
PIL.Image.open(str(tulips[0]))

# COMMAND ----------

PIL.Image.open(str(tulips[1]))

# COMMAND ----------

# Load Data (Keras Utility)
batch_size = 32
img_height = 180
img_width = 180

# Split Data - 80% Train, 20% Validation
train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)
val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# COMMAND ----------

class_names = train_ds.class_names
print(class_names)

# COMMAND ----------

# Visualizing the Data
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")

# COMMAND ----------

# Optional - manually iterate over dataset and retrieve batches of images
# Output is a tensor
for image_batch, labels_batch in train_ds:
  print(image_batch.shape)    # (length, width, channel)
  print(labels_batch.shape    # (labels,)
  break

# COMMAND ----------

# Configure Dataset for Performance
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# COMMAND ----------

# Normalize the Data
# CNN like small ranges, here we are normalizing 0-255 to 0-1
normalization_layer = layers.Rescaling(1./255)

# now apply normalization_layer to dataset
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
# Notice the pixel values are now in `[0,1]`.
print(np.min(first_image), np.max(first_image))

# COMMAND ----------

# Build the Model
# Using a Sequential Keras model that consists of 3 Conv layers and 3 Max Pooling layers, all followed by 1 fully connected layer
num_classes = len(class_names)

model = Sequential([
  layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])

# COMMAND ----------

# Compile the Model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# COMMAND ----------

model.summary()

# COMMAND ----------

# Train the Model
epochs=10
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)

# COMMAND ----------

# Visualize Training Results --- Overfitting will occur (for now, but we will try to fix this in the following cells)
# Overfitting might have occurred due to using small number of training examples
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

# COMMAND ----------

# Fix the overfitting via 1) data augmentation and 2) adding dropout to our model
################################################################################
# 1) Data Augmentation: Generating additional training data from your existing examples by augmenting 
# them using random transformations that yield believable-looking images.
data_augmentation = keras.Sequential(
  [
    layers.RandomFlip("horizontal",
                      input_shape=(img_height,
                                  img_width,
                                  3)),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
  ]
)

# COMMAND ----------

# visualize some of the augmented examples we just made
plt.figure(figsize=(10, 10))
for images, _ in train_ds.take(1):
  for i in range(9):
    augmented_images = data_augmentation(images)
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(augmented_images[0].numpy().astype("uint8"))
    plt.axis("off")

# COMMAND ----------

# 2) Add dropout regularization to the model
################################
# Dropout: randomly drops out (by setting the activation to zero) a number of output units from the layer during the training process.
# 0.2 means 20% of output units will randomly be dropped out. This helps neurons from over-relying on one image which helps prevent overfitting.
model = Sequential([
  data_augmentation,
  layers.Rescaling(1./255),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Dropout(0.2),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes, name="outputs")
])

# COMMAND ----------

# Compile Model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# COMMAND ----------

model.summary()

# COMMAND ----------

# Train Model
epochs = 15
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)

# COMMAND ----------

# Visualize Training Results (after adding data augmentation and dropout to model)
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

# COMMAND ----------

# Test Model (predict on new data)
sunflower_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg"
sunflower_path = tf.keras.utils.get_file('Red_sunflower', origin=sunflower_url)

img = tf.keras.utils.load_img(
    sunflower_path, target_size=(img_height, img_width)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)

# COMMAND ----------

# Optional -- TensorFlow Lite

# Convert the model to TensorFlow Lite model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)


# COMMAND ----------

# Run the TensorFlow Lite Model
TF_MODEL_FILE_PATH = 'model.tflite' # The default path to the saved TensorFlow Lite model

interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)

# COMMAND ----------

# Print the signatures from the converted model to obtain the names of the inputs (and outputs):
interpreter.get_signature_list()

# COMMAND ----------

# Test the TensorFlow Lite Model
classify_lite = interpreter.get_signature_runner('serving_default')
classify_lite

# COMMAND ----------

predictions_lite = classify_lite(sequential_1_input=img_array)['outputs']
score_lite = tf.nn.softmax(predictions_lite)

# COMMAND ----------

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score_lite)], 100 * np.max(score_lite))
)

# COMMAND ----------

print(np.max(np.abs(predictions - predictions_lite)))

# COMMAND ----------


