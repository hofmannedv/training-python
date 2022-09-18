# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# create an array of ones

# use numpy module under the local name np
import numpy as np

# a one-filled 2x2 array of float values
valueList = np.ones((2, 2))
print(valueList)                # [[1.0, 1.0], [1.0, 1.0]]

# a one-filled 2x2 array of integer values
valueList = np.ones((2,2), int)
print(valueList)                # [[1, 1], [1, 1]]


