#!/usr/bin/env python3
##auth: Duncan Peterson
##Desc: I never imagined I'd be doing HTML and JSON stuff.

#pip install requests if you don't already have it.
# Try w3schools.com/html for help

import requests #You use this to demand things from a website using get()
import keyword


#get() has some parameters. The URL (obvious)
#params (dict of GET params to send with the request)
#myParams={"firstname":"timmy"}
#headers (dict of HTTP headers to send with the request) (Maybe a someone who's more familiar with web design knows what this means.)
myHeaders={"content-type":"text"}
#cookies (CookieJar object to send with the req)
#auth (AuthObject for basic HTTP Auth if required)
#timeout (For if the server is taking its sweet time.)

response=requests.get("http://google.com", headers=myHeaders)  #This will get the raw HTML.
#Inspect
if response.ok:
        
    print(type(response))   #probably a models.Response object.
    print(f"Status Code; {response.status_code}")   #100 info. 200 is success (204 is no content). 300 is redirects. 400 is client errors. 500 server errors
    print(f"Headers: {response.headers}")   #Headers are actually a dict and python can store them as such.
    print("")   #Break
    responseHeaders=dict(response.headers.items())
    print(type(responseHeaders))    #It's a 'collections.abc.itemsview' if you don't dict() the assignment.
    for key,value in responseHeaders.items():
        print(f"{key} : {value}")   #These keys are storing very valuable information you can search the dict for.
    print("")   #Break
    print(f"text: {response.text[:256]}")   #Slice to show the first 256
else:
    print(f"Error: {response.status_code}")

#400 replys from the website are not actually errors. You need to do if else. like we have here.
#Or... We can do this.
#try:
#   response.raise-for_status
#except Exception as exc:
#   print(f"There was an error {exc}")  #This is basically treating anything other than a good reply as an exception

"""
import http.server
import socketserver

Handle = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",80), Handler) as httpd
    httpd.serve_forever()   #You can make a simple html server that can provide directory access.

#python3 -m http.server listens on 8000 for safety. Might need sudo.
"""