#Drug Smuggler 2021

from sys import exit
from random import randint
from textwrap import dedent
import time
import math

#back-end initialization classes
class Scenario(object):

	def enter(self):
		print("This scenario is not yet configured")
		print("Subclass and implement enter().")
		exit(1)

class Engine(object):
	
	def __init__(self, scenario_travel):
		self.scenario_travel = scenario_travel

	def play(self):
		current_scenario = self.scenario_travel.opening_scenario()
		last_scenario = self.scenario_travel.next_scenario('finished')

		while current_scenario != last_scenario:
			if current_scenario != None:
				next_scenario_name = current_scenario.enter()
				current_scenario = self.scenario_travel.next_scenario(next_scenario_name)
			else:
				break

		#be sure to print out the last scene
		current_scenario.enter()

#introduction
class Introduction(Scenario):
	
	#this function prints out the background story of the game
	def enter(self):
		print("You are a 20 year old ghetto kid from Medellin Colombia")
		print("Your friend gave you 1kg of coke to smuggle from Colombia") 
		print("to Mexico, Its up to you to find the best way to get it there")
		print("You have 3 transport methods bus, airplane, or boat")

		action = input("> ")

		if action == "bus":
			print("You catched the bus from Medellin Terminal Norte to the")
			print("border with Panama, where you are goin to have a wild adventure")
			return 'bus'
		elif action == "plane":
			print("You swallowed the drugs and nearly died on the flight")
			return 'plane'
		elif action == "boat":
			print("The next morning you took a boat of the coast of Colombia")
			return 'boat'
		else:
			print("Enter bus, plane or boat")
			return 'introduction'

#3 methods 
class Bus(Scenario):
	
	def enter(self):
		print("Through your Journey in the Colombian Jungle you got shot at and")
		print("Kidnapped, fortunatly your buddy found out and sent your ransom")
		print("Unfortunatly, the Panamanian police threw you in jail 3 days later")
		return 'arrest'

class Boat(Scenario):

	def enter(self):
		print("3 days later you got caught by the Mexican Marines and got shot at")
		print("You died when you drowned")

class Airplane(Scenario):
	
	def enter(self):
		print("You arrived in Mexico got tortured by Mexican Authoroties")
		print("But the drugs made it")
		return 'finished'

#bust or pass
class Arrested(Scenario):

	def enter(self):
		print("You got thrown in jail for drug trafficking and have no bail money")
		print("Have fun for the next month")
		return 'debt'
		
class Debt(Scenario):

	def enter(self):
		print("You realize you lost the drugs because of your misfortunes?")
		print("So you manage to escape from jail")
		print("How do you recover the 1kg of cocaine to pay back your friend")
		print("You can either steal coke, beg for forgiveness, or immigrate to the us")
		print("Enter steal, beg, or immigrate")

		action = input("> ")

		if action == "steal":
			print("You robbed a local drug lord of his cocaine and your going to continue your way")
			print("North to Mexico")
			print("With no reprecussions you made it to Mexico")
			return 'finished' 

		elif action == "beg":
			print("You go back to Medellin to beg your friend for forgiveness")
			print("With Hopes of him letting you go free")
			return 'death'

		elif action == "immigrate":
			print("You decide to go to the USA and never think about cocaine again")
			print("You married a white girl and got papers but never saw Medellin again")
			exit(1)

		else:
			return 'debt'

class Death(Scenario):

	def enter(self):
		print("You got murdered for smmugling drugs")
		print("You ended up in a body bag on the side of street")
		print("and your mom never got to bury you")
		exit(1)

class Finished(Scenario):
	
	def enter(self):
		print("You got the drugs to Mexico")
		print("Have won $15000 now go have fun")

#engines and run game
"""This class allows you to orginize your classes in the order that events will occur"""
class Travel(object):

	"""categorizing the scenarios"""
	"""'abbreviated class name': class name"""
	scenarios = {
		'introduction': Introduction(),
		'bus': Bus(),
		'arrest': Arrested(),
		'debt': Debt(),
		'plane': Airplane(),
		'boat': Boat(),
		'death': Death(),
		'finished': Finished(),
	}

	def __init__(self, start_scenario):
		self.start_scenario = start_scenario

	def next_scenario(self, scenario_name):
		val = Travel.scenarios.get(scenario_name)
		return val

	def opening_scenario(self):
		return self.next_scenario(self.start_scenario)


a_travel = Travel('introduction')
a_game = Engine(a_travel)
a_game.play()