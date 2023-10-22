# -----------------------------------------------------------
# Python Data Science examples
# calculate the size of a trapezoid (area)
#o
# (C) 2022-2023 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

def trapezoid(coordinates):
    """calculate the size of a trapezoid under a function
       
       coordinates is an array of two x-y-coordinates for
       the upper left, and upper right corner
    """

    # define size as 0
    size = 0

    # extract coordinates
    x1,y1 = coordinates[0][0],0		# lower, left corner
    x2,y2 = x1,coordinates[0][1]	# upper, left corner
    x3,y3 = coordinates[1]		# upper, right corner
    x4,y4 = x3,0			# lower, right corner

    # calculate size
    size = (x4 - x1) * 0.5 * (y2 + y3)

    return size

def calculateSingleTrapezoid():
    """calculate the area for a single trapezoid
       coordinates: 
       (0.0, 0.0) - (0.0, 2.0) - (1.0, 2.0) - (1.0, 0.0)
    """

    area = [
        [0.0, 2.0],
        [1.0, 2.0]
    ]

    # calculate size of the trapezoid
    size = trapezoid(area)
    print("The area has a size of %.2f cm^2" % size)

    return

def calculateListOfTrapezoids():
    """calculate the area for a list of data points"""

    data = [
        [0.0, 2.0],
        [1.0, 2.0],
        [2.0, 2.5],
        [3.0, 3.0],
        [4.0, 3.5],
        [5.0, 2.0]
    ]

    # initialize the total size
    totalSize = 0.0

    # calculate each trapezoid, and the total size
    for position in range(len(data) - 1):
        area = data[position:position + 2]
        size = trapezoid(area)
        print("area between", area, "has a size of", size, "cm^2")
        totalSize += size

    print("The area has a size of %.2f cm^2" % totalSize)

    return

def calculateTrapezoidFunction(xStart, xEnd, step):
    """calculate the area for a given range for a function"""

    # define underlying mathematical base function
    # f(x) = x^2 - 4x + 5

    # initialize the total size
    totalSize = 0.0

    # calculate the single trapezoids
    for xPosition1 in range(xStart, xEnd, step):
        xPosition2 = xPosition1 + step

        yPosition1 = xPosition1**2 - 4 * xPosition1 + 5
        yPosition2 = xPosition2**2 - 4 * xPosition2 + 5

        position1 = [xPosition1, yPosition1]
        position2 = [xPosition2, yPosition2]

        # calculate the trapezoid
        area = [position1, position2]
        size = trapezoid(area)
        # print("area between", area, "has a size of", size, "cm^2")

        # calculate the total size 
        totalSize += size

    print("The area between %.2f und %.2f with step %.2f has an approximate size of %.2f cm^2" % (xStart, xEnd, step, totalSize))

    return

calculateSingleTrapezoid()
calculateListOfTrapezoids()
for step in range(1, 51, 1):
   calculateTrapezoidFunction(0, 50, step)
