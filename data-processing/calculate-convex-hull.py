# -----------------------------------------------------------
# Python Data Science examples
# (C) 2025 Frank Hofmann, Germany 
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# calculate the convex hull (outer path) of a cloud of points
# calculation is done using the quickhull algorithm
#
# inspired by buggy code from:
# Quickhull for Convex hull in Python
# https://www.geeksforgeeks.org/quickhull-for-convex-hull-in-python/
# -----------------------------------------------------------

# ---- NOTE ----
#
# The code below is work in progress, and does not calculate the 
# convex hull properly, yet. The result contains too many points.
#
# --------------


import math

def findDistance(p1, p2, testpoint):
    """
    Calculate the perpendicular distance between a point testpoint 
    and the line formed by the points p1 and p2.
    """

    print("[FD1] calculating distance between", p1, "-", p2, "and", testpoint)

    numerator = abs((p2[1]-p1[1])*testpoint[0] - (p2[0]-p1[0])*testpoint[1] + p2[0]*p1[1] - p2[1]*p1[0])
    denominator = math.sqrt((p2[1]-p1[1])*(p2[1]-p1[1]) + (p2[0]-p1[0])*(p2[0]-p1[0]))

    try:
    	result = numerator / denominator
    except:
        result = 0

    return result

def findPosition(p1, p2, testpoint):
    """
    Calculate whether a point testpoint is to the right or left side of 
    a line formed by the points p1 and p2.
    """

    print("[FP1] calculating position between", p1, "-", p2, "and", testpoint)

    # position = sign((Bx - Ax) * (Y - Ay) - (By - Ay) * (X - Ax))
    # 0: on the line
    # +1: on one side
    # -1: on the other side
    result = (testpoint[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (testpoint[0] - p1[0])
    if result == 0:
        return 0
    if result < 0:
        return -1
    return 1

def quickHull(points = []):
    """calculate the convex hull using the quickhull algorithm"""

    # define default result: empty
    hull = []

    # check for more than one data point
    if len(points) < 2:
        print("[QH1] Less than three data points")
        return points		# nothing (more) to do

    def calculateHull(p1, p2, pointsList):

        # check for an empty list of points
        if pointsList == []:
            print("[CH1] Cannot work on an empty list")
            return []

        # calculate the farthest point
        farthestPoint = max(pointsList, key=lambda p: findDistance(p1, p2, p))
        print("[CH2] Farthest point:", farthestPoint)

        # calculate the remaining points
        nextPoints = []
        for p in pointsList:
            if findPosition(p1, farthestPoint, p) > 0:
                print("[CH2a] Appending point:", p)
                nextPoints.append(p)
        print("[CH3] Next points:", nextPoints)

        # calculate the hull
        # - between point 1 and the farthest point
        part1 = calculateHull(p1, farthestPoint, nextPoints)
        print("[CH4] Calculated hull part 1:", part1)

        # - farthest point itself
        part2 = [farthestPoint]
        print("[CH5] Calculated hull part 2:", part2)

        # - between point 2 and the farthest point
        part3 = calculateHull(farthestPoint, p2, nextPoints)
        print("[CH6] Calculated hull part 3:", part3)

        # combine the results
        # result = part1 + part2 + part3
        result = sorted(set(part1 + part2 + part3))
        print("[CH7] Calculated hull combined:", result)
        return result

    # calculate the minimal, and maximal point
    minimalPoint = min(points)
    maximalPoint = max(points)
    print("[QH2] Minimal point:", minimalPoint)
    print("[QH3] Maximal point:", maximalPoint)

    # calculate the hull for both directions
    part1 = calculateHull(minimalPoint, maximalPoint, points)
    part2 = calculateHull(maximalPoint, minimalPoint, points)
    part3 = [minimalPoint, maximalPoint]
    print("[QH4] Calculated hull part 1:", part1)
    print("[QH5] Calculated hull part 2:", part2)
    print("[QH6] Calculated hull part 3:", part3)

    # return calculated convex hull with multiple entries removed
    hull = sorted(set(part1 + part2 + part3))
    print("[QH7] Calculated convex hull:", hull)
    return hull

# define cloud of points as a list of tuples
points = [
    (0, 3),
    (1, 1),
    (2, 1),
    (4, 4),
    (0, 0),
    (1, 2),
    (3, 1),
    (3, 3)
]

hull = quickHull(points)
print("[MA] Output:", hull)
