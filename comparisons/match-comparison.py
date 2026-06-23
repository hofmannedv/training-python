# -----------------------------------------------------------
# demonstrates comparisons using match-case (requires Python 3.10)
#o
# (C) 2026 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# comparison using match-case
data = [10, 15, 20]

for value in data:
    match value:
        case 15:                       # check a specific value
            print(f"value has the requested value of 15")
        case 10 | 11 | 12 | 13 | 14:   # check a range of values
            print(f"value has a smaller value than 15 ({value})")
        case _:                        # wildcard: matches everything
            print(f"value has a different value ({value})")
