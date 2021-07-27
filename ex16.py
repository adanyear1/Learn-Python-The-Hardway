from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

print("?")

#open text file
print("Opening the file...")
target = open(filename, 'w')

#print("Truncating the file. Goodbye!")
#target.truncate()

#Set input text
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#Code to write text in file
target.write(line1+"\n"+line2+"\n"+line3)

print("And finally, we close it.")
target.close()