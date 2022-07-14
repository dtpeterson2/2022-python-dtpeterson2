#!/usr/bin/env python3
##auth: Duncan Peterson
#For a funny jurassic park reference but also the midterm.

#I feel like this is a better way of doing this. It compartmentalizes the commands within a good login.

import keyword
print("Name: Duncan Peterson")

#2.
password_database=dict({'Username' : 'dnedry' , 'Password' : 'please'}) #The magic word.

#3.
command_database=dict({'reboot': 'OK. I will reboot all park systems.',
                    'shutdown' : 'OK. I will shut down all park systems.',
                    'done' : 'I hate this hacker crap.'})

#4
white_rabbit_object=int(0)
counter=int(0)

while white_rabbit_object==0 and counter<3:
    input_user=input("Username:> ")
    input_password=input("Password:> ")
    counter+=1
    if input_user==password_database.get('Username') and input_password==password_database.get('Password'):
        print("Hi, Dennis. You're still the best hacker in Jurassic Park.")
        print(f"commands: {list(command_database.keys())}") #It formats nicer as a list.
        #while True:    #We don't need this. We're supposed to exit on a bad command, not ask again.
        command=input("> ")
        if command_database.get(command)==None: #This means the command wasn't found.
            print("The Lysine Contingency has been put into effect.")
            break
        else:
            print(command_database.get(command))
            break
        #break
    elif counter<3:
        print(f"You didn't say the magic word. {counter}")
    else:
        for i in range(1,26):
            print(f"YOU DIDN'T SAY THE MAGIC WORD!")
        break



