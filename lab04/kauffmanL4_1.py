#!/bin/env python

# $Header: nscc_csc110_201409/lab04/kauffman_L4_2.py, r1 201410161829 US/Pacific-New PDT UTC-0700 robink@northseattle.edu Lab $

TUIT_IN = 3000.0
INTEREST = 0.025
DURATION = 5

def muladd(acc, multiplicand):
  return acc + (acc * multiplicand)

cost = float()
total = float()
for year in range(1, DURATION + 1):
  cost = muladd(cost or TUIT_IN, INTEREST)
  total += cost
  print("At year {0}, cost of attending school is {1}".format(year, cost))

print("After {0} of college, the total amount of the projected tuition will be: {1}".format(DURATION, total))
