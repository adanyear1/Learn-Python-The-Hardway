#This program will help you choose a bike
#depending on the state you live in and
#trails you ride

def budget():
	print("What is your budget?")
	price = input("> $")
	global budget 
	budget = int(price)

def fullsuspension_budget():
	budget()

	if budget < 1200:
		print("Buy used on facebook marketplace")
	elif budget > 1201 and budget < 1700:
		print("Buy a Giant Stance 1")
	elif budget > 1701 and budget < 2500:
		print("Buy a Giant Trance 1")
	elif budget > 2501:
		print("Buy a Trek Fuel Ex")
	else:
		print("Enter another purchase value")
def texas():
	print("Are you going to be downhill riding?")
	print("yes/no")
	
	response = input("> ")

	if response == "no": 
		print("Buy a hardtail")
		hardtail_budget()
	elif response == "yes":
		print("Buy a full suspension bike")
		fullsuspension_budget()	
	else:
		print("Enter another response")
		texas()
	
def hardtail_budget():
	budget()
	if budget < 200:
		print("Buy used on Facebook Market Place")
	elif budget > 201 and budget < 400:
		print("We recommend a Schwinn Standpoint")	
	elif budget > 401 and budget < 500:
		print("A GT Agressor is best suited for you")
	elif budget > 501 and budget < 600:
		print("Buy a Trek Marlin 5")
	elif budget > 600:
		print("Buy a Trek Marlin 8")
	else:
		print("Enter another value")


def utah():
	print("Buy a full suspension bike")
	fullsuspension_budget()

def start():
	print("Are you going to be riding in Texas or Utah")
	
	choice = input("> ")

	if choice == "Texas":
		texas()
	elif choice == "Utah":
		utah()
	else:
		print("Choose Texas or Utah")
		start()

start()

		