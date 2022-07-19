#!/usr/bin/env python3
##auth: Duncan Peterson

#Converts temperature and makes usage of other scripts to do it.

import keyword
import f2c
#Define your functions first.


temp=input("Give F to convert> ")

tempc=f2c.convert_temp(temp)    #Do the thing.

print(f"{tempc:<.1f} Degrees Celsius")  #Float math makes huge decimals. Round it for readibility.