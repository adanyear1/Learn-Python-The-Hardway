#Set the variable for the string that determines the number of people
types_of_people = 10
#make a string variable with the types of people int variable inside of the {}
x = f"There are {types_of_people} types of people"

#setting variables for strings that will be inserted inside of a sentance
binary = "binary"
do_not = "don't"

#make a string variable with the types of people int variable inside of the {}
y = f"Those who know {binary} and those who {do_not}"

#print out the x statement
print(x)
#print out the y statement
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

#a binary variable
hilarious = True
#setting a string variable 
joke_evaluation = "Isn't that joke so funny?! {}"

#print string variable
#format the specified values() and inserts them inside a strings placeholder
print(joke_evaluation.format(hilarious))

#setting w and e as a string variable
w = "This is the left side of..."
e = "a string with a right side"

#print a connotation of w and e
print(w + e)