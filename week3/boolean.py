#!/usr/bin/env python3
##auth: Duncan Peterson
##Desc: This script does boolean stuff. My favorite. I loved discrete mathematics and FPGAs

import keyword #this is important now more than ever


print("1. True and True")
result=True and True
print(f"Result: {result}")
print("\n") #break

print("2. False and True")
result=False and True
print(f"Result: {result}")
print("\n") #break

print("3. 1==1 and 2==2)")
result=bool(1==1 and 2==1)  #False because the second test will fail
print(f"Result: {result}")
print("\n") #break

print("4. 0")
result=bool(0)    #Should be False. 0 is the only int that will return false
print(f"Result: {result}")
print("\n") #break

print("5. \"\" ")
result=bool("")   #Should be False, since this is the empty string. It's the only string that will return false.
print(f"Result: {result}")
print("\n") #break

print("6. 0.0")
result=bool(0.0)    #Only the zero float will return false.
print(f"Result: {result}")
print("\n") #break

print("7. not 0")   #Should be True, since 0 is false.
result=bool(not 0)
print(f"Result: {result}")
print("\n") #break

print("8. 'test'=='test'")
result=bool('test' == 'test')   #Should succeed. The strings are equal on a byte level.
print(f"Result: {result}")
print("\n") #break

print("9. 1==1 or 2!=1")
result=bool(1==1 or 2!=1)   #Should succeed because 1==1 and only one argument needs to pass. != is shorthand for not equal
print(f"Result: {result}")
print("\n") #break

print("10. True and 1==1")
result=bool(True and 1==1)
print(f"Result: {result}")
print("\n") #break

print("11. False and 0!=0") #False and False is still false. The statements need to be True. Otherwise you want a NOR (Neither)
result=bool(False and 0!=0)
print(f"Result: {result}")
print("\n") #break

print("12. True or 1==1")
result=bool(True or 1==1)
print(f"Result: {result}")
print("\n") #break

print("13. 'test' == 'testing'")
result=bool('test' == 'testing')    #The bytes aren't equal.
print(f"Result: {result}")
print("\n") #break

print("14. 1!=0 and 2==1")
result=bool(1!=0 and 2==1)    #And requires both.
print(f"Result: {result}")
print("\n") #break

print("15. 'test'!='testing'")
result=bool('test'!='testing')
print(f"Result: {result}")
print("\n") #break

print("16. 'test'==1")
result=bool('test'==1)  #Apparently, if you compare different data types, you'll get false.
print(f"Result: {result}")
print("\n") #break

print("17. 1==1 and not ('testing'==1 or 1==0)")
result=bool(1==1 and not ('testing'==1 or 1==0))
print(f"Result: {result}")
print("\n") #break

print("18. 'chunky' == 'bacon' and not (3==4 or 3==3)") #False and not True is false.
result=bool('chunky' == 'bacon' and not (3==4 or 3==3))
print(f"Result: {result}")
print("\n") #break

print("19. 3==3 and not ('testing' == 'testing' or 'Python' == 'Fun')")
result=bool(3==3 and not ('testing' == 'testing' or 'Python' == 'Fun'))
print(f"Result: {result}")
print("\n") #break'chunky' == 'bacon' and not (3==4 or 3==3)