# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# create an array of zeros

# use numpy module under the local name np
import numpy as np

# a zero-filled 2x2 array of float values
valueList = np.zeros((2, 2))
print(valueList)                # [[0.0, 0.0], [0.0, 0.0]]

# a zero-filled 2x2 array of integer values
valueList = np.zeros((2,2), int)
print(valueList)                # [[0, 0], [0, 0]]


