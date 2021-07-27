i = 0
numbers = []

#while-loop will iterate 6 times or 0 - 5
while i < 8:
	print(f"At the top i is {i}")
	numbers.append(i)

	#print each statement 6 times 0 - 5
	i = i + 2
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
	print(num)

print("Code bellow will be written using a function")

def whilefunc(i, x, numbers):
	numbers = []
	if (i < x):
		print(f"At the top i is {i}")
		numbers.append(i)	
		
		i += 1
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
		whilefunc(i, x, numbers)
	return numbers

numbers = whilefunc(0, 6, [])

for num in numbers:
	print(num)
