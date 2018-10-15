#Input
n = int(input(""))
a = input("")
b = input("")
popSpots = 0

#Process
for i in range (0,n,1):
	if a[i] == b[i] and a[i] != ".":
		popSpots += 1

#Output
print(str(popSpots))