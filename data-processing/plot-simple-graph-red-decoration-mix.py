# -----------------------------------------------------------
# Python Data Science examples
# (C) 2023 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later

# Plot a 2D curve using various parameters.
# Code based on examples from this book:
# Svein Linge, Hans Petter Langtangen:
# Programming for Computations - Python
# 2nd Edition, Springer Open
# -----------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# define the range in which the data shall be plotted
x = np.linspace(-2,2,1001)		# create 1001 time points

# define the two functions f(x), and g(x)
f = x**2
g = np.exp(x)

# plot the two functions
plt.plot(x,f,'r')			# plot f, colour red
plt.plot(x,g,'b--')			# plot g, colour blue, dashed

# decorate the plot
plt.xlabel('x')				# define label for x axis
plt.ylabel('f and g')			# define label for y axis
plt.grid(
	'on', 				# enable the grid
	color = 'gray', 		# set grid colour to gray
	linestyle = '--', 		# set dashed linestyle
	linewidth = 0.5			# set line thickness
)
plt.title('display f(x) and g(x)')	# add title to plot
plt.legend(['x^2', 'e^x'])		# add legend to plot
plt.axis([-3,3,-1,10])			# define axis size

# display the plot
plt.show()				# display plot
