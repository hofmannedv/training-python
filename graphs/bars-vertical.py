# -----------------------------------------------------------
# Python Data Science examples
# demonstrates how to create vertical bars as a graph
#o
# (C) 2015-2023 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# include standard modules from matplotlib
import matplotlib.pyplot as plt

# define example data
# - names
names = ['Tom', 'Joe', 'Reto', 'Peter', 'Hugh']
# - according value
points = [3.5, 17.2, 6.3, 9.15, 4.2]

# define the bar positions (x axis) from 0 to 4
xPos = range(5)

# display a vertical bar based on x-positions, the points, with a bar
# width of 80%, and centered alignment
plt.bar(xPos, points, width=0.8, align='center')

# set the description of the x axis as the names 
plt.xticks(xPos, names)

# set the description of the y axis as Points
plt.ylabel('Points')

# set the title of the graph
plt.title('Achievements')

# display the graph
plt.show()

