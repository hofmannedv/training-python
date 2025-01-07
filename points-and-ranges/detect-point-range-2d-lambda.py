# -----------------------------------------------------------
# algorithms for data points
# demonstrates how to determine the smallest, and biggest 
# value in a two-dimensional list of tuples of floats using
# a lambda function
#o
# (C) 2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define example data: points as a regular list of tuples (x,y)
points = [
    (3.5, 4.0), 
    (17.2, 2.5), 
    (6.3, 8.65), 
    (9.15, 8.2), 
    (4.2, 3.4)
]

# sort the points according to the x axis
sortedPoints = sorted(points, key = lambda x: x[0])

# determine the minimal x value (first list entry)
minimalX = sortedPoints[0][0]

# determine the maximal x value (last list entry)
maximalX = sortedPoints[-1][0]

# sort the points according to the y axis
sortedPoints = sorted(points, key = lambda y: y[1])

# determine the minimal y value (first list entry)
minimalY = sortedPoints[0][1]

# determine the maximal y value (last list entry)
maximalY = sortedPoints[-1][1]

print(f"the points range from {minimalX} to {maximalX} for x")
print(f"the points range from {minimalY} to {maximalY} for y")

