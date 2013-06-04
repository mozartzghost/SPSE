#!/usr/bin/python
#
#Module 1 - Part 4
#Exercise: demo of a for loop with an else statement
#Mark Osborn - 20-March-2013
#


print "\nWelcome to the even-odd detector"

numbers = [1,4,5,7,34,76,78,89,78,77,23,21,43,75,22]
even = []
odd = []

print "Our current list contains the following numbers:\n"
print numbers

for number in numbers:
    if number % 2 == 0:
        print "Even number detected: %s" % number
        even.append(number)
    
    else:
        print "Odd number found: %s" % number
        odd.append(number)

print "\nWe detected the following even numbers: %s" % even
print "\nWe detected the following odd numbers: %s" % odd    


                     

