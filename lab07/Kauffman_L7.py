#!/bin/env python
# $Header: nscc_csc110.09_14_1/lab07/Kauffman_L7.py, r6 201411210131 US/Pacific-New PST UTC-0800 robink@northseattle.edu Lab $

import operator, os, sys, textwrap
from functools import reduce

inp_filename = "numbers.txt"
if(len(sys.argv) >= 2):
  inp_filename = sys.argv[1]

mean = float()
if(os.access(inp_filename, os.R_OK)):
  inp_file = open(inp_filename, "rt")
  acc = float()
  lc = int()
  for t_ln in inp_file:
    lc += 1
    acc += float(t_ln)
  else:
    mean = acc / lc
  if(mean.is_integer): mean = int(mean)

def has_repeating_members(coll, myident = 3, num = 2):
  try:
    startindex = coll.index(myident) + 1
    if(startindex):
      subsearch = iter(coll[startindex:])
      if(operator.length_hint(subsearch) >= num - 1):
        for ign_count in range(num - 1):
          if(next(subsearch) != myident):
            break
        else:
          return True
    else: return False
  except ValueError:
    startindex = None
  return False

def find_sub_in_series_greedy(series = [1, 2, 3, 4, 5, 6, 7, 8, 6, 7, 8, 6, 8], search_series = [6, 7]):
  search_series_iter = iter(search_series) # Calling __iter__() on an iterator returns self, but calling the same on a collections.abc.Sequence tends to return a new collections.abc.Iterator.  We take advantage of that.
  cur_ind = int()
  matches = list()
  for match_max in range(len(series) - (len(series) % operator.length_hint(search_series))):
    try:
      if(cur_ind > (len(series) - operator.length_hint(search_series_iter))):
        break
      if(operator.length_hint(search_series_iter) > 0):
        if(operator.length_hint(search_series_iter) == len(search_series)):
          cur_ind = series.index(next(search_series_iter), cur_ind)
        elif(next(search_series_iter) == series[cur_ind + 1]): cur_ind += 1
        else:
          search_series_iter = iter(search_series)
      else:
        cur_ind += 1
        matches.append(cur_ind - len(search_series))
        search_series_iter = iter(search_series)
    except ValueError:
      cur_ind = len(search_series) - 1 # If collections.Sequence.index() fails to find an identity, it will always fail to find an identity.  Get out of this mess before we end up trying to find the same value in our (sub)set of remaining search space.
  return matches

def filter_series(series, search_series = [6, 7]):
  myseries = series.copy()
  matches_tofilter = find_sub_in_series_greedy(myseries, search_series)
  matches_tofilter.sort() # Match results should nominally be in ascending order already, but just in case...
  matches_tofilter.reverse() # I imagine things would get messy if I tried to pop using indeces in ascending order
  for match in matches_tofilter:
    del myseries[match:(match + len(search_series))]
  else:
    return myseries


repeating_identity_series = [1, 2, 3, 3, 4]
series_to_filter = [1, 7, 2, 6, 7, 6, 6, 8, 10, 7, 6, 1, 6]
subseries = [6, 7]
do_these_have_two_threes = has_repeating_members(repeating_identity_series, 3, 2)
series_acc = reduce(operator.add, filter_series(series_to_filter, subseries))
print("The sum of the numbers in {0} is {1}".format(inp_filename, mean))
print("The sum of the series:\n{0}\nwithout [6, 7] in the series is:\n{1}\nThe series {2} {3} contain a repeating number 3.".format(series_to_filter, series_acc, repeating_identity_series, do_these_have_two_threes and "does" or "does not"))
