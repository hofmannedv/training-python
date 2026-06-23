# -----------------------------------------------------------
# demonstrates how to compare multi-line strings
#o
# (C) 2018-2026 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# import the additional module
import difflib

# define original text
# taken from: https://en.wikipedia.org/wiki/Internet_Information_Services
original = ["About the IIS", "", "IIS 8.5 has several improvements related", "to performance in large-scale scenarios, such", "as those used by commercial hosting providers and Microsoft's", "own cloud offerings."]

# define modified text
edited = ["About the IIS", "", "It has several improvements related", "to performance in large-scale scenarios."]

# initiate the Differ object
d = difflib.Differ()

# calculate the difference between the two texts
diff = d.compare(original, edited)

# output the result
print ('\n'.join(diff))
