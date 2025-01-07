# -----------------------------------------------------------
# algorithms for data points
# demonstrates how to determine the smallest, and biggest 
# value in a two-dimensional Pandas dataframe
#o
# (C) 2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# import Pandas module
import pandas as pd

# define example data: points as a regular list of tuples (x,y)
data = [
    (3.5, 4.0), 
    (17.2, 2.5), 
    (6.3, 8.65), 
    (9.15, 8.2), 
    (4.2, 3.4)
]

# convert data to points dataframe
points = pd.DataFrame(data, columns=list('xy'))

# identify smallest, and biggest x value
minimalX = points['x'].min()
maximalX = points['x'].max()

# identify smallest, and biggest y value
minimalY = points['y'].min()
maximalY = points['y'].max()

print(f"the points range from {minimalX} to {maximalX} for x")
print(f"the points range from {minimalY} to {maximalY} for y")
