from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# I want to show contents of file before user decides if he wants to delete file
print "Opening the file for reading..."
target = open(filename, 'r')
print "Do you really want to delete your file?"
print target.read()
raw_input("?")
target.close()

print "Opening the file for writing..."
target = open(filename, 'w')
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

contents = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(contents)
# close for writing
target.close()
# open same file for reading
print "Opening the file for reading..."
target = open(filename, 'r')
# read contents of file
print target.read()
target.close()
print "And finally, we close it."