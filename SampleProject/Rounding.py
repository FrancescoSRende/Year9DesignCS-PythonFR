number = float(input("Input a number: "))

print(round(number, 2)) #Round automatically goes to a whole number

number = number * 100
number = round(number)
number = number / 100
print(number)