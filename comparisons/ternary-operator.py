# -----------------------------------------------------------
# demonstrates comparisons using ternary operator
#o
# (C) 2026 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# assign weekday 
# - "Friday" if number == 5, 
# - "Saturday" if number == 6,
# - otherwise "other day"

data = [4, 7, 5]
for number in data:
    weekday = "Friday" if number == 5 else "Saturday" if number == 6 else "other day"
    print(f"number {number} results in {weekday}")
