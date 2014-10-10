#!/bin/env python

# $Header: nscc_csc110_201409/lab03/kauffman_L3.py, r1 201410092018 US/Pacific-New PDT UTC-0700 robink@northseattle.edu Lab $

import re

dayschedules = {'wd': [7, 10], 'we': [10, None]}
daykws = ['su', 'mo', 'tu', 'we', 'th', 'fr', 'sa']
daynames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
dayregexps = []
yesregexp = re.compile(".*yes.*", re.I) # Anything not yes is no, namsayin'?
for regexpstr in [".*sunday.*", ".*monday.*", ".*tuesday.*", ".*wednesday.*", ".*thursday.*", ".*friday.*", ".*saturday.*", ".*sunday.*"]: dayregexps.append(re.compile(regexpstr, re.I)) # This is dumb, but doesn't do anything too untoward.
daysdict = {}
for day in range(1, 6): daysdict.update({daykws[day]: {'schedule': dayschedules['wd']}})
for day in [0, 6]: daysdict.update({daykws[day]: {'schedule': dayschedules['we']}})
# Throw some indeces in there, because we're lazy and hate structured data.
for day in range(0, 7): daysdict.update({day: daykws[day]}) # This is dumb and bad (it's not even simple!)
# Why not assoc in some human-language names, while we're at it?
for day in range(0, 7): daysdict[daysdict[day]].update({'name': daynames[day]}) # It's becoming increasingly evident all of this should have been in an ordered list of complete dictionaries.
# and now it gets horrific
for day in range(0, 7): daysdict[daysdict[day]].update({'re': dayregexps[day]})
# We hate values-as-references but we like counting, and assume it's well-known that [0, 1] dereferences to ['regular_day', 'vacation_day']?  Jeez, we suck.
daystr = input("What day is it?: ")
daymatch = str()
for day in range(0, 7):
  if(re.match(daysdict[daysdict[day]]['re'], daystr)):
    daymatch = daysdict[day]
    break
else: daymatch = "We couldn't interpret the user's input."
on_vacat = bool(re.match(yesregexp, input("Are you on vacation?: "))) # You were right, Mr. W., there is a more succinct way of getting anything that doesn't behave like a predicate cast as a bool: cast it as a bool!
print("Today is {name}.  You are {vac_status} vacation.  Your alarm is set to go off at {alarm_hour}:00.\n".format(vac_status = on_vacat and "on" or "off", alarm_hour = daysdict[daymatch]['schedule'][int(on_vacat)], **daysdict[daymatch])) # Similarly, we can get [True, False] transformed to [1, 0] by calling int(our_bool) instead of (our_bool and 1 or 0)
