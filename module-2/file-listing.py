#!/usr/bin/python
#
# File / Dir listings using os.walk
# Module 2 - Exercise 2
# Mark Osborn 29/03/2013
#

import os, sys

path = sys.argv[1]

for path, dirs, files in os.walk(path):
    
  print "\n" + path
  
  for d in dirs:
    print "---" + d

    for f in files:
        print "------" + f
     
    

