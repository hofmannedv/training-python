# -----------------------------------------------------------
# Python Data Science examples
# (C) 2023 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later

# Plot a 2D curve based on pre-calculated data points
# Code based on examples from this book:
# Svein Linge, Hans Petter Langtangen:
# Programming for Computations - Python
# 2nd Edition, Springer Open
# -----------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# define the range in which the data shall be plotted
x = (0.0, 1.0, 2.0, 3.0) 
y = (2.0, 2.0, 2.5, 3.0)

# define datapoints for a second graph to be taken into account
x2 = (0.0, 1.0, 2.0, 3.0) 
y2 = (0.25, 1.0, 0.5, 0.75)

fig, ax = plt.subplots()

# plot the data
# - first graph
ax.plot(
  x,y,					# plot the x and y data
  'r',					# colour red
  linestyle='--',			# set dashed linestyle
  marker='o'				# show datapoints as dots
)

# - second graph
ax.plot(
  x2,y2,				# plot the x and y data
  'g',					# colour green
  linestyle='--',			# set dashed linestyle
  marker='o'				# show datapoints as dots
)

# fill/colourize the area between the two graphs
ax.fill_between(
  x, y, 				# set the upper boundary of the drawing area
  y2, 					# set the lower boundary of the drawing area
  color='blue', 			# set the main colour to blue
  alpha=0.1				# set alpha value to 0.1 as transparency level
)

# decorate the plot
plt.xlabel('x axis')			# define label for x axis
plt.ylabel('y axis')			# define label for y axis
plt.grid(
  'on', 				# enable the grid
  color = 'gray', 			# set grid colour to gray
  linestyle = '--', 			# set dashed linestyle
  linewidth = 0.5			# set line thickness
)
plt.title('Plot title')			# add title to plot
plt.legend([
  'Data points 1',			# add legend to plot
  'Data points 2'
])
plt.axis([-1,4,-1,5])			# define axis size

# define the boundaries: left, and draw it as a blue dashed line
xLeftBoundary = (0.0, 0.0)
yLeftBoundary = (0.0, 2.0)
# plt.plot(xLeftBoundary, yLeftBoundary, 'b--')

# define the boundaries: right, and draw it as a blue dashed line
xRightBoundary = (3.0, 3.0)
yRightBoundary = (0.0, 3.0)
# plt.plot(xRightBoundary, yRightBoundary, 'b--')

# define black line with arrow for x coordinate axis
plt.arrow(
  -1, 0.0,				# start coordinates 
  5, 0.0, 				# length along x and y direction
  shape='full', 			# draw a full arrow
  linewidth=2, 				# define linewidth as 2 points
  length_includes_head=True, 		# add arrow before the end
  head_width=.15, 			# total width of the arrow head
  head_length=.15,			# total length of arrow head 
  color='k'				# set arrow colour to black
)

# define black line with arrow for y coordinate axis
plt.arrow(
  0.0, -1.0, 				# start coordinates
  0.0, 6.0, 				# length along x and y direction
  shape='full', 			# draw a full arrow
  linewidth=2, 				# define linewidth as 2 points
  length_includes_head=True, 		# add arrow before the end
  head_length=.25,			# total length of arrow head 
  head_width=.1, 			# total width of the arrow head
  color='k'				# set arrow colour to black
)

plt.show()				# display plot
