class Parent(object):

	def implicit(self):
		print("PARENT implicit()")

class Child(Parent):
	
	def override(self):
		print("Child override()")

dad = Parent()
son = Child()

dad.implicit()
son.override()
