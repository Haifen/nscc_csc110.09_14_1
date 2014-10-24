#!/bin/env python

# $Header: nscc_csc110_201409/lab05/kauffman_L5.py, r2 201410231852 US/Pacific-New PDT UTC-0700 robink@northseattle.edu Lab $
## Do a search for a series of numeric identities [1, 2, 3] in a list of ints (or instances of number-y things)

import re

## Collect the series
## MSOI is acryonymized "My Series of Identities"
msoi = list()
## Assume anything the user enters may be cast as an int()
## Assume anything that's not 0-9 is the user indicating they're done with text entry.
validentry_re = re.compile("^(\d+)?(.+)?$", re.I)

doneness_canary = False

while(doneness_canary == False):
  inm = re.match(validentry_re, input("Please enter a positive integer: "))
  if(inm.group(1)):
    msoi.append(int(inm.group(1)))
  else:
    print("\n\nThank you for your input!\n")
    doneness_canary = True

# Evil
msoi_rds = msoi.__iter__()

res_ind = int()
matched = bool()

if(len(msoi) < 3):
  print("Sorry, we cannot match against a series of length {}.\n".format(len(msoi)))
else:
  # Worse evil
  # This is not couched in a try: since hopefully we'll never call __next__() on the last element in the iterable list and hit StopIteration, but holy $&#* this is awful.
  while(msoi_rds.__length_hint__() > 3):
    if(msoi_rds.__next__() == 1 and msoi_rds.__next__() == 2 and msoi_rds.__next__() == 3):
      res_ind = len(msoi) - 3 - msoi_rds.__length_hint__()
      matched = True # Hooray, a "recursive descent" "iterator"  At least minimal persistent state plus some use of language primitives are in play.

if(matched):
  print("Match found at index {0} (element of count {1} when counting from one)".format(res_ind, (res_ind + 1)))
else:
  print("Sorry, we couldn't find the sequence [1, 2, 3] in your series.")

