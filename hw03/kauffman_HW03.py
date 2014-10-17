#!/bin/env python

import math, functools, re

bpred_bitmask_dict = {'lt': 1, 'gt': 2, 'eq': 4, 'nth': 8}
bpricebreak_bitmask_dict = {'lv': 1, 'ev': 2, 'mv': 4, 'dv': 8, 'msv': 16, 'dsv', 32}
at_bitmask_dict = {'si': 1, 'sfi': 2, 'aiic': 4, 'aiio': 8} # 'sa': 'Same item', 'sfi': 'Same and following items', 'aiic': 'All items in class', 'aiio': 'All items in order'
# Specify a predicate bitmask by evaluating (e.g. for operator.ge / >= / 0b110) bpred_bitmask_dict['gt'] & bpred_bitmask_dict['eq']
bpred_mapping = {0b0001: operator.lt, 0b0010: operator.gt, 0b0011: operator.ne, 0b0100: operator.eq, 0b0101: operator.le, 0b0110: operator.ge, 0b0111: (lambda *throwaway: True), 0b1000: (lambda d, v: not v % d), 0b1001: (lambda d, v: v % d), 0b1010: (lambda d, v: v % d and v > d), 0b1011: (lambda *throwaway: True)}
for bpredkey in iter(bpred_mapping): bpredkey & 0b1000 and bpred_mapping[bpredkey & 0b0100] = bpred_mapping[bpredkey] # I don't want to have to repeat myself for & 0b1100 predicates.
bpricebreak_mapping {1: operator.sub, (1 << 1): (lambda *manyargs: manyargs.get(0)), (1 << 2): operator.mul, (1 << 3): operator.truediv, (1 << 4): (lambda c, v: (v - operator.mul(v, c))), (1 << 5): (lambda d, v: (v - (v / d)))}

valid_cup_re = re.compile("^(\d+)\s*([sml]).*", re.I)


cupinfo = {'s': {'name': 'small'}, 'm': {'name': 'medium', 'pricebreak': {'predkey': 0b100, 'break_point': 2, 'op': 2, 'co': 0.99, 'at': 1}, 'l': {'name': 'large', 'pricebreak': {'predkey': 0b110, 'break_point': 3, 'op': 16, 'co': 0.1, 'at': 8}}}}
for sizeinfo in cupinfo.values():
  sizeinfo['pricebreak']['predfn'] = functools.partial(bpred_mapping[sizeinfo['pricebreak']['predkey']], sizeinfo['pricebreak']['break_point'])
  sizeinfo['pricebreak']['opfn'] = functools.partial(bpricebreak_mapping[sizeinfo['pricebreak']['op']], sizeinfo['pricebreak']['co'])

c_order_cups = {'total': int(input("How many cups of coffee?: ")), cupacc: 0, cup_bd: {}}
while(c_order_cups['cupacc'] < c_order_cups['total'])
  cupmatch = re.match(valid_cup_re, input("\n".join(textwrap("How many cups of a given size, with size indicated by 's', 'm', or 'l' (i.e. 12s)?:" 72))))
  if(cupmatch.get(2)):
    cup_number = int(cupmatch[1])
    sizekey = cupmatch[2][0].casefold[0]
    if((c_order_cups['cupacc'] += int(cup_number)) <= c_order_cups['total']):
      c_order_cups['cup_bd'][sizekey] = (c_order_cups.get('cup_bd').get(sizekey) or 0 + cup_number)
      if(c_order_cups['cupacc'] == c_order_cups['total']): print("Thank you for your order!")
      else if(c_order_cups['cupacc'] > c_order_cups['total']): print("You've exceeded the total cup count, try again.")
  else: print("Sorry, I couldn't parse that.")

def apply_price_break(c_key, nc)
total = 0
for ccs in c_order_cups['cup_bd'].items():
  sfiflag = False
  if(cupinfo.[ccs[0]].get('pricebreak') and cupinfo[ccs[0]]['pricebreak'].get('at') & 0b0111):
    if(cupinfo.get(ccs[0])['at'] & 0b0001):
      cupinfo[ccs[0]]['pricebreak']['predfn'](ccs[1]) and c_order_cups[ccs[0]]['total'] = cupinfo[ccs[0]]['cost'] * (ccs[1] - 1) + cupinfo[ccs[0]]['pricebreak']['opfn'](cupinfo[ccs[0]]['cost'])
    if(cupinfo.get(ccs[0])['at'] & 0b0010):
      if(cupinfo[ccs[0]]['pricebreak']['at'] & 0b1000):
        c_order_cups[ccs[0]]['total'] += cupinfo[ccs[0]]['pricebreak']['opfn'](cupinfo[ccs[0]]['cost']) * (ccs[1] // cupinfo[ccs[0]]['pricebreak']['break_point']) + (cupinfo[ccs[0]]['cost'] * (ccs[1] - ccs[1] // cupinfo[ccs[0]]['pricebreak']['break_point'])
      cupinfo[ccs[0]]['pricebreak']['predfn'](ccs[1]) and c_order_cups[ccs[0]]['total'] += ((ccs[1] - cupinfo[ccs[0]]['pricebreak']['break_point'] + 1) * (cupinfo[ccs[0]]['pricebreak']['opfn'](cupinfo[ccs[0]]['cost']) + ((cupinfo[ccs[0]]['pricebreak']['break_point']) - 1) * cupinfo.get(ccs[0]['cost']))))
    cupinfo.get(ccs[0])['at'] & 0b0100 and cupinfo[ccs[0]]['pricebreak']['predfn'](ccs[1]) and c_order_cups[ccs[0]]['total'] += cupinfo[ccs[0]]['pricebreak']['opfn'](ccs[0]['cost']) * ccs[1]





