# -----------------------------------------------------------
# demonstrates how to create bars in a graph
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# include standard modules from matplotlib
import matplotlib.pyplot as plt

# define example data
# - names
names = ['Tom', 'Joe', 'Reto', 'Peter', 'Hugh']
# - according value
points = [3.5, 17.2, 6.3, 9.15, 4.2]

# define the bar positions (y axis) from 0 to 4
yPos = range(5)

# display a horizontal bar based on y-Positions, the points, with a bar
# height of 80%, and centered alignment
plt.barh(yPos, points, height=0.8, align='center')

# set the description of the y axis as the names 
plt.yticks(yPos, names)

# set the description of the x axis as Points
plt.xlabel('Points')

# set the title of the graph
plt.title('Achievements')

# display the graph
plt.show()

