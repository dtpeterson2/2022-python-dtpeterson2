#!/usr/bin/env python3
##auth: Duncan Peterson
#For dictionaries and stuff
import keyword

FQDNdict={"server1.testlab.com" : "192.168.1.10",
        "server2.testlab.com" : "192.168.1.11",
        "server3.testlab.com" : "192.168.1.12",
        "server4.testlab.com" : "192.168.1.13",
        "server5.testlab.com" : "192.168.1.14",
        "server6.testlab.com" : "192.168.1.15"
        }   #Here is the thing.

print("2. List all the FQDNs in this dict")
print("All stored FQDNs follow.")
for FQDN in FQDNdict:
    print(f"{FQDN}")    #We can do .keys(), but this looks better in the console.
print() #break

print("#3. List all the IPs in the dict.")
print("All stored IPs follow.")
#for FQDN, IP in FQDNdict:   #You can't do this. You have to give only ONE thing to incriment. Too many values to unpack
for FQDN, IP in list(FQDNdict.items()): #You're gonna get pairs back in the form of a list.
    print(f"{IP}")  #Pick the second ordinal and print that one.
print() #break

print("#4. List all records as key/value pairs")
print("All records follow.")
for FQDN, IP in list(FQDNdict.items()):  #list() is gonna treat each entry as an element. .items() is going to return all tuple pairs. FQDN and IP are going to index them.
    print(f"{FQDN} has {IP}")
print("End record.")
print() #break

print("#5. Add server 7 and 8 to the list and continue the sequence.")
#FQDNdict += {"server7.testlab.com" : "192.168.1.16"} + {"server8.testlab.com" : "192.168.1.17"} #That operand isn't supported for dicts.
#FQDNdict.update({"server7.testlab.com" : "192.168.1.16"},{"server8.testlab.com" : "192.168.1.17"}) #Update only allows one item at a time.
#In the future, instead of hardcoding this, we can seperate all the bytes as a list, incriment the last byte, and then recompile it back into an IP.

FQDNdict["server7.testlab.com"] = "192.168.1.16"    #Dicts are like lists. Use [] and treat it like one.
FQDNdict["server8.testlab.com"] = "192.168.1.17"    #If it doesn't exist, it gets made. Easy!
print("2 entries added")
#lets prove it exists.
tryme=list({"server7.testlab.com","server8.testlab.com"})
for FQDN in tryme: #(key, value) is the tuples stored within. Items returns the whole tuple.
    try:
        print(f"{FQDN} was found and has value: {FQDNdict[FQDN]}") #KeyError if the key doesn't exist. None means it's still found, and we want to know.
    except KeyError:
        print(f"{FQDN} does not exist.")
        #The reason I used try and except is because .get() doesn't make a distinction between not finding the key and the value being None.
print() #break

print("#6, #7, test if server2 and server10 are contained")
tryme=list({"server2.testlab.com","server10.testlab.com"})
#for FQDN in tryme:
#    print(f"Checked for {FQDN}. {FQDNdict.get(FQDN)} found.")   #This returns 'None' if get() didn't find our key in particular. But what if value=None?
#.get() doesn't make a distinction! Lets try somthing else.

for FQDN in tryme: #(key, value) is the tuples stored within. Items returns the whole tuple.
    try:
        print(f"{FQDN} was found and has value: {FQDNdict[FQDN]}") #KeyError if the key doesn't exist. None means it's still found, and we want to know.
    except KeyError:
        print(f"{FQDN} does not exist.")
print("\n")   #break
#The reason I used try and except is because .get() doesn't make a distinction between not finding the key and the value being None.