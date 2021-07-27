#import the argv (argument variable) module/library
#from sys import argv

#filename = "ex15_sample.txt"

#creates two argument variables 
#script, filename = argv

#Sets variable 'txt' to function 'open()' which itself pulls in the filename argv
#txt = open(filename)

#print(f"Here's your file {filename}:")
#print(txt.read())
#prints filename 

#Show user promopt to type in filename 
print("Type the filename again:")
file_again = input(">>> ")

txt_again = open(file_again)

print(txt_again.read())

#pythotxt.close()
txt_again.close()