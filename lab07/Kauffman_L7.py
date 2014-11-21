#!/bin/env python
# $Header: nscc_csc110.09_14_1/lab07/Kauffman_L7.py, r1 201411201644 US/Pacific-New PST UTC-0800 robink@northseattle.edu Lab $

import functools, operator

search_series = [6, 7]
search_series_iter = iter(search_series)

sampleseries = [1, 2, 3, 4, 5, 6, 7, 8]
sampleseries_filtered = sampleseries.copy()
cur_ind = int()
matches = list()

for sample_ind in range(len(sampleseries_filtered) // len(search_series)):
  if(len(search_series_iter) > 0):
    if(len(search_series_iter) == len(search_series)):
      cur_ind = search_series_filtered.index(next(search_series_iter), cur_ind)
      if(not cur_ind):
        break
      else:




print(sampleseries_filtered)
sum = functools.reduce(operator.add, sampleseries_filtered)
print(sum)
