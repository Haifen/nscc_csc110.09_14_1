#!/bin/env python

# $Header: nscc_csc110_201409/hw02/kauffman_HW02.py, r1 201410090017 US/Pacific-New PDT UTC-0700 robink@northseattle.edu Hw $
# Apologies for being 22 minutes late.
## Calculate linear dimensions required for construction work in a completely unexciting room (right prism) of order {|n| n <= 3} plus total unit cost of corresponding n-dimensionally-measured ({|n| n <= 3}) materials, based on individually specified linear dimensions (a tuple of three floating-point values, for three right axes).

#Sorry, Mr. Wu, but the hashbang takes precedence over a descriptive comment.
#Header format is a butchered derivative of Gentoo's (CVS', really) (too much verbosity about locale, unapologetic POSIX format of the datestring, literal TZ offset in case you couldn't work it out, NetID instead of standard simple UNIXy username (robink@northseattle.edu instead of robink ("robink according to who?", one might ask)), SVN-style revisions instead of (CV|RC)S' attempt to do major, minor and point version management) ebuild header format, typically used by developers (but also appropriated by users and unofficial developers for marking up ebuilds they have in personal overlays).  It is decidedly unoriginal, it may suck, but it will never change.
#P.S.: Everything is available on GitHub if you want to browse changes (I do commit changes to files over time, rather than just check in the finished version, you just don't usually see the set of changes that happen in a lab session, since I don't have easy access to Git and plink/OpenSSH on the lab machines).  The URLs are https://github.com/Haifen/nscc_csc110_201409 for the WebIF and SmartGit, git://github.com/Haifen/nscc_csc110_201409 for a fast checkout using any vintage Git client, and ssh://git@github.com/Haifen/nscc_csc110_201409 if you have a GitHub account and commit access to the repo.

import textwrap

print("\n".join(textwrap.wrap("This program will calculate volumetric dimensions of an ordinary room (right prism), will work out total surface area of the interior, will tell you surface area of just the floor (or ceiling), and will tell you the combined linear measurement of the perimeters of the floor and ceiling.  Based on perunit currency conversion for a given volume of paint (in gallons) and a given surface area of flooring (in feet**2), it will tell you approximately how much it will cost to cover the entirety of the wall and ceiling in paint, and the floor in flooring material.")))

# Let's be able to talk about our dimensions if someone asks
axes = {'x': {'axis': 'x', 'name': 'width', 'index': 0}, 'y': {'axis': 'y', 'name': 'height', 'index': 1}, 'z': {'axis': 'z', 'name': 'depth', 'index': 2}} # This is dumb, but I didn't want to bind each member of the axis set to a value( read: positional)-based reference by throwing them in a list, so the key identifying an axis shares identity with the value assigned to the 'axis' key in its associated dict
dims = {0: axes['x'], 1: axes['y'], 2: axes['z'], 'width': axes['x'], 'height': axes['y'], 'depth': axes['z']} # This was the reason for the above assignment.  The problem is making identity assignments that can't be as easily looked up via __next__ on something iterable which also uses the value of the parent key in the subkey is brain-damaged before you even get into the subject of the pitfalls of multiple equivalent identities in a hierarchy without any kind of qualifying indirection.  So, yeah, this is stupid, but I think it's being assigned in by reference, so yay for not completely wasting gobs of process space.
for axisliteral in axes: dims.update({axisliteral: axes[axisliteral]}) # but I got some stupid and unnessecary automation out of it!  Win!

# Room's linear dimensions are stored as an array (it would, of course, be possible (although horrible and ugly) to slip three closures straight into a tuple definition/assignment and slap it down right then and there (yay immutability!), but despite the fact that tuples are subscriptable, and despite the fact that it's unlikely one would change a single linear value as opposed to the set (excepting the possibility that they may be interested in correcting a single error), and despite the fact that values as references are bad no matter which language camp you're from, being able to use the mental constant of x index = 0, y index = 1, etc is hopefully enough in this case (simple, but arguably not documentable).  Plus I've got a big ugly hash to help me out with the relationships if I get confused).
print("\n".join(textwrap.wrap("Units are in feet, and volumetric units (when not feet cubed) are in gallons.  Please be consistent in your use of them when specifying measurements and perunit cost.  Were I clever I would be figuring out the relationship between the volumetric unit (gallons of paint) and area unit (square feet of wall), or at least hardcoding some fixed-power-and-coefficient relationships between units of paint and units of wall area.  Were I really clever I'd be able to not only have a nice cubic relationship between the unit of paint and the linear dimensions of the room (one could assume the necessary paint could be expressed as the cube of the sum of the linear dimensions of the area, with some constant thrown in there before we take things to dimensions cubed, since you can envision coats of paint as barely 3-dimensional slabs of (un)dried paint matter), and also suss out the inverse relationship between how much paint you'll need to be semi-consistently n millimeters from the wall surface and the increase in the fractional dimension of the wall surface as it bends at 90º at each corner, but holy heck, I'm nowhere near that schooled.", 72)))
room_ld_arr = [float(input("Please enter the {x[name]} of the room (in feet): ".format(**dims)))]
room_ld_arr.append(float(input("Please enter the {y[name]} of the room (in feet): ".format(**dims))))
room_ld_arr.append(float(input("Please enter the {z[name]} of the room (in feet): ".format(**axes))))

# You requested simple, and something that sticks to the contract outlined in the assignment description, so I won't ask for a window area percentage.
WINDOW_ratio = 0.1 # I don't actually have to store it as a percentage, do I?
WALLS_sqfttogallon = 350

room_goods_cost = {'paint': float(input("Please enter the cost of one gallon of paint, in unprefixed currency: ")), 'flooring': float(input("\n".join(textwrap.wrap("Please enter the cost of one square foot of flooring, in unprefixed currency:", 72)) + " "))} # Aaa, multiple side-effectful expressions in a single reader type.  May the ghost of McCarthy forgive me.  Hey, it's simple, though, right?

floor_area = (room_ld_arr[0] * room_ld_arr[1])
floor_perimeter = (room_ld_arr[0] + room_ld_arr[1])
trim_length = (floor_perimeter * 2)
room_volume = (room_ld_arr[0] * room_ld_arr[1] * room_ld_arr[2])
room_area_acc = int()
for i in range(3):
  room_area_acc += (2 * (room_ld_arr[i] * room_ld_arr[((i + 1) % 2)])) # Multiply the ith linear dimension by the subsequent one, wrapping around to the start if we run off the end of our valid index value series.
else:
  room_area_acc # Pointless, especially since you can't seem to assign or LHA from a for, but whatever.


# There is a better way to do this.  There has to be.  There *has* to.
walls_ceiling_area = int()
for i in range(2):
  walls_ceiling_area += (2 * (room_ld_arr[i] * room_ld_arr[(i + 1)]))
walls_ceiling_area += room_ld_arr[0] * room_ld_arr[2]
walls_ceiling_area -= (walls_ceiling_area * WINDOW_ratio)

# OK, now we state what we know without memoizing any return values from the following expressions

print("\n".join(textwrap.wrap("You stated the room was {0} feet wide, {1} feet long, and {2} feet deep.  You said that paint cost \00a4{paint} per gallon, and that flooring was \00a4{flooring} per square foot.\n".format(*room_ld_arr, **room_goods_cost), 72)))
print("\n".join(textwrap.wrap("Here's what we think we know about the room:\nThe total volume of the interior is {0} cubic feet.\nThe total surface area enclosing the interior of the room is {1} square feet.\nThe likely paintable portion of the walls and ceiling occupy {2} square feet, and the area of the floor is {3} square feet.  The perimiter of either the floor or the ceiling is {4} feet in length.  Double that (to approximate necessary length of trim for both top and bottom of room) is {5}.\nAt \u00a4{paint} per gallon, and at approximately {6} gallons of paint required to cover a square foot of interior surface, it will cost you approximately \u00a4{7:.2f} to paint the walls and ceiling.\nAt \u00a4{flooring:.2f} per square foot of flooring, it will cost you approximately \u00a4{8:.2f} to cover the cost of laying down flooring material covering the entire surface of the room's floor.".format(room_volume, room_area_acc, walls_ceiling_area, floor_area, floor_perimeter, trim_length, (1.0 / WALLS_sqfttogallon), (room_goods_cost['paint'] * (walls_ceiling_area / WALLS_sqfttogallon)), (room_goods_cost['flooring'] * floor_area), **room_goods_cost), 72)))


