#!/usr/bin/env python3
##auth: Duncan Peterson
#For a funny jurassic park reference but also the midterm.

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
        white_rabbit_object=1   #This will cause termination of the loop.
    elif counter<3:
        print(f"You didn't say the magic word. {counter}")
    else:
        for i in range(1,26):
            print(f"YOU DIDN'T SAY THE MAGIC WORD!")
        #break  #We're supposed to let the white_rabbit_object do that.

if white_rabbit_object==1:  #Fail if we didn't log in. I feel like it's better to put this within the while.
    print(f"commands: {list(command_database.keys())}") #It formats nicer as a list.
        #while True:    #We don't need this. We're supposed to exit on a bad command, not ask again.
    command=input("> ")
    if command_database.get(command)==None: #This means the command wasn't found.
        print("The Lysine Contingency has been put into effect.")
    else:
        print(command_database.get(command))



