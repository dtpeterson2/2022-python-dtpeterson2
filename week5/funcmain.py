#!/usr/bin/env python3
##auth: Duncan Peterson

#Here, we will write things that do things so we never have to write them again.

import keyword
None    #void main(). Hahahah C syntax
def main():
    print("__name__")
    print("toot. You just ran main.")
    return None

if __name__ == "__main__":  #This is an awful thing Python does where, if you call the script directly, the code that runs is main(). This doesn't run if you 'import'. You have to write it this way.
    main()