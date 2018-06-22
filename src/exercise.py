# What is 7 power 4
print(7**4)

# Print a list
aString = 'Hi there Sam!'
aList = list(aString.split())
print(aList)

# Return domain address
email = 'samuel.dufresne@mindgeek.com'
after_at = False
domain = ''
print(len(email))
for index in range(0, len(email)):
	if after_at:
		domain += email[index]
	if email[index] == '@':
		after_at = True
print(domain)

# Format print the diameter of the Earth
planet = "Earth"
diameter = 12742
print('The diameter of the {planet} is {distance} km'.format(planet=planet, distance=diameter))

# Print the hello of the following list
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

# Find a needle in a stack
def findWord(stack, needle):
	list = stack.split()
	for word in list:
		if word == needle:
			return True
	return False
print(findWord('Is there a dog here?', 'dog'))

# Count the number of occurences of a needle in the stack
def countOccurences(stack, needle):
	list = stack.split()
	count = 0
	for word in list:
		if word == needle:
			count += 1
	return count
print(countOccurences('This dog runs faster than the other dog dude!', 'dog'))

# Filter out strings starting with 's'
seq = ['soup','dog','salad','cat','great']
res = list(filter(lambda word: word[0] != 's', seq))
print(res)

# Write a function to determine if someone gets a ticket given a chance of 5km/h for birthday
def caught_speeding(speed, is_birthday=False):
	modif = 0
	if is_birthday:
		modif = 5
	if speed < (60 + modif):
		return 'No Ticket'
	elif speed > (60 + modif) and speed < (81 + modif):
		return 'Small Ticket'
	else:
		return 'Big Ticket'
ticket = caught_speeding(87, True)
print(ticket)

# Determine the sum of the days in a 30 day month
def month_sum():
	sum = 0
	for i in range(1,31):
		sum += i
	return sum
total = month_sum()
print("Le nombre total d'items a se departir est de {total}".format(total=total))