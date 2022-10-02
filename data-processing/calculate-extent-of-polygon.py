# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# calculate the extent of a polygon (area)

import math

def extent(coordinates):
    size = 0

    # distance between two points is
    # sqr((x1 - x2)^2 + (y1 - y2)^2)

    valueRange = range(len(coordinates))    # 0 to n - 1

    for position in valueRange:
        point1 = coordinates[position]
        if position == (len(coordinates) - 1):
            point2 = coordinates[0]
        else:
            point2 = coordinates[position + 1]

        # calculate size
        a = (point1[0] - point2[0])**2
        b = (point1[1] - point2[1])**2
        distance = math.sqrt(a + b)
        print(point1, "to", point2, "is %.2f" % distance)

        size = size + distance
    return size

area = [
    [1.0, 1.0],
    [2.0, 1.0],
    [2.0, 2.0],
    [1.0, 2.0]
]

size = extent(area)
print("The area has an extent of %.2f cm" % size)
