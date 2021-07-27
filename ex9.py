#Here's some new strange stuff, remember type it exactly

days = "Mon Tue Wed Thurs Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

for val in months:
    if val == "a":
        break
    print(val)

print("The end")

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")