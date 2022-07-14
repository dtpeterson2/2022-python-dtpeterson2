#!/usr/bin/env python3
##auth: Duncan Peterson
#Midterm 1 Flow Control

#try python3 midterm/midterm-slicing.py midterm/slicing-file.txt in command line.
import keyword
#from sys import argv
#script, filename = argv
print("Name: Duncan Peterson")
#print(f"The target file is: {filename}\n")

with open('midterm/slicing-file.txt',"r") as file:  #load the file as something we can play with.
    file.seek(0)    #I got some odd behavior so I'm gonna seek the BOF just in case.
    contents=list(file.readlines())
    print(contents)
#4 Create variables for each item and use a SINGLE slice to get the correct words
#4a the third word from the EOF
    fourA=str(f"{contents[-3:-4:-1]}")   #When you go negative, 0 is the EOF, and -1 is the last line before EOF.    #[-3:-4:-1]
#4b the 3rd through 5th words.
    fourB=f"{contents[2:5:1]}"  #Remember, the 2nd index is the 3rd line. Lists begin at 0, but not in reverse- then the 0th is the EOF and -1 is the last line
#4c The 10th word from the EOF, and every other word for a total of 3 words.
    fourC=f"{contents[-10:-15:-2]}"
#4d The 11th through 13th words.
    fourD=f"{contents[10:13:1]}"
#4e the 19th through 21st words from the EOF
    fourE=f"{contents[-19:-22:-1]}"
    #print(contents[1])
    print("")   #blank line
#5. Add each word to a new string. Some slices will return a list. Use join() to join the list into a single string
    #combined=str(' ').join([fourA, fourB, fourC, fourD, fourE])    #nice try, but doing this with a list results in some weird behavior.
    #You can only give join a single argument.
    combined=str('').join([fourA])
    combined=combined.replace("[","")    #Delete these.
    combined=combined.replace("]","")    #Delete that.
    combined=combined.replace("\n"," ")   #No more line feeds... Why is this so stubborn?
    combined=combined.replace("'","")   #No single quotes.

#6. Print the quote. you can use .replace() to remove end of line characters.
    print(combined)
    #Why is the LF so stubborn?

#7. Test your script. If you did everything right, you'll see: "Whether you think you can or you think you can't, you are right."