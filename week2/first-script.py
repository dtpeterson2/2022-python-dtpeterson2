##auth: Duncan Peterson
##Desc: This script will demand to know if you're a teapot
#It also tests some things as practice for myself.
import keyword
import sys  #Lets us pass arguments when we run a script as a list: sys.argv
# sys.argv[0] is always the name of the script. 
# len(sys.argv) num of args
print(sys.argv[0])

authname="Duncan Peterson"
print(f"{authname}");

x="herp"
y="derp"
print(x+" "+y) #We can add strings this way
print(y,x)  #or we can add strings that way
count=[];
for i in range(1,4):
    count.append(i);
count.append('uh');
print(count);   #My baby don't mess around because she loves me soooo ♪
life=0;
while life < len(count):    #Hey so that's how you use __len__! Also, whiles work while true, and then they break
    life+=1
print("Health:"+"♥"*life);
elements=['earth','water','fire','wind','perfect being'];   #Aww shucks, the 5th element is actually the 4th index
print("The fifth element is the {}".format(elements[4]));   #Can't call lists like f"{elements}"", but you can call elements from it with []
#print("The fifth element is the "+elements[4]); #You can do it this way too. Think simpler.
while True: #This while loop is always true. The only way out of it is 'break'
    try:
        tea= int(input ("Are you a Teapot? [True/False] . . . > ")) #try: will run each line and will execpt if there's a problem
        break   #break when the tea=int(input()) succeeds. The while loop will keep asking until we succeed.
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