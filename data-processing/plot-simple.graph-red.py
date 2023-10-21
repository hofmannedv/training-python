# Python Data Science examples
# (C) 2023 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# plot a 2D curve
# example originates from this book:
# Svein Linge, Hans Petter Langtangen:
# Programming for Computations - Python
# 2nd Edition, Springer Open

import numpy as np
import matplotlib.pyplot as plt

v0 = 5
g = 9.81

t = np.linspace(0,1,1001)	# create 1001 time points
y = v0*t - 0.5*g*t**2     	# calculate each value per data point

plt.plot(t,y,'r')		# plot t vs. y coordinates, colour red
plt.xlabel('t (s)')		# define label for x axis
plt.ylabel('y (m)')		# define label for y axis
plt.show()			# display plot
