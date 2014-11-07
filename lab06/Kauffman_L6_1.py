# Lab 3 starter code


# CSC 110

import math, re, textwrap

def main():
  print("This program is to test functions")
    
  ar_tr_tc = [[4, 5, 8], [2, 7, 9]]
  print("Testing areaTrapezoid...")
  for arguments in ar_tr_tc:
     print("\n\nFunction inputs and outputs:\n\nBase1\t\tBase2\t\tHeight\t\tArea (computed)\n{1}\t\t{2}\t\t{3}\t\t{0}".format(areaTrapezoid(*arguments), *arguments))


  yesno = re.compile("^.*(y)?.*$")
  # put your function calls here
  coord_pair = [3, 5]

  if(re.match(yesno, input("\n".join(textwrap.wrap("Would you like to enter a set of base linear dimensions for the trangle, or would you prefer to stick with the internal constants (Y to enter 90º dimensions, N to stick with constants) (Y/N): ", 72)))).group(1)):
    ud_coord_pair = list(int(input("Please enter the width of the triangle: ")))




  
# This function calculates and returns the area of a trapezoid
# parameter: base1, the length of the top of the trapezoid
# parameter: base2, the length of the bottom
# parameter: height, the height of the trapezoid
# See this website for a picture  http://math.com/tables/geometry/areas.htm

def areaTrapezoid(base1, base2, height):

    area = height / 2.0 * (base1 + base2)

    return area


main()
