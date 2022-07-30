#!/usr/bin/env python3
##auth: Duncan Peterson

#This listens for stuff, and then sends it back, then goes back to listening.
#I don't fully understand what happens if we send or recieve things bigger than our buffers.
#We'll find out later I guess and hit the errors as they come.

import keyword
import socket

LHOST = ''  #Leaving this blank actually causes it to listen for everything that's available.

#We choose 5000 because it's not privilaged and probably not being used.
LPORT = 5000    #Port to listen on.
RCV_DATA = ""   #Init.

#Since we're listening, we're gonna say L_SOCK and not C_SOCK.
L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #remote connection socket. use IPv4, TCP.
L_SOCK.bind((LHOST, LPORT)) #tuple pair.
#L_SOCK.settimeout(3)    #3 seconds should be enough to get any amount of data or throw away a bad connection.
#listen will actually proceed and then .accept will hang until there's actually something there.
#Timeout will cause .accept to fail if there isn't anything.

while True: #Lets loop back when we're done.

    L_SOCK.listen(1)    #Now listening and accepting connections with a backlog of 1. This should wait until we get a connection.
    L_CONN, addr = L_SOCK.accept()  #accept() gives a tuple pair of (conn, address) of the incomming connection
    print('Incomming from:', addr) #Will report the connection address. This shouldn't obliterate the console because supposadly .listen will wait until we have something.
    #Now that we're connected, lets prepare to recieve data.

    while(1):   #Continue until there's no more data.
        RCV_DATA = L_CONN.recv(1024)    #get data in 1024 byte chunks max. The Canterbury Corpus is way larger than this. We'll see what happens.
        if not RCV_DATA: break  #If RCV_DATA is empty, the statement will be true and exit.
        print(f"Server recieved: {RCV_DATA.decode()}")    #echo the raw byte data.
        
        L_CONN.sendall(RCV_DATA)    #This echos the data back to the client. This sends until done and doesn't care about size.
        #It can't actually tell you if it was successful though.

    L_CONN.close()  #Shouldn't matter if there's no connection. Close if there is.
    print("Connection closed normally, we hope.")
