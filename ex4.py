#setting the variable for cars 
cars = 100
#setting the variable for space in a car
space_in_a_car = 4.0
#setting the variable for drivers
drivers = 30
#setting the variable for passengers
passengers = 90
#setting the variable for cars not driven
cars_not_driven = cars - drivers
#setting the variable for cars driven
cars_driven = cars - cars_not_driven
#setting the variable for carpool capacity
carpool_capacity = cars_driven * space_in_a_car
#setting the variable for avg passengers per car
average_passengers_per_car = passengers / cars_driven

#print number of cars available
print("There are", cars, "cars available")
#print number of drivers available
print("There are only", drivers, "drivers available")
#print number of cars not driven
print("There will be", cars_not_driven, "empty cars today")
#print carpool capacity
print("We can transport", carpool_capacity, "passengers today")
#print number of passengers
print("We have", passengers, "to carpool today")
#print number of passengers per car
print("We need to put about", average_passengers_per_car, "in each car.")