#!/usr/bin/env python3
##auth: Duncan Peterson
##Desc: Use the ipinfo API to get JSON information about any host.

import keyword, argparse, json, requests

#The first thing we want is a funny thingy that can take a '--ipaddress'

parser = argparse.ArgumentParser(description='Parser handles the ip address to test.')

parser.add_argument('-i', '--ipaddress', metavar='IP Address', dest='ipTry', type=str, required=True, help='Target IPv4 to test. Status Code may inform what happened.')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')    #Change version so you can help others know the ver of your script.

theArgs=parser.parse_args()  #theArgs is gonna get attribute names corresponding to the parser arguments

#Get the data.
requestdata=requests.get(f"https://ipinfo.io/{theArgs.ipTry}/json")    #Get

if requestdata.ok:
    print(f"Status Code; {requestdata.status_code}")   #100 info. 200 is success (204 is no content). 300 is redirects. 400 is client errors. 500 server errors
    print("")   #Visual break.
    myDict=json.loads(requestdata.text)    #Converts the raw JSON string to a Dict.

    print("Keys,    Values")
    print("<BOF>\n{")
    for key,value in myDict.items(): #There might be dicts within dicts, but we're not going to care about that too much.
        print(f"{key},    {value}")
    print("}\n<EOF>")
else:
    print(f"Error: {requestdata.status_code}")
    quit    #Terminate the whole thing.