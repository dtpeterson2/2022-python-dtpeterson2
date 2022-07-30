#!/usr/bin/env python3
##auth: Duncan Peterson

#This gets a file, connects, and sends it over.
#I don't fully understand what happens if we send or recieve things bigger than our buffers.
#We'll find out later I guess and hit the errors as they come.

import keyword
import socket

#Target information
RHOST = '127.0.0.1' #loop back to ourself.
RPORT = 5000

C_SOCK=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #remote connection socket. use IPv4, TCP.
#C_SOCK.settimeout(3)    #3 seconds should be enough to get any amount of data.

FileTarget = open('asyoulik.txt' , 'r')
content=FileTarget.read()   #Read the whole thing.

SND_DATA=content.encode()   #It needs to be bytes.
RCV_DATA = ""   #init.
C_SOCK.settimeout(3)    #3 seconds should be enough to get any reasonable amoutn of data.

try: 
    C_SOCK.connect((RHOST, RPORT)) #Tuple pair. The connection will refuse if nobody is around to listen.
    #behind the scenes, connect() is doing the tcp handshake.
    print("Connection Successful.") #.connect will fail if it didn't

    C_SOCK.sendall(SND_DATA)    #This will make sure everything gets there no matter how long it takes.

    #while True:
    #    RCV_DATA = C_SOCK.recv(1024)    #Get something back if anything.
    #    if not RCV_DATA: break
    #    print(RCV_DATA.decode())    #Print what the server gave us if anything.
    #For whatever reason, this hangs up the program.

    C_SOCK.close()
    print("Connection closed: Done")

except socket.error as e:
    print(f"Connection failed: {e}")
