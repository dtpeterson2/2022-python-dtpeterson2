#!/usr/bin/env python3
##auth: Duncan Peterson

#Here, we will write things that do things so we never have to write them again.

import keyword

var_global="I'm global"
var_1="Defined first."
print(var_1)
print("define the function.")
def functest():
    var_local="I exist only within the function."
#    print(var_1)   #Error. Even though var_1 is a global, you can't do anything with it if it's colliding with a local in the function, even if it's in the future.
    #Maybe this is a compile-time feature?
    print("herp")
    print(var_global)   #Globals can get referenced inside functions.
    var_1="I'm gonna collide with a global"
    print(var_1)

def multivar(arg1, arg2): #Functions aren't like scripts that can only take a single argv. We can have a lot of inputs with funcs.
    print(arg1)
    print(arg2)

def allvars(*arg):  #This takes as many args as you want and assigns them as a list.
    for i in arg:
        print(i)
    return print("wow")

allvars("The","Quick","Brown","Fox")

import funcmain #You can import scripts to gain the functionality of the defined functions within.

email_address = funcmain.create_tea("Teapotmail")
print(f"Email Address: {email_address}")
#It turns out that when we call things from funcmain, funcmain runs in its entirety excluding any failed conditionals.

#Lets try calling directly.
callingmain = funcmain()    #I know it returns None, but lets see what happens.


