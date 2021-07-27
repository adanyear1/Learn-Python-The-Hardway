from sys import argv


stuff = input("Favorite Item")
car = input("Dream Car")
boat = input("Dream Boat")
script, stuff, car, boat = argv

print("The script is called:", script)
print("Random Letter:", stuff)
print("Land vehicle: ", car)
print("Water vehicle: ", boat)