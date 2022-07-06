#A demonstration of reading text files.
from sys import argv

#By writing script, we are propmting for input
script, filename = argv
txt=open(filename)  #At a DEDENT, the file will close if you used 'with'.
#open(file,mode) the second arg can do special things like 'r', read only for text.
#'r+' is read and write text. 'rb' is read the binary. 'a' for append. Adds a new line to the EOF.
#'w' for writing text. This will make a new file if it doesn't exist
#.close() to terminate and remove from memory
print(f"The target file is: {filename}\nDUMP FOLLOWS.")
print(txt.read())   #read the contents of the target. .read(5) reads the first 5 characters
print(type(txt))    #As you will see, the txt is a funny thing because this object represents the file.
content = txt.read(5)
print(type(content))    #This will be a string, once we actually read the txt and assign it.
content5 = txt.read(5)  #This will read characters 6-10. Read actually incriments when you do things like read(5)
print(content)
print(content5)
#These are going to be null because txt.read() went all the way to EOF
txt.seek(0,0)   #Returns the read to the starting point
content = txt.read(5)
content5 = txt.read(5)
print(content)
print(content5)
print(txt.tell())   #Where are we?
txt.seek(0,0)
contentList=txt.readlines() #Reads the whole thing. Each LF gets translated as \n and delimits.
print(contentList)