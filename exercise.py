print(7**4)

aString = 'Hi there Sam!'

aList = list(aString.split())

print(aList)

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

planet = "Earth"
diameter = 12742

print('The diameter of the {planet} is {distance} km'.format(planet=planet, distance=diameter))

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

print(lst[3][1][2][0])

def findWord(stack, needle):
	list = stack.split()
	for word in list:
		if word == needle:
			return True
	return False

print(findWord('Is there a dog here?', 'dog'))

def countOccurences(stack, needle):
	list = stack.split()
	count = 0
	for word in list:
		if word == needle:
			count += 1
	return count

print(countOccurences('This dog runs faster than the other dog dude!', 'dog'))

seq = ['soup','dog','salad','cat','great']

res = list(filter(lambda word: word[0] != 's', seq))
print(res)

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