#!/usr/bin/env python3
##auth: Duncan Peterson

#Argparse? Didn't we do this already?

import keyword
from sys import argv    #alternatively, import sys and use sys.argv
#argv is a list of arguments you gave in order, but the 0th element always returns the name of the script.
import argparse #This thing is way cooler than argv.

parser = argparse.ArgumentParser(description='I am the parser description. What does this even do?')
#The description is something you can check by doing ./argvtest.py -h in command line. It also tells you about all the 
#vars that get parsed.

#scriptname, firstarg = argv     #Oh boy.
#print(scriptname)
#print(firstarg)

#Arguments get added in order and are assigned in order unless otherwise defined.
#If you don't wanna add things in order, you can use flags.
parser.add_argument('teapot')   #This works, but it'll be required you add it. Unflagged vars get added in order.
parser.add_argument('-t', '--tea', dest='tea', type=str, help='No teapot is complete without tea') #You can 'safely' neglect to assign these.  
#-t is a switch flag. You can call it wherever followed by the input.
#-- allows you to make longer flags.
#dest is the variable this input will be assigned to
#help is text that will display when you -h
#type can forcefully typecast the input, but it data validates for you.
#default='' is something you can assign in case you want the variable to be something besides None if no input was given.
#required=True can make the input not optional
#metavar='str' can change the displayed name in help, but has no other function.
#action='store-true' For bools, it might be useful to know if the var got called at all. This tells you if it did.
#nargs='' Store a list off arguments. List type is implied- don't type=list or you'll get a list of lists. '3' means exactly 3, '?' is optional, '+' is one or more- same as '*'.
#For nargs, you can actually -l one -l two -l three, and you'll append each time and get ['one', 'two', 'three']
#action='append' lets you do this with other things without nargs by repeating the flag and giving another input.
#https://docs.python.org/3/library/argparse.html#the-add-argument-method for more information.

parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')    #Change version so you can help others know the ver of your script.
parser.add_argument('-l', dest='listvar', help='this should take a lot of arguments', nargs='+')

print(parser.parse_args())
myArgs=parser.parse_args()  #myArgs is gonna get attribute names corresponding to the parser arguments
#print(parser.teapot)    #no.

#In our case, this doesn't work because there are some required args that error automatically if not given.
if len(argv) ==1:   #The length will be 1 if nothing was given. This is a handy way to automatically trigger help.
    print(myArgs.print_help())

print(myArgs.teapot)    #Unflagged vars are required.
print(myArgs.tea)   #flagged vars are not required, but remember they will still exist as 'None' if not given a default value.
print(type(myArgs.tea))
print(myArgs.listvar)
print(type(myArgs.listvar))
print(parser.parse_args().teapot)