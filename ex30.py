#set variable for no. of people
people = 59
#set variable for no. of cars
cars = 44
#set variable for no. of trucks
trucks = 64

#if statement checking if their are more cars than people
if cars > people:
	#print out if condition is met
	print("We should take the cars")
#if statement checking if their are more people than cars
elif cars < people:
#print out if condition is met
	print("We should not take the cars")
#else condition checking if conditions are not met
else:
#print out if condition is not met
	print("We can't decide")

if trucks > cars:
#print out if condition is met
	print("That's too many trucks.")
elif trucks < cars:
#print out if condition is met
	print("Maybe we could take the trucks")
#else condition checking if conditions are not met
else:
#print out if condition is not met
	print("We still can't decide")

if people == trucks and people == cars:
	print("Takewhat ever")
else:
	print("Need to choose between car or truck")

if people < trucks:
#print out if condition is met
	print("Alright, let's just take the trucks")
#else condition checking if conditions are not met
else:
#print out if condition is not met
	print("Fine let's stay home")
