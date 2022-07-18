#!/usr/bin/env python3
##auth: Duncan Peterson

#Here, we will write things that do things so we never have to write them again.

#if you need to import things, you may need pip.
#sudo apt install python3-pip
#pip install rich (rich isn't needed for anything but this is how you install modules.)
#check pypi.org for available packages.

import keyword
from rich.console import Console    #If you can't resolve this, you don't have the rich module.
#Creating a console object. This is a place where we can draw stuff.
console = Console()

#Using the console object's internalized print function to print cool stuff.

console.print("Hello :smiley:", style="bold red")