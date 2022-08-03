#!/usr/bin/env python3
##auth: Duncan Peterson
##Desc: Holy crap we're gonna be interacting with webpages with JSON!?

import keyword, argparse, json, requests
#use requests to demand HTML, but you don't get any hidden scripts like json. HTML is loaded with unnecessary format and not a lot of data.
#JSON has a lot more 'data' which is useful to python. The data is written in Java but the JSON module can translate null to None and true to True, etc.

#reqres.in is a good place to do front-end tests of your scripts.

#The first thing we want is a funny thingy that can take a '--ipaddress'
#
#parser = argparse.ArgumentParser(description='Parser handles the ip address to test.')
#
#parser.add_argument('-i', '--ipaddress', metavar='IP Address', dest='ipTry', type=str, required=True, help='Target IPv4 to test. If the address is not valid, no error will be given but nothing will be found.')
#parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')    #Change version so you can help others know the ver of your script.
#
#theArgs=parser.parse_args()  #theArgs is gonna get attribute names corresponding to the parser arguments
#

response=requests.get("https://reqres.in/api/users/2")  #This is raw text.
if response.ok:
    print(type(response))   #models.Response object.
    print(f"Status Code; {response.status_code}")   #100 info. 200 is success (204 is no content). 300 is redirects. 400 is client errors. 500 server errors
    print(f"text: {response.text[:64]}")
else:
    print(f"Error: {response.status_code}")
    quit

print("")   #break
json_dict=json.loads(response.text)    #Converts the raw JSON string to a Dict.
print(type(json_dict))  #Believe it or not, it's a dictionary.
for key,value in json_dict.items(): #There are dicts within dicts! The fabled nested dictionary!
        print(f"{key} : {value}")
print("")   #break
print(json.dumps(json_dict,indent=4))    #.dumps is a print function that puts the data to the screen formatted in a special way that makes it easy to read. It is just a dict but .dumps is special.
    #indent=4 makes horizontal tabs 4 spaces so it's formatted the way python is when you code.
    #JSON is nested dictionaries, so the indentation lets you see how they seperate.

#You don't have to type-check the values for more nested dicts. json.dumps makes this easy. Lets print out just the data section.
print("")
print("\"data\" section")
print(json.dumps(json_dict["data"]["id"],indent=4))   #If it looks like we're just picking the data key out and printing its value, it's because we are.
#YES YOU CAN GIVE DOUBLE INDICIES (As long as you're calling a dict key!)!

#For looking for things in nested dicts, you need to do this.

for key in json_dict:
    print(f"Key name: {key}")
    for subkey in json_dict[key]:
        print(f'subkey: {subkey} , has value of: {json_dict[key][subkey]}')

#url=f"https://"

#How do URL's work?
#Scheme: HTTPS, ftp, or mailto (rare?)
#Subdomain: addresses or domain. For example, madison.k12.wi.us- madison is the subdomain.
#Second level: k12
#Top level: .com, .us, .org, etc. The entity registration.
#subdirectory; anything after the domain. yuja.com/V/Video, google.com/documents/d/ etc...

#Params: anything after a ? is a parameter: youtube.com/watch?(The address of the video)