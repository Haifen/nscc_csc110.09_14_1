#!/bin/env python

import math, textwrap, re

class UnitBase:
  def __init__(self, *args):
    self.unit_dict = dict(*args)
  @property
  def unit(self): return self.unit_dict.get('unit_s')
  @unit.setter
  def unit(self, unitstr = "meters"):
    self.unit_dict['unit_s'] = unitstr
  @property
  def sunit(self): self.unit_dict.get('sunit_s')
  @sunit.setter
  def sunit(self, sunitstr = "centimeters"):
    self.unit_dict['sunit_s'] = sunitstr
  @property
  def unit_sum(self): return self.unit_dict.get('unit_sum_f')
  @unit_sum.setter
  def unit_sum(self, usf = 100):
    self.unit_dict['unit_sum_f'] = usf
    if(self.unit_dict.get('units_f')):
      if(self.unit_dict.get('units_f').is_integer):
        self.unit_dict['breakdown'] = [int(self.unit_dict['units_f']), 0] # Why does math.floor() exist if converting a float to an int does the same thing?
      else:
        self.unit_dict['breakdown'] = [(math.floor(self.unit_dict['units_f']))]
        self.unit_dict['breakdown'].append((self.unit_dict['units_f'] - self.unit_dict['breakdown'][0]) * self.unit_dict['unit_sum_f'])
  @property
  def measure(self): return self.unit_dict.get('measure_f')
  @measure.setter
  def measure(self, length):
    self.unit_dict['measure_f'] = length
    if(self.unit_dict.get('unit_sum_f')):
      if(self.unit_dict.get('units_f').is_integer):
        self.unit_dict['breakdown'] = [int(self.unit_dict['units_f']), 0]
      else:
        self.unit_dict['breakdown'] = [(math.floor(self['units_f']))]
        self.unit_dict['breakdown'].append((self.unit_dict['units_f'] - self.unit_dict['breakdown'][0]) * self.unit_dict['unit_sum_f'])
  @property
  def splitmeasure(self): return self.unit_dict.get('breakdown')

yesno_regexp = re.compile(".*yes.*", re.I)
wantmetric_regexp = re.compile(".*metric.*", re.I)

sldm = UnitBase()
unit_preferences = {'own_unit': (lambda uprs = 'yes': yesno_regexp.match(uprs) and True or False)(input("Do you wish to specify your own units?: "))}
if(unit_preferences['own_unit']):
  sldm.unit = input('What is the name of your linear measurement unit (pluralized)?: ')
  sldm.sunit = input('What is the name of your linear measurement subunit (pluralized)?: ')
  print(sldm.unit_dict)
  sldm.unit_sum = float(input('What do you multiply {unit_s:s} by to turn them into {sunit_s:s}?: '.format(**sldm.unit_dict)))
else:
  sldm = UnitBase((lambda stdnm = "metric": wantmetric_regexp.match(stdnm) and True or False)(input("Do you prefer metric or imperial?: ")) and {'unit_s': 'meters', 'sunit_s': 'centimeters', 'unit_sum_f': 100} or {'unit_s': 'feet', 'sunit_s': 'inches', 'unit_sum_f': 12})

sldm.units = float(input('What is the linear dimension measurement in {unit_s:s}?: '.format(**sldm.unit_dict)))

print("\n".join(textwrap.wrap("Here's what we know:\nYour measurement of {0.units} {0.unit} works out to measure {0.splitmeasure[0]} {0.unit} and {0.splitmeasure[1]} {0.sunit}.\n".format(sldm), 72)))
