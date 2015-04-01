from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
# f.seek(offset, from_what)
# from_what: 0 beginning of file; 1 current file position; 2 end of file
# from_what can be omitted and defaults to 0
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline(),

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# every time readLine() is called, the file object's current position is moved to the next line
# This is line 1\n
# This is line 2\n
# This is line 3\n
# 1 to indicate line 1
# current_line = 1
current_line = 1
print_a_line(current_line, current_file)

# increment current_line to indicate line 2
# current_line = 1 ---> current_line = current_line + 1 ---> 2
# current_line = 2
current_line += 1
print_a_line(current_line, current_file)

# increment current_line to indicate line 3
# current_line = 2 ---> current_line = current_line + 1 ---> 3
# current_line = 3
current_line += 1
print_a_line(current_line, current_file)