#create a mapping of state to abbreviation
states = {
	'Zacatecas': 'Zac.',
	'Jalisco': 'Jal.',
	'Nuevo Leon': 'N.L.',
	'Michoacan': 'Mich.',
	'Sinaloa': 'Sin.',
}

#create a basic set of states and some cities in them
cities = {
	'Zac.': 'Zacatecas',
	'N.L.': 'Monterrey',
	'Mich.': 'Morelia',
}

#add some more cities
cities['Sin.'] = 'Culiacan'
cities['Jal.'] = 'Guadalajara'

#print out some cities
print('-' * 10)
print(cities['Sin.'], "is Sinaloa's capital city")
print(cities['Jal.'], "is Jalisco's capital city")

#print some states
print('-' * 10)
print("Zacatecas' Abbreviation is: ", states['Zacatecas'])
print("Jalisco's Abbreviation is: ", states['Jalisco'])

#do it by using the state then cities dict
print('-' * 10)
print("Michoacan has: ", cities[states['Michoacan']])
print("Nuevo Leon has: ", cities[states['Nuevo Leon']])

#print out every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the {city}")

#now do both at the same time 
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('Sonora')

if not state:
	print("Sorry, no Sonora.")

#get a city with default value 
city = cities.get('Son.', 'Does not exist')
print(f"The city for the state 'Son.' is: {city}")