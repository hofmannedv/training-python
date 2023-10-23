# -----------------------------------------------------------
# Python Data Science examples
# calculate the area between functions, or two sets of data points
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

def calculateListOfTrapezoids(data):
    """calculate the area for a list of data points"""

    # initialize the total size
    totalSize = 0.0

    # calculate each trapezoid, and the total size
    for position in range(len(data) - 1):
        area = data[position:position + 2]
        size = trapezoid(area)
        print("area between", area, "has a size of", size, "cm^2")
        totalSize += size

    print("The area has a size of %.2f cm^2" % totalSize)

    return totalSize

def calculateAreaBetweenGraphs(dataset1, dataset2):
    """calculate the area between two graphs given as datasets"""

    sizeArea1 = calculateListOfTrapezoids(dataset1)
    sizeArea2 = calculateListOfTrapezoids(dataset2)

    return abs(sizeArea1 - sizeArea2)

# define the dataset #1 as a list of tuples of x-y-coordinates
dataset1 = [
    (0.0, 2.0),
    (1.0, 2.0),
    (2.0, 2.5),
    (3.0, 3.0)
]

# define the dataset #2 as a list of tuples of x-y-coordinates
dataset2 = [
    (0.0, 0.25),
    (1.0, 1.0),
    (2.0, 0.5),
    (3.0, 0.75)
]

totalSize = calculateAreaBetweenGraphs(dataset1, dataset2)
print("the size of the area between the two graphs is %.2f cm^2" % totalSize)
