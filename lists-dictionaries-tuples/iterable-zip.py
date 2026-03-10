# -----------------------------------------------------------
# demonstrates how to use the zip function
#o
# (C) 2015-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define variables zipCode, place
zipCode = ["10247", "01015", "80123", "14467"]
place = ["Berlin", "Dresden", "München", "Potsdam"]

# combine both zipCode and place
address = zip(zipCode, place)
print (address)

# output address
for item in address:
    print ("ZIP code: %s" % item[0])
    print ("place   : %s" % item[1])
    print (" ")
