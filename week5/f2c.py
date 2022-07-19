#!/usr/bin/env python3
##auth: Duncan Peterson

#Converts Fahrenheit to that temperature they use over in Europe and Canada.
import keyword
#Define your functions first.

def convert_temp(degrees_fahrenheit):    
    return float((float(degrees_fahrenheit)-32)*(5/9)) #input() gives strings. enforce a float on in and out.
#void main(). Hahahah C syntax
def main():
    result=convert_temp(32)
    print(result)
    return result   #This will run if you just run the script.

if __name__ == "__main__":  #If you want to run main() like other codes, you have to do check __name__. This doesn't run if you 'import'.
    main()