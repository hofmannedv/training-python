# -----------------------------------------------------------
# Python Data Science examples
# (C) 2025 Frank Hofmann, Germany 
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# calculate the convex hull (outer path) of a cloud of points
# calculation is done using the quickhull algorithm
# uses threads in order to run calculation in parallel
#
# inspired by buggy code from:
# Quickhull for Convex hull in Python
# https://www.geeksforgeeks.org/quickhull-for-convex-hull-in-python/
# -----------------------------------------------------------

import math
from threading import Thread
import queue
import random
import pickle

def findDistance(p1, p2, testpoint, recursionLevel = 0, verbosity = False):
    """
    Calculate the perpendicular distance between a point testpoint 
    and the line formed by the points p1 and p2.
    """

    if verbosity:
        print(f"[FD1] [{recursionLevel}] Calculating distance between {p1} - {p2} and {testpoint}")

    numerator = abs((p2[1]-p1[1])*testpoint[0] - (p2[0]-p1[0])*testpoint[1] + p2[0]*p1[1] - p2[1]*p1[0])
    denominator = math.sqrt((p2[1]-p1[1])*(p2[1]-p1[1]) + (p2[0]-p1[0])*(p2[0]-p1[0]))

    try:
    	result = numerator / denominator
    except:
        result = 0

    if verbosity:
        print(f"[FD2] [{recursionLevel}] Calculated distance between {p1} - {p2} and {testpoint}: {result}")

    return result

def findPosition(p1, p2, testpoint, recursionLevel = 0, verbosity = False):
    """
    Calculate whether a point testpoint is to the right or left side of 
    a line formed by the points p1 and p2.
    """

    if verbosity:
        print(f"[FP1] [{recursionLevel}] Calculating position between {p1} - {p2} and {testpoint}")

    # position = sign((Bx - Ax) * (Y - Ay) - (By - Ay) * (X - Ax))
    # 0: on the line
    # +1: on one side
    # -1: on the other side
    result = (p2[0] - p1[0]) * (testpoint[1] - p1[1]) - (p2[1] - p1[1]) * (testpoint[0] - p1[0])
    if verbosity:
        print(f"[FP1] [{recursionLevel}] Calculated position between {p1} - {p2} and {testpoint}: {result}")

    if result == 0:
        return 0
    if result < 0:
        return -1
    return 1

def isPointInTriangle(p1, p2, p3, testpoint, recursionLevel = 0, verbosity = False):
    """
    Determine if point testpoint is within the triangle (p1,p2,p3),
    or not
    """

    # define default return value: False
    result = False

    if verbosity:
        print(f"[IP1] [{recursionLevel}] Determine {testpoint} being in triangle ({p1}, {p2}, {p3})")

    # Calculate the barycentric coordinates of point testpoint with 
    # respect to the triangle 
    denominator = ((p2[1] - p3[1]) * (p1[0] - p3[0]) + (p3[0] - p2[0]) * (p1[1] - p3[1]))
    if denominator > 0:
        a = ((p2[1] - p3[1]) * (testpoint[0] - p3[0]) + (p3[0] - p2[0]) * (testpoint[1] - p3[1])) / denominator
        b = ((p3[1] - p1[1]) * (testpoint[0] - p3[0]) + (p1[0] - p3[0]) * (testpoint[1] - p3[1])) / denominator
        c = 1 - a - b
 
        # Check if all barycentric coordinates are non-negative
        if a >= 0 and b >= 0 and c >= 0:
            result = True

    return result

def quickHull(points = [], recursionLevel = 0, verbosity = False):
    """
    calculate the convex hull using the quickhull algorithm
    """

    # define output1, and output2 as empty queue
    output1 = queue.Queue()
    output2 = queue.Queue()

    # define default result: empty
    hull = []

    # check for more than one data point
    if len(points) < 2:
        if verbosity:
            print(f"[QH1] [{recursionLevel}] Less than two data points")
        return points		# nothing (more) to do

    def calculateHull(p1, p2, pointsList, recursionLevel = 0, verbosity = False, dataQueue = None):

        # check for an empty list of points
        if pointsList == []:
            if verbosity:
                print(f"[CH1] [{recursionLevel}] Cannot work on an empty list")
            return []

        # calculate the farthest point
        farthestPoint = max(pointsList, key=lambda p: findDistance(p1, p2, p, recursionLevel, verbosity))
        if verbosity:
            print(f"[CH2] [{recursionLevel}] Farthest point: {farthestPoint}")

        # calculate the remaining points
        nextPoints = []
        for testpoint in pointsList:
            if testpoint != farthestPoint:
                result = isPointInTriangle(p1, p2, farthestPoint, testpoint, recursionLevel, verbosity)
                if verbosity:
                    print(f"[CH3] [{recursionLevel}] Testing point: {result}")
                if not result:
                    if verbosity:
                        print(f"[CH4] [{recursionLevel}] Appending point: {testpoint}")
                    nextPoints.append(testpoint)
        if verbosity:
            print(f"[CH5] [{recursionLevel}] Next points: {nextPoints}")
            
        if not len(nextPoints):
            result = sorted([p1, p2, farthestPoint])
        else:

            # calculate the hull
            # - between point 1 and the farthest point
            part1 = calculateHull(p1, farthestPoint, nextPoints, recursionLevel + 1, verbosity, dataQueue)
            if verbosity:
                print(f"[CH6] [{recursionLevel}] Calculated hull part 1: {part1}")

            # - between the farthest point and point 2
            part2 = calculateHull(farthestPoint, p2, nextPoints, recursionLevel + 1, verbosity, dataQueue)
            if verbosity:
                print(f"[CH7] [{recursionLevel}] Calculated hull part 3: {part2}")

            # combine the results
            result = sorted(set(part1 + part2))

        if verbosity:
            print(f"[CH7] [{recursionLevel}] Calculated hull combined: {result}")

        # add result to output queue
        for element in result:
            dataQueue.put(element)

        return result

    # calculate the minimal, and maximal point
    minimalPoint = min(points)
    maximalPoint = max(points)
    if verbosity:
        print(f"[QH2] [{recursionLevel}] Minimal point: {minimalPoint}")
        print(f"[QH3] [{recursionLevel}] Maximal point: {maximalPoint}")

    # determine the points that are left, and right of the path
    leftPoints = []
    rightPoints = []
    for singlePoint in points:
        position = findPosition(minimalPoint, maximalPoint, singlePoint, recursionLevel)
        if position > 0:
            if verbosity:
                print(f"[QH4] [{recursionLevel}] Data point {singlePoint} classified as left point")
            leftPoints.append(singlePoint)
        if position < 0:
            if verbosity:
                print(f"[QH5] [{recursionLevel}] Data point {singlePoint} classified as right point")
            rightPoints.append(singlePoint)
        if position == 0:
            if verbosity:
                print(f"[QH6] [{recursionLevel}] Data point {singlePoint} removed")

    if verbosity:
        print(f"[QH7] [{recursionLevel}] Left data points: {leftPoints}")
        print(f"[QH8] [{recursionLevel}] Right data points: {rightPoints}")

    # calculate the hull for the left points
    thread1 = Thread(target=calculateHull, args=(minimalPoint, maximalPoint, leftPoints, recursionLevel + 1, verbosity, output1))
    thread1.start()

    # part1 = calculateHull(minimalPoint, maximalPoint, leftPoints, recursionLevel + 1, verbosity)
    #if verbosity:
    #    print(f"[QH9] [{recursionLevel}] Calculated hull part 1: {part1}")

    # calculate the hull for the right points
    thread2 = Thread(target=calculateHull, args=(minimalPoint, maximalPoint, rightPoints, recursionLevel + 1, verbosity, output2))
    thread2.start()

    #part2 = calculateHull(minimalPoint, maximalPoint, rightPoints, recursionLevel + 1, verbosity)
    #if verbosity:
    #    print(f"[QH10] [{recursionLevel}] Calculated hull part 2: {part2}")

    # end thread 1 and 2
    thread1.join()
    part1 = []
    while not output1.empty():
        part1.append(output1.get())

    if verbosity:
        print(f"[QH9] [{recursionLevel}] Calculated hull part 1: {part1}")

    thread2.join()
    part2 = []
    while not output2.empty():
        part2.append(output2.get())

    if verbosity:
        print(f"[QH10] [{recursionLevel}] Calculated hull part 2: {part2}")

    # add minimal, and maximal point
    part3 = [minimalPoint, maximalPoint]
    if verbosity:
        print(f"[QH11] [{recursionLevel}] Calculated hull part 3: {part3}")

    # return calculated convex hull with multiple entries removed
    hull = sorted(set(part1 + part2 + part3))
    if verbosity:
        print(f"[QH12] [{recursionLevel}] Calculated convex hull: {hull}")
    return hull

if __name__ == '__main__':

    # define verbosity
    verbosity = False

    # define level of recursion depth
    recursionLevel = 0

    # read data points from previously generated data file
    with open('points.data', 'rb') as fp:
        points = pickle.load(fp)

    hull = quickHull(points, recursionLevel, verbosity)
    if verbosity:
        print(f"[MA] [{recursionLevel}] Output: {hull}")
    else:
        print(f"Output: {hull}")
