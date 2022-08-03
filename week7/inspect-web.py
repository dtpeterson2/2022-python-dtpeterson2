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
if response.ok:
    bsHTML= bs4.BeautifulSoup(response.text, features="html.parser")

    #Get the title of the page and each of the links.
    print(bsHTML.title.text)    #gets you the contents of the meta variable defined in <meta name="title" content="www.notpurple.com">

    for aLink in bsHTML.find_all('a'): #<a is a tag for links. each <a contains stuff like <a class="gb1" href="https://www.google.com/imghp?hl=en&amp;tab=wi">Images</a>
        print(f"Link: {aLink.getText()} , URL: {aLink.get('href')}") #This will get the href information which is a URL. The name is actualy outside of the attributes and you use getText to show it.

else:
    print(f"Error: {response.status_code}")