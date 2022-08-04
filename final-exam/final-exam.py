#!/usr/bin/env python3
##auth: Duncan Peterson
authname="Duncan Peterson"
##I'm a bit sad that it's over with already...

#IMPORT EVERYTHIIING!!!
import keyword, argparse, requests, bs4, json, socket
from sys import argv

#Sometimes coding is about copy-pasting a thing you wrote that you know works, and not re-pioneering the same thing.

parser = argparse.ArgumentParser(description='Parser handles the args. Imagine that.')

parser.add_argument('-i', '--ipaddress', metavar='IP Address', dest='ipTry', type=str, required=True, help='<REQUIRED> IP address to try.')
parser.add_argument('-q', '--question', metavar='Question Number', dest='question', type=int, required=True, choices=range(1,6), help='<REQUIRED> Valids are 1-5. Flow control argument for question selection.')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')    #Change version so you can help others know the ver of your script.

argparsed=parser.parse_args()  #args have been parsed.

tryURL=f"http://{argparsed.ipTry}/q{argparsed.question}"

print(f"Name: {authname}")
print(tryURL)

#Question 1 function:
def get_response(URL):
    response=requests.get(URL)
    print(f"Server reply: {response.text}") #.text is just a string. it's not a function. Don't call it.
    return None

#Question 2. You're gonna need beautiful soup for this one. Import bs4
#We want the <h2> element so I'm guessing we want to use the HTML parser.
#You're supposed to extract the secret message from the h2 element!
def parse_string(URL):
    response=requests.get(URL)
    bsHTML= bs4.BeautifulSoup(response.text, features="html.parser")
    #print(bsHTML)
    h2 = bsHTML.find("h2")    #This should get the element with <h2. You can't getText() unless you're doing a findall
    #print(type(h2)) #It's a bs2.element.Tag. You can't slice this yet.
    #str(). Will do it in a raw, unclean way.
    #h2.text #This will give us the clean text

    print(f"ANSWER: {h2.text[7:-5:3]} <{authname}>")    #It looks like 'Found it!' is every 3 characters and starts on the 8th, but the 1st is actually 0 in the index.
    return

#Question 3. We want to do a request.get and find the header and return it.
def parse_header(URL):
    response=requests.get(URL)
    print(f"ANSWER: {response.headers['FINAL-HEADER']}")   #Headers are actually a dict and python stores them as such! So lets call it like a dict!
    #Nailed it!
    return

#Question 4. Use the json module
def parse_json(URL):
    response=requests.get(URL)
    json_dict=json.loads(response.text)    #Converts the raw JSON string to a Dict that we can search.
    #There are dicts within dicts! The fabled nested dictionary! The only good way to pluck things is

    for i in json_dict['Music And Books']:  #the dict has one key and one value. The key is Music And Books and the value is a list of dicts 
        #We can't pluck indexes. We have to search for which one has the correct title and go from there.

        #'i' is a dict of length 3. We want the one that has 'title' : 'The Shining'
        if i['title']=='The Shining':
            print(f"ANSWER: {i['publish_info']['publish_year']}")
            break   #We found it. Stop checking for more.

    return

#Question 5. We're going to use sockets to ask a server something. import sockets.
def socket_client(URL):

        #Target information
    RHOST = URL
    
    #The port can be anything from 5000 to 7000. We need to try every one.
    msg="secret"
    SND_DATA=msg.encode()   #It needs to be bytes.

    RCV_DATA = ""   #init.
    goodport = None #init
    for RPORT in range(5000,7001):
        try:
            C_SOCK=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #remote connection socket. use IPv4, TCP.
            C_SOCK.connect((RHOST, RPORT)) #Tuple pair. The connection will refuse if nobody is around to listen.

            print(f"Connection Successful on {RPORT}") #.connect will fail if it didn't

            C_SOCK.sendall(SND_DATA)    #This will make sure everything gets there no matter how long it takes.
            goodport=RPORT  #Save the port if we succeeded.
            
            RCV_DATA = C_SOCK.recv(1024)    #Get something back if anything. 1024 bytes should be enough.
            C_SOCK.close()

            break   #We succeeded. Break. There's no need to keep trying.
        
        #For whatever reason, this hangs up the program.

        except socket.error as e:
            #print(f"{RPORT} is bad.")
            C_SOCK.close()  #Silently error and try the next port.
    
    if goodport==None:
        return  #We don't want to try to .decode on RCV_DATA if nothing was got, because RCV_DATA won't have the .decode attribute.
    else:
        return  print(f"ANSWER: {RCV_DATA}\nPort: {goodport}")
        

#Lets parse the -q argument. We have to do this at the end AFTER the functions get defined.
if argparsed.question==1:
    get_response(tryURL)

elif argparsed.question==2:
    parse_string(tryURL)

elif argparsed.question==3:
    parse_header(tryURL)

elif argparsed.question==4:
    parse_json(tryURL)

elif argparsed.question==5:
    socket_client(tryURL)

else:
    print(f"Somehow, you managed to get around the argparser. How dare you")
    quit