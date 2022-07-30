#!/usr/bin/env python3
##auth: Duncan Peterson

#What the heck is this? Client version.

import keyword
import socket   #I'm not part of the ITPROG. I'm an engineer. I'm going to do my best though.

#Reference table.
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

RHOST = '127.0.0.1' #loop back to ourself.
RPORT = 5000 #so it works with echosockets which is listening on 5000

SND_DATA = b"This data came from clientsockets.py behold my power"
RCV_DATA = ""   #init.

C_SOCK=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #remote connection socket. use IPv4, TCP.
#C_SOCK sets up all the connection information. It has a namespace of things that let us do data transfer.

try: 
    C_SOCK.connect((RHOST, RPORT)) #Tuple pair. The connection will refuse if nobody is around to listen.
    #behind the scenes, connect() is doing the tcp handshake.
    print("Connection Successful.") #.connect will fail if it didn't

    C_SOCK.send(SND_DATA)

    RCV_DATA = C_SOCK.recv(1024)    #You actually need a while loop to recieve the other chunks.
    print(RCV_DATA.decode())    #Print what the server gave us

    C_SOCK.close()

except socket.error as e:
    print(f"Connection failed: {e}")

