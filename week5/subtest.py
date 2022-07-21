#!/usr/bin/env python3
##auth: Duncan Peterson

#Holy crap how do subprocesses work?

import keyword
import subprocess

#print(type(subprocess.run(['ls', '-la'])))    #This will literally show the contents of the current dir
#Make sure you give a list if you wanna give more arguments. You can't write 'ls -la'
#It's because some arguments require values.

#The subprocess vomits to the console when you run.
#bytes are the default.

#procComplete= subprocess.run(['ls'],stdout=subprocess.PIPE) #ps -ef can view processes like a tskmngr
#print(type(procComplete))
#print(procComplete)
#output=procComplete.stdout.decode().split('\n') #String Decode translates the bytes to a string.
#.split creates new elements deliminted by the specified characters.
#print(output)

#.stderr can write stuff if something goes wrong.
#You can write logfiles by opening a file, even if it doesn't already exist.
#'a' is the append mode which allows writing.
StdOutFile = open('file_o.txt' , 'w')
StdErrFile = open('file_e.txt' , 'w')
resultant=subprocess.run(['ls','-la'],stdout=StdOutFile,stderr=StdErrFile)
StdOutFile.close()
StdErrFile.close()

#Before Python 3.5, you used .call() on subprocess which behaves a lot like .run()
#This operation returned the exit code integer, and was synchronous (execution blocking)

#For threaded processes, .Popen() is asynchronous. Execution will continue and you can't read until the thread is done.
#Output is read usiong subprocess.communicate()

result = subprocess.Popen(['ls','-la'], shell=True) #shell=true tells to run through bash.
print(result)   #This command is fast, and it's done by the time you read.
#There's a possibility that if it's not done, reading will return None!
#Check docs.python.org/3/library/subprocesses.html for information.