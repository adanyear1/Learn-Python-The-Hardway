name = 'Manuel Garcia'
age = 24.0
height = 188.0
weight = 190.0
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

in_to_cm = float(2.54)
heightin = height/in_to_cm 

print(f"Let's talk about {name}.")
print(f"He's {heightin} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually he is not that heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky try to get it right
total = age + heightin + weight
print(f"If I add {age}, {heightin}, and {weight} I get {total}")