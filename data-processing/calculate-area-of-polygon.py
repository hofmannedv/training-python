# -----------------------------------------------------------
# Python Data Science examples
# calculate the size of a polygon (area)
#o
# (C) 2022-2023 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

def polyarea(coordinates):
    "calculate the size of an polyarea"

    # define size as 0
    size = 0

    # a = x1*y2 + x2*y3 + ... + xn-1*yn + xn*y1
    # b = y1*x2 + y2*x3 + ... + yn-1*xn + yn*x1
    # size = 1/2 * |(a - b)|

    # identify the number of coordinates
    valueRange = range(len(coordinates))    # 0 to n - 1

    # calculate 1st component
    a = 0
    for value in valueRange:
        x = value
        y = value + 1
        if y > len(valueRange) - 1:
            y = 0
        a = a + coordinates[x][0] * coordinates[y][1]

    # calculate 2nd component
    b = 0
    for value in valueRange:
        y = value
        x = value + 1
        if x > len(valueRange) - 1:
            x = 0
        b = b + coordinates[x][0] * coordinates[y][1]

    # calculate size
    size = 0.5 * abs(a - b)

    return size

# example data for a triangle
area = [
    [1.0, 1.0],
    [1.0, 3.0],
    [2.0, 1.0]
]

# calculate size of triangle
size = polyarea(area)
print("The area has a size of %.2f cm^2" % size)
