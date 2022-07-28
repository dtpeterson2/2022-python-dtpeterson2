#!/usr/bin/env python3
##auth: Duncan Peterson

#What the heck is this?

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

yahooRHOST=socket.gethostbyname('yahoo.com')
print(yahooRHOST)    #Forward DNS lookup (A)

print(socket.gethostbyaddr(yahooRHOST)) #Reverse DNS lookup (PTR) similar to "host '72.30.35.10'""

print(socket.getservbyname('http'))  #Probably gives you 80. This is the listening port for http to communicate traditionally.
print(socket.getservbyport(80)) #80 is http. 443 is https listener

print('break \n')   #Split the console up.

#Here's how you might make a client
RHOST = socket.gethostbyname('ident.me')    #This is a place. It's an API for IP exposure. You'll get a simple IP.
RPORT = 80  #We hope the server is listening here.
SND_DATA = b"GET / HTTP/1.0\r\n\r\n"    #The socket communicates in bytes. You can't send anything else.
RCV_DATA = ""   #Init.

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #remote connection socket. use IPv4, TCP.
#C_SOCK sets up all the connection information. It has a namespace of things that let us do data transfer.
#This will crash if the connection is refused. Use try: except:

C_SOCK.connect((RHOST, RPORT)) #Tuple pair
#behind the scenes, connect() is doing the tcp handshake.

#After the server responds to our handshake, it should be safe to send data.
C_SOCK.send(SND_DATA)
#behind the scenes, send() is pushing the contents of SND_DATA to the server.
#If you're trying to send something else like text, you need it as bytes.
#Try something like C_SOCK.send(bytearray(SND_DATA,'utf8'))
#bytearray will take SND_DATA and treats it like utf8, and encodes it.

RCV_DATA = C_SOCK.recv(1024)    #the 1024 is the byte buffer for data. Hardware may require this to be a power of 2 that's smol, like 4096 bytes or less.
#This (should) catch any data the server sent back.

print(RCV_DATA.decode())    #Print the decoded byte data so we can see what we got.

C_SOCK.close()  #The responsible person closes their connection instead of letting it time out.
#close() handles the TCP terminate.