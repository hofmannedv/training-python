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

    def __init__(self, xData = None, yData = None):
        """create a 2d data structure as object"""
        self.x = xData
        self.y = yData
        return

    def getX(self):
        """return the x component of the object"""
        return self.x

    def setX(self, xData = None):
        """set the x component of the object"""
        self.x = xData
        return

    def getY(self):
        """return the y component of the object"""
        return self.y

    def setY(self, yData = None):
        """set the y component of the object"""
        self.y = yData
        return

# define example data: data points as a regular list of tuples (x,y)
datapoints = [
    (3.5, 4.0), 
    (17.2, 2.5), 
    (6.3, 8.65), 
    (9.15, 8.2), 
    (4.2, 3.4)
]

# define an empty list of points
points = []

# go through the list if data, and create a new list entry based on
# Point class defined above
for xData,yData in datapoints:
    entry = Point(xData, yData)
    points.append(entry)

# determine the minimal, and maximal x value for the list of points
# - assume we have an empty list
minimalX = None
maximalX = None
minimalY = None
maximalY = None

# - go though the list
for entry in points:
    # extract the x value
    xValue = entry.getX()
    yValue = entry.getY()

    # update the smallest x value if unset, or higher than the current entry
    if minimalX == None or xValue < minimalX:
        minimalX = xValue

    # update the biggest x value if unset, or smaller than the current entry
    if maximalX == None or xValue > maximalX:
        maximalX = xValue

    # update the smallest y value if unset, or higher than the current entry
    if minimalY == None or yValue < minimalY:
        minimalY = yValue

    # update the biggest y value if unset, or smaller than the current entry
    if maximalY == None or yValue > maximalY:
        maximalY = yValue

print(f"the x value of the points ranges from {minimalX} to {maximalX}")
print(f"the y value of the points ranges from {minimalY} to {maximalY}")

