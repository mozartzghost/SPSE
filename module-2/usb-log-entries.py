#!/usr/bin/python
#
#Script to extract USB events from logs
#Module 2 - lesson 1
#Mark Osborn 29/03/2013
#
#(I used 'syslog' as an example as there was no 'messages' file on my system)
#

print """\nLog file analysis - USB
=======================\n
"""

fd = open("/var/log/syslog", "r")
for line in fd.readlines():
        if "usb" in line.lower():
                print line
                fd2 = open("usb-log-entries.txt", "a")
                fd2.write(line)

print """\n Your log entries have also been saved to
'usb-log-entries.txt' in this directory.
"""

