#!/bin/env python

import functools, textwrap

# OK, I really really don't know what I'm doing w/r/t higher-order functions in
# Python, all I know is this particular mix of function decorators and
# function-passing gives me the result I want (behaves, memoizes, doesn't freak
# out as a result of trying to serialize the parent class).

# Everybody gets their own private collection of memoized values upon class
# instantiation.  Don't like it?  Too bad.
class TripInfo(dict):
	def __trip_cost_memoizable():
		@functools.lru_cache()
		def trip_cost(v, c): return v * c
		return trip_cost
	def __pergallon_memoizable():
		@functools.lru_cache()
		def pergallon(d, v): return d / v
		return pergallon
	def __init__(self, *args):
		self.trip_cost = __trip_cost_memoizable()
		self.pergallon = __pergallon_memoizable()
		super().__init__(*args)

	@property
	def cost(self, volume = None, cost = None):
		volume or volume = (self.get('fuel_volume') or 0)
		cost or cost = (self.get('perunit_cost') or 0)
		return self.trip_cost(volume, cost)
	@property
	def mpg(self, distance = None, volume = None):
		distance or distance = (self.get('distance') or 0)
		volume or volume = (self.get('fuel_volume') or 0)
		return self.pergallon(distance, volume)

# Build up a dictionary again

mpg = TripInfo({'linear_unit': input("\n".join(textwrap.wrap("What unit (singular, decapitalized, unless it's a proper noun) do you use to measure distance?:", 72)) + "  ")}) # Holy moses textwrap is irritating.
mpg['volumetric_unit'] = input("\n".join(textwrap.wrap("What unit (lower-case, unless a proper pronoun) do you use to measure volume?:", 72)) + "  ")
mpg['distance'] = float(input("\n".join(textwrap.wrap("What was the length of your trip in {linear_unit:s}s?:".format(**mpg), 72)) + "  "))
mpg['fuel_volume'] = float(input("\n".join(textwrap.wrap("How many {volumetric_unit:s}s did you use on your trip?:".format(**mpg), 72)) + "  "))
mpg['perunit_cost'] = float(input("\n".join(textwrap.wrap("What was the cost (in currency, unprefixed) per {volumetric_unit:s} of gas?:".format(**mpg), 72)) + "  "))

# Right, so now we get to see the fruits of our labors.
print("\n".join(textwrap.wrap("OK, here's what we know: Your trip was {distance:f} {linear_unit:s}s long.\nYou expended {fuel_volume:f} {volumetric_unit:s}s of gas.\nAt {perunit_cost:f} per {volumetric_unit:s}, your trip cost approximately {trip_cost:f} units of currency.\nFor the entirety of the trip, you averaged {pergallon:f} miles per gallon.".format(trip_cost = mpg.cost, pergallon = mpg.mpg, **mpg), 72)))
# ...and we're done.  Phew.

