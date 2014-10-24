#!/bin/env python

# $Header: nscc_csc110_201409/lab05/kauffman_L5.py, r5 201410241459 US/Pacific-New PDT UTC-0700 robink@northseattle.edu Lab $
## Do a search for a series of numeric identities [1, 2, 3] in a list of ints (or instances of number-y things)

import itertools, re

## Collect the series
## MSOI is acryonymized "My Series of Identities"
msoi = list()
## Assume anything the user enters may be cast as an int()
## Assume anything that's not [+-]?[0-9]+ is the user indicating they're done with text entry.
validentry_re = re.compile("^([+-]?\d+)?(.+)?$", re.I)
search_s = [1, 2, 3] # Let's actually define what we're searching for

doneness_canary = False

while(doneness_canary == False):
  inm = re.match(validentry_re, input("Please enter an integer: "))
  if(inm.group(1)):
    msoi.append(int(inm.group(1)))
  else:
    print("\n\nThank you for your input!\n")
    doneness_canary = True

# Evil
msoi_rds = msoi.__iter__()

match_indeces = list()

if(len(msoi) < 3):
  print("Sorry, we cannot match against a series of length {}.\n".format(len(msoi)))
else:
  # Worse evil
  # This is not couched in a try: since hopefully we'll never call __next__() on the last element in the iterable list and hit StopIteration, but holy $&#* this is awful.
  msoi_lm = msoi_rds.__next__() # Oh god why
  while(msoi_rds.__length_hint__() > (len(search_s) - 2)):
    if(msoi_lm == search_s[0]):
      for subsearch_ident in search_s[1:]:
        msoi_lm = msoi_rds.__next__()
        if(not msoi_lm == subsearch_ident): break
      else:
        match_indeces.append(len(msoi) - 3 - msoi_rds.__length_hint__())
    else: msoi_lm = msoi_rds.__next__()

if(match_indeces): # Thank goodness for an empty list() evaluating as False
  print("The following matches have been found:\n")
  for ind in match_indeces:
    print("Match found at index {0} (element #{1}) of parent series.".format(ind, ind + 1))
else:
  print("Sorry, we couldn't find the sequence [1, 2, 3] in your series.")


  # This super-ugly "recursive" descent search needs to be properly implemented as a function that takes a variable-arity search list and always knows to quit when it's ahead.
  # If I were doing this "functionally", my crude approach would be to try to implement a general-purpose "reduce-while" function that would not only take a closure, a collection and an optional initial value but would also allow whomever was calling it to throw in a predicate (bound function or lambda) that would tell it to give up when that block returned False.
  # What I ought to implement, given that this is Python, would be a "higher-order" function that returned some object implementing an iterable interface that stepped over its contents only returning the identity of an item in the list when it was a matching component of a series and only set a boolean attribute and a (list of) inde(ces|x) of the match(es) when the entire set was evaluated.  This has the rather glaring flaw of returning not only a value, but a value that evaluates to True when only a subset of a match series has been encountered.  Thus, while it would be kinda cool, the identities in an iterable wouldn't be an accurate representation of the ultimate endgame (the index or indeces of where in the original list the match(es) began).
  # Lastly, I wouldn't know how to force in the extra object attributes (did_match = bool(), match_indeces = list()) were my little iterable "collection" cast to a proper sequential Python type (list(), etc), so the information that someone making use of this instance would really care about (did we match?  Where did we match?  If we care about partial matches, how well did we match?) would be completely thrown away.

## This ultimately should be made a function that returns an implementation of the iterable interface which returns wrapped match identity objects implementing subclasses of whatever the identity's native type is with the .data ideally set to whatever it is for the original matching identity, so that we can add our own attributes about where it is within the original collection or its current match group.  This ends up plugging into anything that does type checking, and it'll probably go nuts.

