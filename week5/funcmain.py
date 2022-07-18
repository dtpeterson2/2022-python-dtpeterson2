#!/usr/bin/env python3
##auth: Duncan Peterson

#Here, we will write things that do things so we never have to write them again.

import keyword
None    #void main(). Hahahah C syntax
def main():
    print(__name__)
    print("argh")
    print("Ran main()")
#    print(args)
    print("Done")
    return int(1)

def create_tea(user_id,domain="teapot.edu"):    #You can't write 'user'. That's a special name.
    return user_id + "@" + domain

print("Funcmain line 18 got ran")   #A thingy to tell us that line 18 got executed.

if __name__ == "__main__":  #This is an awful thing Python does where, if you call the script directly by name, the code that runs is main(). This doesn't run if you 'import'. You have to write it this way.
    main()