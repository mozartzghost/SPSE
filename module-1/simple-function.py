#!/usr/bin/python
#
#Module 1 - Part 5
#Exercise: a simple function example
#Mark Osborn - 20-March-2013


def heading(text):
    length = len(text)
    print "-" * length
    print(text)
    print "-" * length

text = raw_input("\nPlease enter some text to become a heading: ")

heading(text)
