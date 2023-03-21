# This is an import. This adds modules to your script from the Python
# feature set. The 'argv' is the argument variable and is used to
# hold the arguments you pass to your Python script when run.
from sys import argv

# This 'unpacks' argv so that it gets assigned to 4 variables you
# can work with.
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
