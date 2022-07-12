#!/usr/bin/env python3
##auth: Duncan Peterson
##We're just playing around with dictionaries here.
import keyword

things = ['a','b','c','d']
print(f"things: {type(things)}")
print(things[1])
print(things)
#This is just a list. Boring.

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}    #What happens when we do these colons...???
print(f"Stuff: {type(stuff)}")
print(stuff['name'])    #Dicts are indexed by things. We can call the index but not the thing it represents.
    #You're calling elements of a list. You can't call a bad element.

dorts = {1,2,3,5}
print(f"dorts: {type(dorts)}")
print(dorts)

states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

#You can append things to a dict this way. It's not ordered.
#cities['NY'] = 'New York'
#cities['OR'] = 'Portland'

for state, acronym in list(states.items()): #You don't actually have to typecast this, but some codes may do this as a precaution of some versions working differently than others.
    #the 'state, acronym' is assigning names to the tuple pairs returned by states.items()
    print(f"{state} is {acronym}")
    print(f"{acronym} is {state}")

print("\n")
print("-"*32)

#Try to enter the result as an argument to search another dict.
for state, acronym in list(states.items()):
    print(f"{state} is {acronym}")
    #try:
    #    print(f"{acronym} indexes {cities[acronym]} in cities") #Remember, this will KeyError: if you ask for a bad index. This will handle it and move on.
    #except KeyError:
    #    print(f"{acronym} is not found in cities")
    #A FAR SAFER WAY TO DO THE ABOVE IS TO .get()
    if not cities.get(acronym):
        print(f"{acronym} refers to a bad index")
    else:   #If not None, then clearly something.
        print(f"{acronym} indexes {cities.get(acronym)} in cities")

