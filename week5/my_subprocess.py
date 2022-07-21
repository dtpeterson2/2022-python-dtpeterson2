#!/usr/bin/env python3
##auth: Duncan Peterson

#We gonna do a subprocess
#Check docs.python.org/3/library/subprocesses.html for information.

import keyword
import subprocess

#part 1

#outFile = open('file_o.txt' , 'w')
errFile = open('file_e.txt' , 'w')
result=subprocess.run(['ps','-axco','command'],stdout=subprocess.PIPE)   
#ps is 'process status'. PIPE should stream the output if you have a Popen, and you can't give filnames when using PIPE
#-a is all processes, -x removes TTYs, -c shows the true command name instead of paths from where it ran.
#-o is user format which then requires an additional arg.
#There are 5 columns. 'PID, TTY, STAT, TIME, COMMAND.' By specifying 'command', you get just that column.

#print(result.stdout.split('\n'))    #You can't do this to bytes. You have to decode it.
#Hey wait, don't do decoding here, do it for part 2!

myProc=result.returncode    #Should probbaly be zero?

#part 2

myProcString=result.stdout.decode() #It's a string now.
#print(myProcString) #Jeepers. Don't print this unless you want to clear your console after that.
#resultDump='\', \''.join(resultDump)
myProcList=myProcString.split('\n')  #Now it's a list delimited by the line feeds.
#print(type(myProcList))
#Part 3. Use a for loop to print each process one line at a time. 
#Use slicing to skip the 'COMMAND' header.
myProcList=myProcList[1::1] #Skip the first element (which was actually 0) and then : to goto the end.
#print(type(myProcList)) #It's still a list.

for i in myProcList:
    print(i)

count=len(myProcList)   #We assigned with a splice that is less the header. Should be shorter.
print(f"ProcList length: {count}")    #here it is I could have {len(myProcList)} but I feel like it was wanted as an assignment first.