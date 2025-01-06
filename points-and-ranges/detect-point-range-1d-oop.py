# -----------------------------------------------------------
# algorithms for data points
# demonstrates how to determine the smallest, and biggest 
# value in a list of objects
#o
# (C) 2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

class Point:

    def __init__(self, xData = None):
        """create a 1d data structure as object"""
        self.x = xData
        return

    def getX(self):
        """return the x component of the object"""
        return self.x

    def setX(self, xData = None):
        """set the x component of the object"""
        self.x = xData
        return

# define example data as a regular list of floats
xData = [3.5, 17.2, 6.3, 9.15, 4.2]

# define an empty list of points
points = []

# go through the list if data, and create a new list entry based on
# Point class defined above
for xValue in xData:
    entry = Point(xValue)
    points.append(entry)

# determine the minimal, and maximal x value for the list of points
# - assume we have an empty list
minimalX = None
maximalX = None

# - go though the list
for entry in points:
    # extract the x value
    xValue = entry.getX()

    # update the smallest x value if unset, or higher than the current entry
    if minimalX == None or xValue < minimalX:
        minimalX = xValue

    # update the biggest x value if unset, or smaller than the current entry
    if maximalX == None or xValue > maximalX:
        maximalX = xValue

print(f"the x value of the points ranges from {minimalX} to {maximalX}")

