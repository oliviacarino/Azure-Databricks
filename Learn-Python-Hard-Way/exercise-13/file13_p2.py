# import sys module
from sys import argv

# unpack
script, one, two, three = argv

quote = raw_input("Enter a random quote")

print "This script is called:", script
print "One:", one
print "Two:", two
print "Three:", three
print "You said: %s" % quote
