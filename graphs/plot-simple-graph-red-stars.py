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

v0 = 5
g = 9.81

t = np.linspace(0,1,21)		# create 21 time points
y = v0*t - 0.5*g*t**2     	# calculate each value per data point

plt.plot(t,y,'r*')		# plot t vs. y coordinates, red stars
plt.xlabel('t (s)')		# define label for x axis
plt.ylabel('y (m)')		# define label for y axis
plt.show()			# display plot
