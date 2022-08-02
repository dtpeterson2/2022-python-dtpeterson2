#!/usr/bin/env python3
##auth: Duncan Peterson
##Desc: Holy crap we're gonna be interacting with webpages!?

import keyword
import requests #You use this to demand things from a website using get()

response=requests.get("https://notpurple.com", None)  #This will get the raw HTML.
#Inspect
if response.ok:
    print(type(response))   #probably a models.Response object.
    print(f"Status Code; {response.status_code}")   #100 info. 200 is success (204 is no content). 300 is redirects. 400 is client errors. 500 server errors
    print(f"text: {response.text[:256]}")   #[:256] Slice to show the first 64
else:
    print(f"Error: {response.status_code}")

HTMLsave = open('my_web-file.html', 'w')
HTMLsave.write(response.text)
HTMLsave.close()

#Wow. notpurple.com isn't much to look at, but it did work- I'll give it that.