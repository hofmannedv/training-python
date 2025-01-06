# -----------------------------------------------------------
# algorithms for data points
# demonstrates how to determine the smallest, and biggest 
# value in a two-dimensional list of tuples of floats
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

# retrieve the x and y values
pointsX = []
pointsY = []
for coordinates in points:
    x,y = coordinates
    pointsX.append(x)
    pointsY.append(y)

# determine the minimal x value
minimalX = min(pointsX)

# determine the maximal x value
maximalX = max(pointsX)

# determine the minimal y value
minimalY = min(pointsY)

# determine the maximal y value
maximalY = max(pointsY)

print(f"the points range from {minimalX} to {maximalX} for x")
print(f"the points range from {minimalY} to {maximalY} for y")

