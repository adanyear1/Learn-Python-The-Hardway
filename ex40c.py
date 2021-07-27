mystuff = {'apple': "I AM APPLES"} # {} makes dictionary. It means 'apple' is 'I AM APPLES'
print(mystuff['apple']) # print 'apple' from 'mystuff' dictionary

import mystuff # take mystuff.py in this py file

mystuff.apple() # in mystuff.py, order apple is defined
print(mystuff.tangerine) # printing tangerine in mystuff.py


class MyStuff(object): # 'class' can making order. we make order 'MyStuff'
    def __init__(self):
        self.tangerine = "And now a thousand years between"
# __init__ is initialize. we define tangerine already. but using __init__, we make new tangerine

    def apple(self):
            print("I AM CLASSY APPLES!")


# end class MyStuff

thing = MyStuff()
thing.apple()
print(thing.tangerine)