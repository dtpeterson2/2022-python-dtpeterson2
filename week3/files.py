#!/usr/bin/env python3
##auth: Duncan Peterson
##Desc: This script showcases file read python capabilities
import keyword

print("\n") #break

#1. Open passwd and read only and save it all to a string

with open("/etc/passwd","r") as pw1:
    #pw1 represents the file. we can't do much with it yet.
    contents1 = pw1.read()
    print(f"File char length: {len(contents1)}")
    print("passwd now read as contents1. We can control contents1 however we please,\
        \n and write to a file later")
    #This saved contents1 as the whole thing. We can close and do anything we want.
    #del contents1
    #pw1.close()    #Not needed because the file closes at the DEDENT

print("\n") #break

#2. Open passwd and save it to a list.
with open("/etc/passwd","r") as pw2:
    contents2 = pw2.readlines()
    print(f"File row length: {len(contents2)}.")
    print("passwd now read as contents2. We can control contents1 however we please,\
        \n and write to a file later. \n \
        It's perhaps easier to navigate large files by line, but we may lose \n \
        sense of relationship between columns doing it this way.")
    #pw2.close() #Not needed because the file closes at the DEDENT

#3. Open passwd and save it to a variable line by line.

#STOP THIS MADNESS. Use a for lines in pw3 loop.
"""
with open("/etc/passwd","r") as pw3:
    contents3="" #init
    while True:
        pos = pw3.tell()
        print(pos)
        if pw3.readline=="": #Nothing left.
            pw3.seek(pos,0) #Go back so we're exactly at the EOF.
            break
        else:
            contents3 = contents3+pw3.readline()
            print(contents3)

    print(contents3)
    print(type(contents3))

    pw3.close()
"""
print("\n") #break
with open("/etc/passwd","r") as pw3:
    contents3="" #init
    pw3.seek(0,0)
    for line in pw3:
        contents3 = contents3 + line    # You actually can't tell() during a for loop in a file
    print(f"File length: {len(contents3)}") #The sane way to do things.
    print("""I imagine we can use a for loop to check the whole file, and an if: statement
    to check for a peculiarly formatted block. 
    In the context of yanking the kcode block of my MCNP6.2 nuclear reactor simulation,
    I would use an if statement to check for the following string on every line...
    
    \"1neutron  activity in each cell {73 white spaces} print table 126\"
    
    and then I will kcode_block=kcode_block + line.

    while True: if I reach the kcode terminator which consists of:
    a whitespace, 131 dashes, a carriage return, and a line feed,
    break.
    
    Capturing things in MCNP isn't too easy because it's all formatted for teletype machines.
    Many of the terminators are just for the eyes and are not unique.
    We can still count and check for back-to-back LFs, which is something MCNP does a lot
    :)""")

#DON'T DO THIS the for loop is already stepping through lines!:
#    for line in pw3:
#         contents3 = contents3 + pw3.readline()
