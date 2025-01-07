# -----------------------------------------------------------
# Python Data Science examples
# (C) 2022-2025 Frank Hofmann, Germany 
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# calculate the extent of a polygon (area)
# use the ComplexHull class from ScyPy to calculate the border of the polygon
# use the map function to calculate the border length (extent)
# -----------------------------------------------------------

from scipy.spatial import ConvexHull
import numpy as np

def distance(vertice):
    # geometric distance between two points is
    # sqr((x1 - x2)^2 + (y1 - y2)^2)

    # extract the two points
    point1 = vertice[0]
    point2 = vertice[1]

    # calculate length of the vertice
    a = (point1[0] - point2[0])**2
    b = (point1[1] - point2[1])**2
    d = np.sqrt(a + b)
    print(point1, "to", point2, "is %.2f" % d)

    return d

def extent(vertices):
    size = 0

    # apply the function distance() to all vertices
    components = map(distance, vertices)

    # result is an array of numbers that we can sum up
    size = sum(components)

    return size

# define 5 points
point1 = [1.0, 1.0]
point2 = [2.0, 1.0]
point3 = [2.0, 2.0]
point4 = [1.0, 2.0]
point5 = [1.5, 1.5]

points = [point1, point2, point3, point4, point5]
print(points)

# calulate extent using ConvexHull class
hull = ConvexHull(points)

# define list of vertices for extent
vertices = []

#print(hull.simplices)
for vertex in hull.simplices:
    #print(vertex)
    p1 = vertex[0]
    p2 = vertex[1]
    print(points[p1], "->", points[p2])
    vertices.append([points[p1], points[p2]])

# calculate the extent of the polygon
size = extent(vertices)
print("The area has an extent of %.2f cm" % size)

