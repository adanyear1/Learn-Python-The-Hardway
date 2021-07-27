print("""You are riding a rocky trail on a Trek Mountain Bike.
Is your bike a hardtail or full_suspension?""")

bike = input()

if bike == "hardtail":
	print("Are you excited for a bumpy trail?")
	print("yes or no")

	response = input()
	
	if response == "yes":
		print("Have fun don't sit for too long")
	elif response == "no":
		print("Ride the gravel trail")
	else:
		print("The trails aren't that hard")

elif bike == "full_suspension":
	print("your bike is fit for this park")

else:
	print("Find an easier trail")