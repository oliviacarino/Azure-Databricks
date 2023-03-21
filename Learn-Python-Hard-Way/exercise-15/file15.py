# import sys module
from sys import argv

# unpack
script, filename = argv

# opens a file
txt = open(filename)

# outputs the specified file from argv to stdout
print "Here's your file %r:" % filename
print txt.read()

# collects new filename from stdin
print "Type the filename again:"
file_again = raw_input("> ")

# opens file
txt_again = open(file_again)

# outputs the specfied file from stdin to stdout
print txt_again.read()

txt.close()
txt_again.close()

# collect new line of content from stdin
new_content = raw_input("Type a sentence: ")

txt = open(filename)
txt.write(new_content)
print txt.read()
