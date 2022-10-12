# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# calculate the length of a track in 2D using numpy

# based on a proposal from:
# https://stackoverflow.com/questions/58713739/distance-matrix-between-two-point-layers

import numpy as np

# define 5 points
point1 = [1.0, 1.0]
point2 = [2.0, 2.0]
point3 = [3.0, 2.5]
point4 = [4.0, 2.1]
point5 = [5.0, 2.9]
points = [point1, point2, point3, point4, point5]

# separate x and y coordinates
x = []
y = []
for currentPoint in points:
    x.append(currentPoint[0])
    y.append(currentPoint[1])

print(x)
print(y)

x = np.asarray(x)
y = np.asarray(y)
x_i = x[:, np.newaxis]
x_j = x[np.newaxis, :]

y_i = y[:, np.newaxis]
y_j = y[np.newaxis, :]

# calculate distances
distances = (x_i-x_j)**2+(y_i-y_j)**2
result = np.sqrt(distances, out=distances)

# extract relevant distances, only
size = 0
position = 0
while position < len(points) - 1:
    size = size + result[position][position+1]
    position = position + 1

# calculate the length of the entire track
print("The track has a length of %.2f cm" % size)

