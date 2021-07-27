def add(a, b):
	print(f"ADDING {a} +{b}")
	return a + b

def subtract(a, b):
	print(f"SUBTRACTING {a} + {b}")
	return a - b

def multiply(a, b):
	print(f"MULTIPLYING {a} + {b}")
	return a * b

def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b

print("Let's do math with just functions")

age = add(300, 50)
height = subtract(780, 400)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight} IQ: {iq}")

#A puzzle for extra credit
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
kewl = multiply(age, height) + add(age, subtract(height, iq))
london = multiply(weight, multiply(age, divide(iq, 4)))
lhr = subtract(age, add(height, divide(weight, multiply(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

print("That becomes: ", kewl, "Can you do it by hand?")

print("That becomes: ", london, "Can you do it by hand?")

print("That becomes: ", lhr, "Can you do it by hand?")









