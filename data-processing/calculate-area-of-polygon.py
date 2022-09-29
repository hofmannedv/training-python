# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# calculate the size of a polygon (area)

def polyarea(coordinates):
    size = 0

    # a = x1*y2 + x2*y3 + ... + xn-1*yn + xn*y1
    # b = y1*x2 + y2*x3 + ... + yn-1*xn + yn*x1
    # size = 1/2 * |(a - b)|

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

area = [
    [1.0, 1.0],
    [1.0, 3.0],
    [2.0, 1.0]
]

size = polyarea(area)
print("The area has a size of %.2f cm^2" % size)
