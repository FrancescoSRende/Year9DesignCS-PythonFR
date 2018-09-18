firstName = input("Hello human! Can I have your first name please? ")
lastName = input("Thank you, homo sapiens! May I also have your last name? ")
print("Many thanks, "+firstName[0]+". "+lastName+",living creature of the species homo sapiens!")
lengthFirstName = len(firstName)
lengthFirstName = int(lengthFirstName)
lengthLastName = len(lastName)
lengthLastName = int(lengthLastName)
codeName = lastName[-3]+firstName[0]+lastName[2:lengthLastName]+firstName[1:-2]
print("Farewell "+codeName+".")