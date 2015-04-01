# Here's some new strange stuff, remember type it exactly.
#string
days = "Mon Tue Wed Thu Fri Sat Sun"
#string that contains new line symbol for each month
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months
#\n does not work with %r
print "\n%r" % months
#no longer need commas
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
# + only works when the two strings are on one line. like this:
print "There's something going on here." + "With the three double-quotes."
# , works with two prints.
print "There's something going on here.", 
print "With the three double-quotes."