#This is practice code for functions
#The purpose of this program is to help determine a user if he can buy a home in ATX

salary = input("> $")

def salary():
	wage = int(salary)
	print("What is your yearly salary?", wage)

	print("Your salary is $", wage)

def decision():
	if salary <= 60000:
		print("You can't afford a house")
	elif salary >= 60001:
		print("You can afford a house")
	else:
		print("Enter another response") 	

def start():
	print("Congratulations on taking the next step to buy a home")
	print("Do you have credit score above 700")
	print("Enter yes or no")
	
	response = input("> ")
	if response == "yes":
		salary()
	elif response == "no":
		print("You need to improve your credit score")
	else:
		print("Enter another response!")

start()	


	