#!/bin/env python

# $Header: nscc_csc110.09_14_1/hw07/Kauffman_HW7.py, r1 201411181839 US/Pacific-New PST UTC-0800 robink@northseattle.edu HW $

import functools, re, sys, textwrap

if(len(sys.argv) > 2 and sys.argv[2].isdigit()): ba_size = int(sys.argv[1])
else: ba_size = 4096
letter_set = set.union(set(map(chr, range(65, 91))), set(map(chr, range(97, 123))))
consonants = set.difference(letter_set, set("AEIOUaeiou"))
digits = set(map(chr, range(48, 58)))
digit_re = re.compile(".*(\d+).*")
punc_set = set("!~`^()_{}[]|\\;:\"',.?")
wordchar_set = set("@#$%&+-=<>*/")
fba = bytearray(ba_size)
