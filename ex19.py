def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# pass numbers as arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#pass variables as arguments
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# pass math operations as arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# pass variables combined with numbers as arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def add(value1, value2):
	print "sum: %d" % (value1 + value2)

# way 1	
add(4, 5)
# way 2
value1 = 77
value2 = 5
add(value1, value2)
# way 3
add(value1 + 4, value2)
# way 4
add(value1, value2 + 5)
# way 5
add(value1 + 10, value2 + 4)
# way 6
add(value1 - 10, value2 + 4)
# way 7
input1 = int(raw_input("enter value1: "))
add(input1, 4)
# way 8
input2 = int(raw_input("enter value2: "))
add(input1, input2)
# way 9
add(input1, value1)
# way 10
add(input1 + 3, value2)
