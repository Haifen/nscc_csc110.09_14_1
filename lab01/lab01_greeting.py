#!/bin/env python

# input section
name = input('Please enter your name: ')

# output section
print ( "hello ", name, ".  Nice to meet you." )

# Ask a couple of questions and assoc the result to a dictionary
res = {'more_csc': (input("Are you interested in pursuing CSC beyond this class? "))} # The developer has written too much Clojure, and concedes nesting the 'input' call in parens isn't necessary to force evaluation in the context of assignment.
res['other_major'] = (input("If pursuing another major, what would you like to major in? ")) # Also, the developer ought to ask more interesting questions.

print("OK, here's what we know so far:\nYour answer to whether you want to continue CSC beyond this class was %(more_csc)s.\nYour current major is %(other_major)s" % res)
