#auth: Duncan Peterson
#Desc: Demonstrates string modification abilities of python3

import keyword

varRed="Red";
varGreen="Green";
varBlue="Blue";
varName="Timmy";
varLoot=10.4516295;

#1: 'Hello Timmy'
print(f"Hello {varName}");
#2: 'Red-Green-Blue'
print(f"{varRed}-{varGreen}-{varBlue}");
#3: 'Is this green or blue?'
print(f"Is this {varGreen.lower()} or {varBlue.lower()}")
#4: 'My name is TIMMY'
print(f"My name is {varName.upper()}");
#5: '[++Red++]'
print(f"[++{varRed}++]");   #We don't need escape \ for these symbols.
#6: '[green==]'
print(f"[{varGreen.lower()}==]");
#7: '[*****blue]'
print("*"*5+f"{varBlue.lower()}");
#8: 10 Blues.
print(f"{varBlue}"*10);
#9: the number
print(varLoot)  #Think simple.
#10: '10.5'
print(round(varLoot,1))   #Try rounding
#11 'I have $10.45'
print(f"I have ${round(varLoot,2)}")
#12 '[$$$Red$$$$] [$$Green$$$] [$$$Blue$$$]'
print(f"[{varRed.center(10, '$')}]",f"[{varGreen.center(10, '$')}]",f"[{varBlue.center(10, '$')}]")
#Don't have to pad the end if you use , isntead of +
#13 '[   deR    ] [  Green   ] [   eulB   ]', reverse the strings somehow.
print(f"[{varRed[::-1].center(10, ' ')}]",f"[{varGreen[::1].center(10, ' ')}]",f"[{varBlue[::-1].center(10, ' ')}]")
#[::-1] is [start:stop:step]. It reads the string like a set with delimiters omitted to read all, and reads in reverse.
#14 'First Color:[Red] Second Color:[Green] Third Color:[Blue]'
print(f"First Color:[{varRed}]",f"Second Color:[{varGreen}]",f"Third Color:[{varBlue}]")
