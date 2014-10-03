#!/bin/env python

# Note to Mr. Wu:
# I know that a. I've already submitted homework #1 and b. I got a satisfactory
# (20/20) score on it, but I thought I'd submit this to let you know I've
# "fixed" it to use Python 3 string interpolation semantics (only use of
# format() and join(), no "String %(dictkey)s %(aaamorekeys)f" % dict).

# The former 'trip_cost' and 'pergallon' dictionary keys are now properties
# that expose a bound-per-instance function (bound to the instance, not the
# class since it memoizes the result (not that I did *not* do *anything* to
# actually implement memoization, I cheated and used functools' lru_memoize()
# decorator that does everything for me, and declared the wrapped function
# inside a give_me_a_memoizing_function HOF, which seems like The Way to do
# things like that, since you can't make (lambda a, b: a op b) actually return
# a value, rather just expose whatever the result of the last-evaluated
# expression was to the parent expression (sorta).  Like I said in the comment
# on my lab homework, I've been spending too much time fussing with Clojure and
# expect even Modula/Smalltalk hybrids like Python (which, thankfully, have a
# number of functional-friendly built-in functions (map, reduce, etc)) to treat
# any closure (whether defined with def(): or anonymously plunked in with
# (lambda:)) as first-class (can be passed around with no issue (that part
# Python does, for the most part) and is identical to a "native" function
# declared with whatever native macro/keyword/function the language exposes for
# setting up functions like a sane person would).

# So, my request with this isn't a re-evaluation of the homework in the context
# of this submission, and certainly isn't a request for an altered grade (which
# would be ludicrous), but rather a request that if I *do* submit homework that
# makes use of Python 2 conventions, *mark it down* and then allow me to
# correct it for an improved grade at your discretion.

# If I submit homework that makes use of the Python 2 convention you elided to
# in class today (calling a function *without* putting the arguments in
# parens), mark it 0.  I'm not even kidding.  My first "serious" language was
# C, my first high-level OO language was Ruby (which, despite the
# everything-is-an-object semantics and use of Iterators (basically for/while
# closures with declarative/reference-binding sugar) still demanded you
# generally enclose arguments in parens and enclose entire expressions in
# parens to force evaluation), and my most recent language exposure has been to
# Clojure (a LISP that sits on the JVM), so if I'm forgetting to enclose
# *arguments* in parens, something is very (*very*) wrong.

# OK, enough logorrhea, here's the actual Python3-ic script:

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
print("\n".join(textwrap.wrap("OK, here's what we know: Your trip was {distance:f} {linear_unit:s}s long.\nYou expended {fuel_volume:f} {volumetric_unit:s}s of gas.\nAt {perunit_cost:f} per {volumetric_unit:s}, your trip cost approximately {trip_cost:f} units of currency.\nFor the entirety of the trip, you averaged {pergallon:f} miles per gallon.".format(trip_cost = mpg.cost, pergallon = mpg.mpg, **mpg), 72))) # format() seems to prefer not to mix member accesses and positional arguments and/or dictionary keyword pairs, so while I would have preferred to call format() as format(mpg, **mpg) and be able to grab the properties via {.cost:f} and {.mpg:f}, that seems to not be easily doable, at least while destructured dictionaries are in the mix.
# ...and we're done.  Phew.

