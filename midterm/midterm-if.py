#!/usr/bin/env python3
##auth: Duncan Peterson
#Midterm 1 Flow Control

#try python3 midterm/midterm-if.py midterm/Midterm-if.txt in command line.
import keyword
#from sys import argv
#script, filename = argv
print("Name: Duncan Peterson")
#print(f"The target file is: {filename}\n")

Total=int(0) #Initialize.
findme=["gmeach18@ed.gov","248.253.63.149","Whiteland","80.222.19.190","Kayley","dcassyqw@microsoft.com"]

with open('Midterm-if.txt',"r") as contents:
    headercontent = list(contents.readline()) #Enter the header because it's perhaps useful?
    for i in range(0,len(findme)):    #i is the index of the findme list, for strings we have to match.
        contents.seek(0)    #Go back to the BOF.
        contents.readline() #skip the first line by reading it and assigning it to nothing.
        for line in contents:
            Total += 1    #You read a line, now incriment the total
            linecontent=line.split(",")  #I'm just going to store the contents of the line as a list.
            linecontent[len(linecontent)-1]=f"{linecontent[len(linecontent)-1]:<.{len(linecontent[len(linecontent)-1])-1}s}"
            #We use this previous line to remove the LF character at the end of the last element of linecontent.
            #If we didn't, the IP addresses have a \n character at the end of them, which impedes searching.
            if findme[i] in linecontent:
                print (f"'{findme[i]}' found.")
                #print (f"Total={Total}")
                break
            if Total>=5000:
                print("Search taking too long :(")
                quit()
if Total==2425:
    print(f"Total is {Total}")
    print("Nailed it. :) ")
else: print(Total)

        

