#auth: Duncan Peterson
#Desc: This script will demand to know if you're a teapot
import keyword
import sys  #Lets us pass arguments when we run a script as a list: sys.argv
# sys.argv[0] is always the name of the script. 
# len(sys.argv) num of args
print(sys.argv[0])

authname="Duncan Peterson"
print(f"{authname}");

x="herp";
y="derp";
print(x+" "+y); #We can add strings$
"""
tea=int(0);
try:
    tea=(input("Are you a teapot? [True/False] . . .> "))
except ValueError:
    print("Boolean required")
print(tea);
print(type(tea));
tea = not tea;  #boolean invert
eval_teapot=f"Tea was not {tea}" #We can fill sets outside of prints.
print(eval_teapot)
"""

count=[];
for i in range(1,4):
    count.append(i);
count.append('uh');
print(count);   #My baby don't mess around because she loves me soooo ♪
life=0;
while life < len(count):    #Hey so that's how you use __len__!
    life+=1
print("Health:"+"♥"*life);
elements=['earth','water','fire','wind','perfect being'];   #Aww shucks, the 5th element is actually the 4th index
print("The fifth element is the {}".format(elements[4]));   #Can't call lists, but you can call elements from it
#print("The fifth element is the "+elements[4]); #You can do it this way too. Think simpler.
while True:
    try:
        tea= int(input ("Are you a Teapot? [True/False] . . . > "))
        break
    except ValueError:
        print("Please answer with an integer.")
"""
if tea == "1":
    tea = bool(True)
else:
    tea == "0"
    tea = bool(False)
"""
print(tea);
tea = not tea;
eval_teapot = f"The statement was not {tea}";
print(eval_teapot);
print(chr(916));    #print any UTF-8 characters this way
print(ord('Δ'));    #get the number of any UTF-8 character this way