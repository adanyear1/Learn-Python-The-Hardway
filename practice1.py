from sys import exit

print("How old are you?")
age = int(input())
if age > 18 and age < 45:
	print("You are of age")
elif age < 18:
	print("You are too young")
	exit()
elif age > 45:
	print("You are too old")
else:
	print("I don't understand")