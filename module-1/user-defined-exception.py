#!/usr/bin/python
#
#Exercise - User-defined exception
#Mark Osborn
#28/03/2013

import sys

class illegalColour(Exception):
    
    def __init__(self, colour):
        self.disallowed_colour = colour

    def __str__(self):
        return repr(self.disallowed_colour)
    

print """
!!!Congratulations on winning a new car!!!

You now need to choose a colour; we have the following available -

- Red
- Blue
- Green

"""

carColour = raw_input("Please choose a colour for your new car:")

try:
    if carColour.lower() != 'red':
        print "\nYou have selected %s - which is unfortunate." % carColour
        raise illegalColour(carColour)

    else:
        print "\n You have selected 'Red' - an excellent choice!"   

except illegalColour as ex:
    print "Exception occurred for colour choice: " +ex.disallowed_colour
    

finally:
    print "\n Sometimes we don't have all the colours in stock...\n"
    
