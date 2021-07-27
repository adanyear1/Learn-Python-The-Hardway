#program to practice all the python symbols

#Make a restaurant total calculator
#make a Tip calculator
#practice for, while loops
#practice if, elif, else
#practice math symbols

def start():
	custOrder = []

	print("How Many Customers Are At Table?")
	custNum = int(input())
	
	for i in range(0, custNum):
		print("Enter Price of Item")
		ele = int(input())
		custOrder.append(ele)
	
	print(custOrder)
	subtotal = sum(custOrder)
	print("Your subtotal is $", subtotal)
	
	tax = subtotal * 0.0825
	tip = subtotal * 0.2
	total = subtotal + tax + tip	
	print("Your total is $", total)
start()


