#auth: Duncan Peterson
#Desc: Does stuff

varString="Here is a nice string to slice"
varList=["Here","is","a","nice","list","to","slice"]

#2 String slicing
#2a 'e is a nice string to slice'
print(f"{varString[3::1]}");

#2b 'Her'
print(f"{varString[:3:1]}");

#2c 'e is a ni'
print(f"{varString[3:12:1]}");

#2d 'Hr sanc tigt lc'
#it looks like we're skipping every other letter.
print(f"{varString[::2]}");

#2e 'ecils ot gnirts ecin a si ereH'
print(f"{varString[::-1]}");

#3 List slicing
#3a ['slice', 'to', 'list', 'nice', 'a', 'is', 'Here']
print(varList[::-1])    #Whyt does it say None?
#3b ['a', 'is', 'Here']
print(varList[2::-1])
#3c ['a', 'nice']

#3d ['Here', 'nice', 'slice']

#3e ['is', 'a', 'nice', 'list', 'to', 'slice']

#4 Use a for loop to print all elements of varString one at line at a time
"""
for i in range(1,len(varString)):
    print()
"""
#5 Use a for loop to print out all elements of varList one line at a time