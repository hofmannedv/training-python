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

# example data for a trapezoid
area = [
    [0.0, 2.0],
    [1.0, 2.0]
]

# calculate size of triangle
size = trapezoid(area)
print("The area has a size of %.2f cm^2" % size)
