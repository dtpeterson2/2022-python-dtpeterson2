#!/usr/bin/env python3
#auth: Duncan Peterson
#Desc: Demonstrates string modification abilities of python3

import keyword

varRed="Red"
varGreen="Green"
varBlue="Blue"
varName="Timmy"
varLoot=10.4516295

#1: 'Hello Timmy'
print(f"Hello {varName}")

#2: 'Red-Green-Blue'
print(f"{varRed}-{varGreen}-{varBlue}")

#3: 'Is this green or blue?'
print(f"Is this {varGreen.lower()} or {varBlue.lower()}")

#4: 'My name is TIMMY'
print(f"My name is {varName.upper()}")

#5: '[++Red++]'
#print(f"[++{varRed}++]");   #Use string formatting instead of just typing it in, smartie.
#< makes it left align. ^ centers it. > puts it on the right.
#Valids are "s (str), d (dict?), f (Float), c, x (hex 'base 16'), X (capitol HEX), b (binary 'base 2'), o (octal 'base 8, 3 bit'), e" and some others.
print(f"{varRed:+^7s}")

#6: '[green==]'
#print(f"[{varGreen.lower()}==]")
#Use string formatting instead of just typing it in, smartie.
print(f"{varGreen.lower():=<7s}")

#7: '[*****blue]'
#print("*"*5+f"{varBlue.lower()}")
#Close, but you're supposed to use string formatting.
print(f"{varBlue.lower():*>9s}")

#8: 10 Blues.
print(f"{varBlue}"*10)

#9: the number
print(varLoot)  #Think simple.

#10: '10.5'
# print(round(varLoot,1))   #You're intended to split, and use the 'f' datatype for float, though round() works too
print(f"{varLoot:<.1f}")  #When you use a float type, it rounds to the specified decimal. It's kinda smart!

#11 'I have $10.45'
#print(f"I have ${round(varLoot,2)}")   #Use the formatting and splitting to help round.
print(f"I have ${varLoot:<.2f}")

#12 '[$$$Red$$$$] [$$Green$$$] [$$$Blue$$$]'
#print(f"[{varRed.center(10, '$')}]",f"[{varGreen.center(10, '$')}]",f"[{varBlue.center(10, '$')}]")
#Yes, the strings have a width of 10, now do it with formatting instead of functions.
print(f"[{varRed:$^10s}]",f"[{varGreen:$^10s}]",f"[{varBlue:$^10s}]")  #Much shorter!
#Don't have to pad the end if you use , isntead of +

#13 '[   deR    ] [  Green   ] [   eulB   ]', reverse the strings somehow.
#print(f"[{varRed[::-1].center(10, ' ')}]",f"[{varGreen[::1].center(10, ' ')}]",f"[{varBlue[::-1].center(10, ' ')}]")
#.reverse returns None. Don't use it here.
#[::-1] is [start:stop:step]. It reads the string like a set with delimiters omitted to read all, and reads in reverse.
#Use the formatting instead of center. Strings have a width of ten.
print(f"[{varRed[::-1]: ^10s}]",f"[{varGreen[::1]: ^10s}]",f"[{varBlue[::-1]: ^10s}]")  #Now wasn't that much shorter?

#14 'First Color:[Red] Second Color:[Green] Third Color:[Blue]'
print(f"First Color:[{varRed}]",f"Second Color:[{varGreen}]",f"Third Color:[{varBlue}]")
