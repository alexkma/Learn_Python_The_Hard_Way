i = 0
numbers = []
	
while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
	
print "The numbers: "

for num in numbers:
	print num
	
def while_func(increment, size):
	i = 0
	nums = []
	while i < size:
		nums.append(i)
		i += increment
		
	return nums
	
print while_func(2, 10)

def for_func(increment, size):
	nums = []
	for i in range(0, size, increment):
		nums.append(i)
		
	return nums
	
print for_func(2, 10)