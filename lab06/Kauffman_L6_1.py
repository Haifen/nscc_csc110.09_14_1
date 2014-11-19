#!/bin/env python

# $Header: nscc_csc110.09_14_1/lab06/Kauffman_L6_1.py, r5 201411061840 US/Pacific-New PST UTC-0800 robink@northseattle.edu Lab $
# Lab 3 starter code


# CSC 110

import functools, math, re, textwrap

def main():
  print("This program is to test functions")

  ar_tr_tc = [[4, 5, 8], [2, 7, 9]]
  print("Testing areaTrapezoid...")
  for ar_tr_arg in ar_tr_tc:
     print("\n\nFunction inputs and outputs:\n\nBase1\t\tBase2\t\tHeight\t\tArea (computed)\n{1}\t\t{2}\t\t{3}\t\t{0}".format(areaTrapezoid(*ar_tr_arg), *ar_tr_arg))


  yesno = re.compile("^.*([Yy])?.*$")
  # put your function calls here
  coord_pair = [3, 5]

  if(re.match(yesno, input("\n".join(textwrap.wrap("Would you like to enter a set of base linear dimensions for the right trangle, or would you prefer to stick with the internal constants (Y to enter 90º dimensions, N to stick with constants) (Y/N): ", 72)))).group(1)):
    coord_pair[0] = float(input("Please enter the width of the triangle: "))
    coord_pair[1] = (float(input("Please enter the height of the triangle: ")))
  ud_tr_result = hypRtTriangle(*coord_pair)
  print("\n".join(textwrap.wrap("For a right triangle of width {1} and height {2}, the hypotenuse is {0}".format(ud_tr_result, *coord_pair))))
  ichr = input("Please enter a single character: ")[0]
  print("Your character ({0}), {1} contain a vowel.".format(ichr, vowelcheck(ichr) and "does" or "does not"))

# This function calculates and returns the area of a trapezoid
# parameter: base1, the length of the top of the trapezoid
# parameter: base2, the length of the bottom
# parameter: height, the height of the trapezoid
# See this website for a picture  http://math.com/tables/geometry/areas.htm

def areaTrapezoid(base1, base2, height):

    area = height / 2.0 * (base1 + base2)

    return area

def areaTriangle(width, height): # This wasn't necessary (I didn't read the lab assignment spec closely enough)
  return width * height / 2.0

def hypRtTriangle(width, height): return math.sqrt(width ** 2 + height ** 2)

def vowelcheck(charcoll, matchset = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}): return charcoll[0] in matchset
vowelcheck_greek = (lambda charcoll, matchset = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}: charcoll[0] in matchset)
def vowelcheck_re(charcoll, matchre = re.compile("([AEIOUaeiou])")): return re.match(vowel.re, charcoll) and True or False
vowelcheck_re_greek = (lambda charcoll, matchre = re.compile("([AEIOUaeiou])"): re.match(vowel.re, charcoll) and True or False)

main()
