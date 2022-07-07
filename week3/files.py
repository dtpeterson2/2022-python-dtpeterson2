#!/usr/bin/python3
##auth: Duncan Peterson
##Desc: This script showcases file read python capabilities
#It also tests some things as practice for myself.
import keyword

print("\n") #break

#1. Open passwd and read only and save it all to a string

with open("/etc/passwd","r") as pw1:
    #pw1 represents the file. we can't do much with it yet.
    contents1 = pw1.read()
    print(f"#File char length: {len(contents1)}")
    print("passwd now read as contents1. We can control contents1 however we please,\
        \n and write to a file later")
    #This saved contents1 as the whole thing. We can close and do anything we want.
    #DON'T DO THIS: print(contents1)
    #del contents1
    pw1.close()

print("\n") #break

#2. Open passwd and save it to a list.
with open("/etc/passwd","r") as pw2:
    contents2 = pw2.readlines()
    print(f"File row length: {len(contents2)}.")
    print("passwd now read as contents2. We can control contents1 however we please,\
        \n and write to a file later. \n \
        It's perhaps easier to navigate large files by line, but we may lose \n \
        sense of relationship between columns doing it this way.")
    pw2.close()

#3. Open passwd and save it to a variable line by line.

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
