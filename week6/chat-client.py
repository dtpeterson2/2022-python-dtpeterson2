#!/usr/bin/env python3
##auth: Duncan Peterson

#This gets some text, and then connects and sends, then asks again.
#I don't fully understand what happens if we send or recieve things bigger than our buffers.
#We'll find out later I guess and hit the errors as they come.

import keyword
import socket

#Target information
RHOST = '127.0.0.1' #loop back to ourself.
RPORT = 5000

C_SOCK=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #remote connection socket. use IPv4, TCP.
C_SOCK.settimeout(3)    #3 seconds should be enough to get any amount of data.


while True:
    msg=input("Give any message. 'exit' will terminate case-sensitively.: ")
    if msg=="exit":
        break

    #Data
    SND_DATA = msg.encode('utf-8')
    RCV_DATA = ""   #init.
    #print(f"Message length: {len(SND_DATA)} bytes.")

    C_SOCK=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #remote connection socket. use IPv4, TCP.

    #initiate the connection.
    try: 
        C_SOCK.connect((RHOST, RPORT)) #Tuple pair. The connection will refuse if nobody is around to listen.
        #behind the scenes, connect() is doing the tcp handshake.

        C_SOCK.send(SND_DATA)

        #while True: #Lets do this in case the server has more to say.
        #    RCV_DATA = C_SOCK.recv(1024)    #You actually need a while loop to recieve the other chunks.
        #    if not RCV_DATA: 
        #        break
        #    else:
        #        print(RCV_DATA)
        #    #print(RCV_DATA.decode())    #Print what the server gave us

        #.recv will hang and wait for more data until it gets some. Don't loop it.

        RCV_DATA = C_SOCK.recv(1024)
        print(f"Server Response: {RCV_DATA.decode()}")    #Print what the server gave us

        C_SOCK.close()

    except socket.error as e:
        print(f"Connection failed: {e}")
        break

    #We just closed the connection. We can still reconnect. This will return to the top.


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