#!/usr/bin/python
#
#Module 1 - Part 6
#Exercise: a simple class
#Mark Osborn - 20-March-2013


class employee:
    def __init__(self, salary):
        self.wage = salary
        print "employee initialised!"

    def tax(self):
        return int(self.wage * 0.25)
        #do some stuff


class manager(employee):
    print "manager initialised!"

    def payIncrease(self):
        return int(self.wage * 1.05)
    

mark = employee(75000)
john = employee(45000)
jack = employee(56333)
kylie = manager(120000)

print "\nmark has a salary of: %d" % mark.wage
print "mark will pay %d in tax\n" % mark.tax()


print "john has a salary of: %d" % john.wage
print "john will pay %d in tax\n" % john.tax()

print "jack has a salary of: %d" % jack.wage
print "jack will pay %d in tax\n" % jack.tax()

print "kylie has a salary of: %d" % kylie.wage
print "kylie will pay %d in tax\n" % kylie.tax()
print "kylie can get a pay increase to %d !!" % kylie.payIncrease()

