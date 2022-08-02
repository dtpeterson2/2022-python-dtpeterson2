#!/usr/bin/env python3
##auth: Duncan Peterson
##Desc: Holy crap we're gonna be interacting with webpages!?

import keyword
import requests, bs4 #You use this to demand things from a website using get()
#pip install beautifulsoup4

#links look like <li> <a href="stuff">name</a></li> so scan the website for those lines. You think you can just write your own parser
# but you'd find out that HTML can be formated a myriad of different ways and still be valid. It may even be obfuscated.
#This is why we're not going to write our own parser and instead use BeautifulSoup.

response=requests.get("https://notpurple.com", None)  #This will get the raw HTML.
response.raise_for_status() #This creates an HTTPError object if something went wrong. You probably don't have to do this but you certainly can.
if response.ok:
    bsHTML= bs4.BeautifulSoup(response.text, features="html.parser")
    print(type)
    print('pepe')
else:
    print(f"Error: {response.status_code}")