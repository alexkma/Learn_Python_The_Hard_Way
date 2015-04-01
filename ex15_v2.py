# takes two arguments; script name and file name to open
filename = raw_input("Please enter file name you'd like to open :): ")
# open file
txt = open(filename)
# print out file name
print "Here's your file %r:" % filename
# read contents of file assigned to variable txt
print txt.read()