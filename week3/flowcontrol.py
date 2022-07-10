#!/usr/bin/env python3
##auth: Duncan Peterson
##Flow control is about if else statements. This is a showcase for that.

#Your silly dungeon game should have at least 3 doors.
#If this was BASIC, I'd use JMP and labels, but Python can't do that.
#Perhaps python isn't ideal for branched RPGs.

import keyword
items=[]

#Lets show off some input sanitization.
while True: #This lets us run the dungeon again.
    print("""You enter a dark room with three doors. 
Do you go through door #1 #2, or #3?""")
    while True:
        try:
            while True:
                door = int(input("-> "))
                if (1 <= door and door <= 3):    #If input valid
                    #We can't use 'door in range()' sadly.
                    break
                else:
                    print("Please enter a valid integer. There's no turning back, Muahaha!")
            break
        except ValueError:
            print("Bad Type. Please answer with an integer.")
    door=str(door)
    print("Using invalid inputs can cause strange things can happen")
    print("\n") #break

    # == Door Number 1 logic =======================
    if door == "1":

        print("There's a koala pouting on the ground in the middle of the room")
        print("What do you do?\n")

        print("1. Nothing")
        print("2. Leave")

        # == Bear logic ============================
        koala = input("-> ")

        if koala == "1":
            print("1) The koala crawls up your leg to get to a higher place.")
            items.append("koala")  #He's yours now.
        elif koala == "2":
            print("2) You leave the poor cuddly clawed critter to their fate.")
        else:
            print(f"By violating our trust on making valid input, you lose your items.")
            items=[]

    # == Door Number 2 Logic =====================
    elif door == "2":
        print("You stare into the endless abyss of an infinite loop fault.\n\
            The void reaches out and asks what you want.")
        
        print("1. Knowledge")
        print("2. Cheesecake")
        print("3. Soft toys")

        # == Void Logic======================
        infloop = input("-> ")

        if infloop == "1":
            print("1) The void tells you to try all the doors to get the best ending")
        elif infloop == "2":
            print("2) The void tells you there is no cake. It was replaced with a cuddly creature.")
        elif infloop == "3":
            print("3) The void tells you to take door #3 next time around.")
        else:
            print("N) By trying the patience of the void, your journey abruptly ends")
            break

    
    # == Door Number 3 Logic =====================
    elif door == "3":

        print("The room is dark as you enter. As the door locks behind you,\nyou are surrounded\
 by large plush sharks. A glance examination reveals they are Blåhaj, and are sold by IKEA.")
        print("What do you do?\n")

        print("1. Take one")
        print("2. Leave")

        # == Blåhaj logic ============================
        blahaj = input("-> ")

        if blahaj == "1":
            print("1) You take the oversized soft toy with you. It gives you a unique comfort and sense of community.")
            items.append("blahaj")  #He's yours now.
        elif blahaj == "2":
            print("2) You need no unique comforts and leave the school of fish alone.")
        else:
            print(f"There is no third option. The void commands a Blåhaj to follow you against your will.")
            items.append("blahaj")  #Whether you want it or not.

    print("\n") #break
    print("Two portals in front of you. One is labled 'Exit', the other is 'Restart' Exit?")
    norestart = input("(y/n)->")
    if norestart.lower() == "y":
        break
print("\n") #break
print("Your journey ends.")
#koalatotal=sum(1 for i in items if i=="koala")
#blahajtotal=sum(1 for i in items if i=="blahaj")
if items.count('koala') ==0 and items.count('blahaj') == 0:
    print("You carry with you nothing.")
elif items.count('koala')>=1 and items.count('blahaj') == 0:
    print("A very happy koala clings to your side, vibrating with warmth as you depart.")
elif items.count('koala')==0 and items.count('blahaj') >= 1:
    print("With a Blahaj to keep you company in bed, you will never be alone.")
elif items.count('koala')>=1 and items.count('blahaj') >= 1:
    print("You certainly have plenty of friends to keep you company, both animate and inaimate but equally cuddly.\
        \n You a total of...")
    print(f"{items.count('blahaj')} Blahaj toy"+ ("s" if items.count('blahaj') >= 1 else ""))
    print(f"{items.count('koala')} Clingy koala"+ ("s" if items.count('koala') >= 1 else ""))  #Wowzah. Trailing if statement!

"""
else:
    print("Through usage of black magic or existance of poor input\
        \nvalidation, your journey ends before it begins")
"""
