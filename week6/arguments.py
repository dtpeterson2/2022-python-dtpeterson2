#!/usr/bin/env python3
##auth: Duncan Peterson

import keyword
import argparse #This thing is way cooler than argv.

parser = argparse.ArgumentParser(description='This is %(prog)s script')
parser.add_argument('-m', dest='basic', help='Enter some text') #You can 'safely' neglect to assign these.  
parser.add_argument('-i', '--integer', metavar='[an integer]', dest='integer', type=int, required=True, help='<required> Enter a simple Integer')
parser.add_argument('-d', '--float', metavar='[a float]', dest='float', type=float, help='Enter a simple float')
parser.add_argument('-s', '--string', metavar='[a string]', dest='string', type=str, help='Enter a simple string')
parser.add_argument('-l', metavar='[strings]', dest='stringlist', nargs='+', help='Enter a list of strings (space delimited)') #DON'T type=list WHEN YOU NARGS OR YOU'LL GET ODD BEHAVIOR! LIST IS ALREADY IMPLICIT.
parser.add_argument('-t', '--set-true', dest='default_false', default=False, action='store_true', help='Toggle from default False to True') #action='store_true' forbids 'type' and any manner of user input.
parser.add_argument('-f', '--setfalse', dest='default_true', default=True, action='store_false', help='Toggle from default True to False')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0', help='show program\'s version number and exit')    #action='version' expects version keyword.
parser.add_argument("echo", help="")
myArgs=parser.parse_args()

#for i in myArgs:   #No, the Namespace isn't iterable. Too bad :C
#    print(i)
#print(dir(myArgs)) #You can actually see the namespace by doing this :D

print(myArgs.integer)
print(myArgs.string)
print(myArgs.float)
print(myArgs.stringlist)
#These are the args we were instructed to echo.
