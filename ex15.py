# Use only raw_input and try the script that way. Why is one way of getting the filename would be better than another?
# It is better to use argv when the inputs will not be affected by any conditional statements such as username, age.
# In other words, variables that don't change.
 
# import argv module
from sys import argv
# takes two arguments; script name and file name to open
script, filename = argv
# open file
txt = open(filename)
# print out file name
print "Here's your file %r:" % filename
# read contents of file assigned to variable txt
print txt.read()

# asks for file name again
print "Type the filename again:"
file_again = raw_input("> ")
# open file
txt_again = open(file_again)
# read file
print txt_again.read()

txt.close()
txt_again.close()