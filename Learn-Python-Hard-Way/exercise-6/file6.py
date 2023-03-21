# examples of using string formatting characters
x = "There are %d types of people." % 10 # the character %d is used for numbers
binary = "binary"
do_not = "don't"
# when using multiple formatting chars in a string, you need to put them in () separated
# by commas
y = "Those who know %s and those who %s." % (binary, do_not) # <- like there

print x
print y

print "I said: %r." % x
# %r is used in strings to format with variables, like %s. %s puts
# the variable through str() which converts it to a string. %r puts it through
# repr() which also converts to string, but represents a valid python syntax
# for the object being passed.

# use %r for debugging because it displays the raw data of the variable
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
