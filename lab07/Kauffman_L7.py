#!/bin/env python
# $Header: nscc_csc110.09_14_1/lab07/Kauffman_L7.py, r1 201411201644 US/Pacific-New PST UTC-0800 robink@northseattle.edu Lab $

import functools, operator

search_series = [6, 7]
search_series_iter = iter(search_series) # Calling __iter__() on an iterator returns self, but calling the same on a collections.abc.Sequence tends to return a new collections.abc.Iterator.  We take advantage of that.

rep_sampleseries = [1, 2, 3, 3]
sampleseries = [1, 2, 3, 4, 5, 6, 7, 8, 6, 7, 8, 6, 8]
sampleseries_filtered = sampleseries.copy()
cur_ind = int()
match_ind = int()
matches = list()

def has_repeating_members(coll, myident = 3, num = 2):
  startindex = coll.index(myident)
  if(startindex):
    subsearch = iter(coll[startindex:])
    if(operator.length_hint(subsearch) >=num):
      for ign_count in range(num - 1):
        if(next(subsearch) == myident): None
        else: break
      else: True

for match_max in range(len(sampleseries_filtered) - (len(sampleseries_filtered) % operator.length_hint(search_series))):
  try:
    print(cur_ind, len(search_series), operator.length_hint(search_series_iter))
    if(cur_ind > (len(sampleseries_filtered) - operator.length_hint(search_series_iter))):
      break
    if(operator.length_hint(search_series_iter) > 0):
      if(operator.length_hint(search_series_iter) == len(search_series)):
        cur_ind = sampleseries_filtered.index(next(search_series_iter), cur_ind)
      elif(next(search_series_iter) == sampleseries_filtered[cur_ind + 1]): cur_ind += 1
      else:
        search_series_iter = iter(search_series)
    else:
      cur_ind and matches.append(cur_ind + 1 - len(search_series))
      cur_ind += 1
      search_series_iter = iter(search_series)
  except ValueError:
    print(cur_ind)
    cur_ind = len(search_series) - 1 # If collections.Sequence.index() fails to find an identity, it will always fail to find an identity.  Get out of this mess before we end up trying to find the same value in our (sub)set of remaining search space.


print(has_repeating_members(rep_sampleseries))
matches.reverse() # I imagine things would get messy if I tried to pop using indeces in ascending order
print(matches)
for match in matches:
  del sampleseries_filtered[match:(match + len(search_series))]
print(sampleseries_filtered)
sum = functools.reduce(operator.add, sampleseries_filtered)
print(sum)
