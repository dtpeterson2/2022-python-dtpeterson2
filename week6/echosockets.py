#!/usr/bin/env python3
##auth: Duncan Peterson

#What the heck is this? (Receiver version)

import keyword
import socket   #I'm not part of the ITPROG. I'm an engineer. I'm going to do my best though.

"""
RHOST / RPORT - Remote address and port
RPORTS - list or Tuple of ports to try.
LHOST - Localhost? The address you accept connections from.
LPORT - The listening port
SND_DATA - Store the data to send to RHOST and RPORT
RCV_DATA - Store recieve on L.
C_SOCK - Socket object to connect to remote
L_SOCK - Socket object for listening
L_CONN - Connection object use to interact to a connected client.

socket.AF_INET6 because IPv4 will be obsolete (eventually)
TCP, socket.SOCK_STREAM connect until terminated
UDP, socket.SOCK_DGRAM send a single datagram, get a reply, connection terminates automatically.

UDP won't inform the sender if a packet gets lost. and datagrams are limited in size.
The 8 byte UDP header and 60 byte IPv4 header means a maximum packet size of 508 bytes. The reassembly buffer is 576 byte.
TCP doesn't have these restrictions but waits for packets to reach the destination before sending more.
"""
LHOST = ''  #Leaving this blank actually causes it to listen for everything that's available.

#We choose 5000 because it's not privilaged and probably not being used.
LPORT = 5000    #Port to listen on.
RCV_DATA = ""   #Init.

#Since we're listening, we're gonna say L_SOCK and not C_SOCK.
L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #remote connection socket. use IPv4, TCP.
#This sets up all the connection information. It has a namespace of things that let us do data transfer.
L_SOCK.bind((LHOST, LPORT)) #tuple pair.

while(1):   #infinite loop until we recieve.
    L_SOCK.listen(1)    #Now listening and accepting connections with a backlog of 1
    L_CONN, addr = L_SOCK.accept()  #accept() gives a tuple pair of (conn, address) of the incomming connection
    print('Connected by', addr) #Will report the connection address
    while(1):   #infinite loop will continue until break
        RCV_DATA = L_CONN.recv(1024)    #get data in 1024 byte chunks max
        if not RCV_DATA: break  #If RCV_DATA is empty, the statement will be true and exit. We'll wait for more connections.
        print(f"Server recieved:{RCV_DATA}")    #echo the raw byte data.

        L_CONN.sendall(RCV_DATA)    #This echos the data back to the client

    L_CONN.close()  #Shouldn't matter if there's no connection. Close if there is.
