#!/bin/env python

# $Header: nscc_csc110.09_14_1/lab06/Kauffman_L6_1.py, r4 201411061724 US/Pacific-New PST UTC-0800 robink@northseattle.edu Lab $
# Lab 3 starter code


# CSC 110

import functools, math, re, textwrap # Why have we imported the math module?

def main():
  print("This program is to test functions")
    
  ar_tr_tc = [[4, 5, 8], [2, 7, 9]]
  print("Testing areaTrapezoid...")
  for ar_tr_arg in ar_tr_tc:
     print("\n\nFunction inputs and outputs:\n\nBase1\t\tBase2\t\tHeight\t\tArea (computed)\n{1}\t\t{2}\t\t{3}\t\t{0}".format(areaTrapezoid(*ar_tr_arg), *ar_tr_arg))


  yesno = re.compile("^.*([Yy]).*$")
  # put your function calls here
  coord_pair = [3, 5]

  if(re.match(yesno, input("\n".join(textwrap.wrap("Would you like to enter a set of base linear dimensions for the trangle, or would you prefer to stick with the internal constants (Y to enter 90º dimensions, N to stick with constants) (Y/N): ", 72)))).group(1)):
    coord_pair[0] = float(input("Please enter the width of the triangle: "))
    coord_pair[1] = (float(input("Please enter the height of the triangle: ")))
  ud_tr_result = areaTriangle(*coord_pair)
  print("\n".join(textwrap.wrap("For a triangle of width {1} and height {2}, the area is {0}".format(ud_tr_result, *coord_pair))))

# This function calculates and returns the area of a trapezoid
# parameter: base1, the length of the top of the trapezoid
# parameter: base2, the length of the bottom
# parameter: height, the height of the trapezoid
# See this website for a picture  http://math.com/tables/geometry/areas.htm

def areaTrapezoid(base1, base2, height):

    area = height / 2.0 * (base1 + base2)

    return area

def areaTriangle(width, height):
  return width * height / 2.0

main()
