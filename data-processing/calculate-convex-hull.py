# -----------------------------------------------------------
# Python Data Science examples
# (C) 2025 Frank Hofmann, Germany 
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# calculate the convex hull (outer path) of a cloud of points
# calculation is done using the quickhull algorithm
# -----------------------------------------------------------

def quickHull(points = []):
    """calculate the convex hull using the quickhull algorithm"""

    # define default result: empty
    hull = []

    # return calculated convex hull
    return hull

# define cloud of points as a list of tuples
points = [
    (1.0, 1.0),
    (2.0, 1.0),
    (1.5, 1.5),
    (2.0, 2.0),
    (1.0, 2.0)
]

hull = quickHull(points)
print(hull)
