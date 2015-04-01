#prints number of people
x = "There are %d types of people." % 10
#string
binary = "binary"
#string
do_not = "don't"
#string inside a string (#1)
y = "Those who know %s and those who %s." % (binary, do_not)
#print string x
print x
#print string y
print y
#string inside a string (#2)
print "I said: %r." % x
#string inside a string (#3)
print "I also said: '%s'." % y
#boolean variable
hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"
#string inside a string (#4)
print joke_evaluation % hilarious
#first string
w = "This is the left side of..."
#second string
e = "a string with a right side."
#concat string w and string e.
print w + e