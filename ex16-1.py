from sys import argv

script, filename = argv

print(f"reading {filename} file.")
#reading file
target = open(filename)

print(target.read())
