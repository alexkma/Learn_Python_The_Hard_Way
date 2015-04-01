from random import randint

code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
print "code: ", code
guess = raw_input("[keypad]> ")
guesses = 0

while guess != code and guesses < 10:
	print "guesses: ", guesses
	print "BZZZZEDDD!"
	guesses += 1
	guess = raw_input("[keypad]> ")

if guess == code:
    print "The container clicks open and the seal breaks, letting gas out."
    print "You grab the neutron bomb and run as fast as you can to the"
    print "bridge where you must place it in the right spot."
else:
    print "The lock buzzes one last time and then you hear a sickening"
    print "melting sound as the mechanism is fused together."
    print "You decide to sit there, and finally the Gothons blow up the"
    print "ship from their ship and you die."
