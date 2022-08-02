#!/usr/bin/env python3
##auth: Duncan Peterson
##Desc: Holy crap we're gonna be interacting with webpages!?

import keyword
import requests, bs4 #You use this to demand things from a website using get()
#pip install beautifulsoup4

#links look like <li> <a href="stuff">name</a></li> so scan the website for those lines. You think you can just write your own parser
# but you'd find out that HTML can be formated a myriad of different ways and still be valid. It may even be obfuscated.
#This is why we're not going to write our own parser and instead use BeautifulSoup.

response=requests.get("https://www.google.com", None)  #This will get the raw HTML.
response.raise_for_status() #This creates an HTTPError object if something went wrong. You probably don't have to do this but you certainly can.
if response.ok:
    bsHTML= bs4.BeautifulSoup(response.text, features="html.parser")
    #Check beautiful-soup-4.readthedocs.io/en for more information
    print(type(bsHTML)) #It's a beautifulsoup bs4 object.
    print(bsHTML.title.text)    #gets you the contents of the meta variable defined in <meta name="title" content="www.notpurple.com">
    #not doing .text will give you the tags themselves!
    images = bsHTML.select('img')   #This gives you anything in <img > if any. In the case of notpurple, there are none.
    print(images[0]['src']) #Everything with <img is followed by src="some sort of picture.png"
    links = bsHTML.select("a")    #To get the href of a link tag <a>
    for a in bsHTML.find_all('a'): #<a is a tag for links. each <a contains stuff like <a class="gb1" href="https://www.google.com/imghp?hl=en&amp;tab=wi">Images</a>
        print(f"{a.get('href')} : {a.getText()}") #This will get the href information which is a URL. The name is actualy outside of the attributes and you use getText to show it.
else:
    print(f"Error: {response.status_code}")