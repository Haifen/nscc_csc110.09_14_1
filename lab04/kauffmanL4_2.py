#!/bin/env python

## Count the number of even integers given a series fed from stdin (should be a set, not a list)

import functools, operator, re

i_no_regexp = re.compile("^(\d+)?(n)?.*", re.I)

cont = True
iset = set()
odds = set()
while(cont):
  s_entry = input("Please enter a number: ")
  s_match = i_no_regexp.match(s_entry)
  if(s_match.group(2))
    print("Thank you, here is your tally:")
    iset_str = map(str, iset)
    print("Numbers entered:", ", ".join(iset_str))
    for uniq_int in iset:
      uniq_int & 1 and odds.update({uniq_int})
    evens = iset.difference(odds)
    evens_str = map(str, evens)
    print("Even numbers in that set:", ", ".join(evens_str))
    total = functools.reduce(operator.add, evens)
    print("Sum of even numbers in the set: {0}".format(total))
    cont = False # Could also use break here
  else:
    iset |= {int(s_match.group(1))}


