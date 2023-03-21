from sys import argv

script, filename = argv

print "This is another example of opening a file, emptying it's contents"
print "and writing new lines."

target = open(filename, 'r+')
print "This is what the file says before truncating"
print "%s" % target.read()
target.truncate()

print "Enter a line"
line1 = raw_input()

target.write(line1)
target.close()

new_content = open(filename)
print "This is what the updated file says: %s" % new_content.read()
new_content.close()
