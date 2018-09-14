#Strings are collections of characters, which are enclosed in "" or ''

#Indexes:
#  012345	 0123456
# "Stalin"	'Nirvana'

#Length:
# len("Stalin") = 6
# len('Nirvana') = 7

name = "Сталин"
print(name) #You can print strings

sentence = name + " was right"
print(sentence)
print(sentence + "!")

firstLetter = name[0] #name at 0
print(firstLetter)
letters1 = name[0:2] #inclusive:exclusive
print(letters1)
letters2 = name[2:]
print(letters2)
letters3 = name[:2]
print(letters3)
lname = len(name)
print(lname)
for i in range(len(name)):
	print(name[i])