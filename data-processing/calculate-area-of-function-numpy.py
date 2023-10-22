# -----------------------------------------------------------
# Python Data Science examples
# calculate the size of a trapezoid (area) using numpy
#o
# (C) 2022-2023 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

import numpy as np

def calculateListOfTrapezoids():
    """calculate the area for a list of data points"""

    x = [0.0, 1.0, 2.0, 3.0] 
    y = [2.0, 2.0, 2.5, 3.0]

    # initialize distance dx
    dx = 1

    # initialize the total size
    totalSize = 0.0

    # calculate size of area using trapz function from NumPy
    totalSize = np.trapz(y, dx=dx)

    return totalSize

print(calculateListOfTrapezoids())
