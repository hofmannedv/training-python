# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# calculate the extent of a polygon (area)
# use a vectorization to minimize calculation time

import math

def distance(vertice):
    # distance between two points is
    # sqr((x1 - x2)^2 + (y1 - y2)^2)

    point1 = vertice[0]
    point2 = vertice[1]

    # calculate size
    a = (point1[0] - point2[0])**2
    b = (point1[1] - point2[1])**2
    d = math.sqrt(a + b)
    print(point1, "to", point2, "is %.2f" % d)

    return d

def extent(vertices):
    size = 0

    components = map(distance, vertices)
    size = sum(components)

    return size

point1 = [1.0, 1.0]
point2 = [2.0, 1.0]
point3 = [2.0, 2.0]
point4 = [1.0, 2.0]

vertices = [
    [point1, point2],
    [point2, point3],
    [point3, point4],
    [point4, point1]
]

size = extent(vertices)
print("The area has an extent of %.2f cm" % size)
