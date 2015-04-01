from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
	# the following is only executed if user types 0 or 1.
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	# always true and will forever run until user selects an option that either calls dead() or gold_room()
	# infinite loop
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		# true AND bear_moved must be false. true AND not(false) = true
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		# true AND bear_moved must be true. bear_moved can only be true if the user has already taunted the bear once before.
		# basically if you taunt the bear TWICE, you're dead.
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		# true AND bear_moved must be true. bear_moved can only be true if the user has already taunted the bear once before.
		# leads you to the gold room.
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	# recursion 
	else:
		cthulhu_room()
		
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
		
start()