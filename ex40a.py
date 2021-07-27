mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

import mystuff

mystuff.apple()
print(mystuff.tangerine)

class MyStuff(object):
	
	def _init_(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print("I am classy apples!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)