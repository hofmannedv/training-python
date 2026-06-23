# -----------------------------------------------------------
# demonstrates basic comparisons
#o
# (C) 2026 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# basic comparison using if-elif-else
data = [10, 15, 20]
for value in data:
    if value == 15:
        print(f"value has the requested value of 15")
    elif value < 15:
        print(f"value has a smaller value than 15 ({value})")
    else:
        print(f"value has a different value ({value})")
