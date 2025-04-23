# -----------------------------------------------------------
# Python Data Science examples
# demonstrate the power of aggregate functions
# (so-called universal functions)
#o
# (C) 2022-2025 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# follows the techniques as described in Haoyi's Programming Blog:
# http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
# -----------------------------------------------------------

# use numpy module under the local name np
import numpy as np

# define array of 10 elements
a = np.random.rand(10)
print(a)

# calculate the total
t = np.add.reduce(a)
print("sum of the elements:", t)

# multiply all the elements
t = np.multiply.reduce(a)
print("product of the elements:", t)

# store the intermediate results of the addition
t = np.add.accumulate(a)
print("intermediate results of the addition:", t)

# store the intermediate results of the multiplication
t = np.multiply.accumulate(a)
print("intermediate results of the multiplication:", t)

# determine the minimum, and the maximum value of the array
minimum = np.min(a)
maximum = np.max(a)
print ("The values range between %f, and %f" % (minimum, maximum))
