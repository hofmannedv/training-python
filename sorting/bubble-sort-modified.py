# -----------------------------------------------------------
# sort a list using modified bubble sort
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

data = [34, 12, 67, 55, 10]
result = []
print(data, "->", result)

position = 0                 # from
run = len(data)              # to
while position < run:
    minimum = min(data)      # detect smallest value
    minimumPosition = data.index(minimum) # detect position

    # extend result by minimum value
    result.append(minimum)

    # remove minimum from data
    del(data[minimumPosition])

    print(data, "->", result)

    # move one element
    position = position + 1
