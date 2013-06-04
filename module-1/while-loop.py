#!/usr/bin/python
#
#Module 1 - Part 4
#Exercise: demo of a while loop with an else statement
#Mark Osborn - 20-March-2013
#

nStrawberries = 1

while nStrawberries > 0:
    nStrawberries = int(raw_input("\nHow many strawberries did you eat today? "))
    if nStrawberries < 10:
       print "\nHow about another strawberry..?\n"
       continue

    else:
        print "\nWow, you got your quota for today!!\n"
        break    

        
