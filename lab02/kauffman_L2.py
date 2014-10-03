#!/bin/env python

import math, textwrap

# We ask the user to define their terms
sldm = {'unit_s': (input('What is the name of your linear measurement unit (pluralized)?: '))}
sldm['sunit_s'] = input('What is the name of your linear measurement subunit (pluralized)?: ')
sldm['unit_sum_f'] = float(input('What do you multiply {unit_s:s} by to turn them into {sunit_s:s}?: '.format(**sldm)))
sldm['units_f'] = float(input('What is the linear dimension measurement in {unit_s:s}?: '.format(**sldm)))
if(sldm['units_f'].is_integer()):
	sldm['breakdown'] = [int(sldm['units_f']), 0] # Why does math.floor() exist if converting a float to an int does the same thing?
else:
	sldm['breakdown'] = [(math.floor(sldm['units_f']))]
	sldm['breakdown'].append((sldm['units_f'] - sldm['breakdown'][0]) * sldm['unit_sum_f'])

print("\n".join(textwrap.wrap("Here's what we know:\nYour measurement of {units_f:f} {unit_s:s} works out to measure {breakdown[0]:d} {unit_s:s} and {breakdown[1]:f} {sunit_s:s}.\n".format(**sldm), 72)))





