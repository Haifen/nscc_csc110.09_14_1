#!/bin/env python

import math, textwrap, re

class UnitBase(dict):
  @property
  def unit(self): return self.get('unit_s')
  @unit.setter
  def unit(self, unitstr = "meters"):
    self['unit_s'] = unitstr
  @property
  def sunit(self): return self.get('sunit_s')
  @sunit.setter
  def sunit(self, sunitstr = "centimeters"):
    self['sunit_s'] = sunitstr
  @property
  def unit_sum(self): return self.get('unit_sum_f')
  @unit_sum.setter
  def unit_sum(self, usf = 100):
    self['unit_sum_f'] = usf
    if(self.get('measure_f')):
      if(self.get('measure_f').is_integer()):
        self['breakdown'] = [int(self['measure_f']), 0] # Why does math.floor() exist if converting a float to an int does the same thing?
      else:
        self['breakdown'] = [(math.floor(self['measure_f']))]
        self['breakdown'].append((self['measure_f'] - self['breakdown'][0]) * self['unit_sum_f'])
  @property
  def measure(self): return self.get('measure_f')
  @measure.setter
  def measure(self, length):
    self['measure_f'] = length
    if(self.get('unit_sum_f')):
      if(self.get('measure_f').is_integer()):
        self['breakdown'] = [int(self['measure_f']), 0]
      else:
        self['breakdown'] = [(math.floor(self['measure_f']))]
        self['breakdown'].append((self['measure_f'] - self['breakdown'][0]) * self['unit_sum_f'])
  @property
  def splitmeasure(self): return self.get('breakdown')

yesno_regexp = re.compile(".*yes.*", re.I)
wantmetric_regexp = re.compile(".*metric.*", re.I)

unit_preferences = {'own_unit': (lambda uprs = 'yes': yesno_regexp.match(uprs) and True or False)(input("Do you wish to specify your own units?: "))}
if(unit_preferences['own_unit']):
  sldm = UnitBase({'unit_s': input('What is the name of your linear measurement unit (pluralized)?: ')})
  sldm.sunit = input('What is the name of your linear measurement subunit (pluralized)?: ')
  sldm.unit_sum = float(input('What do you multiply {unit_s:s} by to turn them into {sunit_s:s}?: '.format(**sldm)))
else:
  sldm = UnitBase((lambda stdnm = "metric": wantmetric_regexp.match(stdnm) and True or False)(input("Do you prefer metric or imperial?: ")) and {'unit_s': 'meters', 'sunit_s': 'centimeters', 'unit_sum_f': 100} or {'unit_s': 'feet', 'sunit_s': 'inches', 'unit_sum_f': 12})

sldm.measure = float(input('What is the linear dimension measurement in {unit_s:s}?: '.format(**sldm)))

print("\n".join(textwrap.wrap("Here's what we know:\nYour measurement of {0.measure} {0.unit} works out to measure {0.splitmeasure[0]} {0.unit} and {0.splitmeasure[1]} {0.sunit}.\n".format(sldm), 72)))

