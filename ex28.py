car = True and True
#&& is invalid
print(car)

boeing = True and False
print(boeing)

if (1 == 1 and 2 == 1):
#same as True and False
	print("cierto")
else:
	print("Falso")

exam = "test" == "test"
print(exam)

if (1 == 1 and 2 != 1):
#true and true
	print("Neta Del Planeta")
else:
	print("No seas mamon")

if (1 == 1 and True):
#true and true
	print("Neta Del Planeta")
else:
	print("No seas mamon")

chevy = False and 0 != 0
print(chevy)

if (True or 1 == 1):
	print("Verdad")
else: 
	print("mentira")

if ("test" == "testing"):
	print("Kewl")
else:
	print("ehh")

boat = 1 != 0 and 2 == 1
print(boat)

print("test" != "testing")

if ("test" == 1):
	print("yes")
else:
	print("no")

print(not(True and False)) #true
print(not(1 == 1 and 0 != 1)) #false
print(not(10 == 1 or 1000 == 1000)) #false
print(not(1 != 10 or 3 == 4)) #false
print(not("testing" == "testing" and "Zed" == "Cool Guy")) #true
print(1 == 1 and (not(3 == 4 or 3 == 3)))
print("chunky" == "bacon" and (not(3 == 4 or 3 == 3)))
print(3 == 3 and (not("testing" == "testing" or "Python" == "Fun")))