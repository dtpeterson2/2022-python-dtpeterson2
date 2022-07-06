import keyword




print("I'm a teapot."\
    " This is a line return being used") #any space after '\' is an error. you must hit return after a '\'.
print(type("Teapot"))
xname = "Teapot" #I'm a var
print(418, xname) #We can print vars
print("teapot".islower())
print(f"You are a... {xname}"); #{xname} string append. Not prefixing f will make the str literal and you'll see the {xname} verbatim
y = input("Are you a teapot? Press y to continue . . . > ")
if y.__eq__('y'):
    print("You are a teapot");
    tea=True
else:
    tea=False
x="herp";
y="derp";
print(x+" "+y); #We can add strings
eval_teapot = "Tea was {}"
print(eval_teapot.format(tea))  #.format(value, special), returns the value to an arg in a string. value can be a string too

#Week 2 stuff
tea = not tea;  #boolean invert
eval_teapot=f"Tea was not {tea}" #We can string append outside of prints. Duh
print(eval_teapot)
life=0;
print("Health:"+"♥"*life); #You can't just do {life} because it's a set instead of a value
print("derp"\
" herp")
   #unlike MATLAB, you can't operate on nothing- it won't get made automatically.
count=[];
for i in range(1,4):
    count.append(i);
count.append('uh');
print(count);   #My baby don't mess around because she loves me soooo ♪
while life < 10:
    life+=1
print("Health:"+"♥"*life);
elements=['earth','water','fire','wind','perfect being'];   #Aww shucks, the 5th element is actually the 4th index
print("The fifth element is the {}".format(elements[4]));   #Can't call lists, but you can call elements from it
#print("The fifth element is the "+elements[4]); #You can do it this way too. Think simpler.


"""
Behold, a giant comment
Look at me go.

python3 -c 'print(''I am a teapot'')' 
works in command line, but remember it's double singles and not a quote like this (")
This is probably a PowerShell thing. Bash is okayh with (")
"""
z="toot"
print(f"{z:z^10s}") #^ is the direction
print(f"{z:z<10s}") #s is the data type. Valids are "s, d, f, c, x (hex 'base 16'), X (HEX), b (binary 'base 2'), o (octal 'base 8, 3 bit'), e"
print(f"{z:z>10s}") #This formatting allows us to add padding of a desired char and data type
print(f"{z:z<.2s}") #We can delete things too by using a dot.
subnet=[255,255,255,0]
print(f"{subnet[0]:0>8b}.{subnet[1]:0>8b}.{subnet[2]:0>8b}.{subnet[3]:0>8b}")
#An interesting way to get 8bit binary for addresses

import shutil
dimension=shutil.get_terminal_size()    #Returns an object with an attr called .lines and .columns
print(f"CMD y:{dimension.lines}")
print(f"CMD y:{dimension.columns}") #Use this to format strings to fit into the command window.

print("""big fat
block
of text, wow look at me go
""")