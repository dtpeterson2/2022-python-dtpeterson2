#!/usr/bin/env python3
##auth: Duncan Peterson
##Desc: I never imagined I'd be doing HTML and JSON stuff.

import keyword
import http.server,socketserver

Handler = http.server.SimpleHTTPRequestHandler #The handler is the response object
with socketserver.TCPServer(("",80),Handler) as httpd:  #"" as the address means localhost.
    httpd.serve_forever()  #This will fail because 80 is a privilaged port.

#This thing will host the files in the directory it is run. As you can imagine, this is dangerous. It needs sudo.