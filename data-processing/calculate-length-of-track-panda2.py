# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# calculate the length of a track in 2D

import pandas as pd
import numpy as np

def distance(vertex):
    # geometric distance between two points is
    # sqr((x1 - x2)^2 + (y1 - y2)^2)

    # extract the two points
    point1 = vertex[0]
    point2 = vertex[1]

    # calculate length of the vertex
    a = (point1[0] - point2[0])**2
    b = (point1[1] - point2[1])**2
    d = np.sqrt(a + b)
    print(point1, "to", point2, "is %.2f" % d)

    return d

def trackLength(vertices):
    size = 0

    # apply the function distance() to all vertices
    components = map(distance, vertices)

    # result is an array of numbers that we can sum up
    size = sum(components)

    return size

# define 5 points
point1 = ['P1', 1.0, 1.0]
point2 = ['P2', 2.0, 2.0]
point3 = ['P3', 3.0, 2.5]
point4 = ['P4', 4.0, 2.1]
point5 = ['P5', 5.0, 2.9]
points = [point1, point2, point3, point4, point5]

# define an empty dataframe
df = pd.DataFrame({})

for specificPoint in points:
    name = specificPoint[0]
    coordinates = specificPoint[1:]
    df[name] = pd.Series(coordinates, index=['x', 'y'])

print(df)

# define list of vertices for extent
vertices = []

columnNames = df.columns
position = 0
while position < len(columnNames) - 1:
    nameP1 = columnNames[position]
    nameP2 = columnNames[position + 1]
    print("track from", nameP1, "to", nameP2)
    position = position + 1

    # generate new vertex, and add it to the list of vertices
    p1 = [df[nameP1]['x'], df[nameP1]['y']]
    p2 = [df[nameP2]['x'], df[nameP2]['y']]
    vertices.append([p1, p2])

# print(vertices)

# calculate the length of the entire track
size = trackLength(vertices)
print("The track has a length of %.2f cm" % size)

