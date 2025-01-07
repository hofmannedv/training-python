# -----------------------------------------------------------
# Python Data Science examples
# (C) 2022-2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# calculate the extent of a polygon (area)
# use a vectorization to minimize calculation time
# -----------------------------------------------------------

import numpy as np

def distance(point1, point2):
    # geometric distance between two points is
    # sqr((x1 - x2)^2 + (y1 - y2)^2)

    print(point1, point2)

    # calculate length of the vertice
    a = (point1[0] - point2[0])**2
    b = (point1[1] - point2[1])**2
    d = np.sqrt(a + b)
    print(point1, "to", point2, "is %.2f" % d)

    return d

def extent(vertices):
    size = 0

    # vectorize distance
    vdistance = np.vectorize(distance, signature='(n),(n)->()')

    for vertice in vertices:
        d = vdistance(vertice[0], vertice[1])
        size += d

    return size

# define 4 points
point1 = [1.0, 1.0]
point2 = [2.0, 1.0]
point3 = [2.0, 2.0]
point4 = [1.0, 2.0]

# define the vertices based on the points
vertices = [
    [point1, point2],
    [point2, point3],
    [point3, point4],
    [point4, point1]
]

# calculate the extent of the polygon
size = extent(vertices)
print("The area has an extent of %.2f cm" % size)
