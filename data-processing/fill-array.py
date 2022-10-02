# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# create an array with specific values

# use numpy module under the local name np
import numpy as np

# a 5x5 array of float values filled with 10.25
# [[ 10.25  10.25  10.25  10.25  10.25]
#  [ 10.25  10.25  10.25  10.25  10.25]
#  [ 10.25  10.25  10.25  10.25  10.25]
#  [ 10.25  10.25  10.25  10.25  10.25]
#  [ 10.25  10.25  10.25  10.25  10.25]]
valueList = np.full((5, 5), 10.25)
print(valueList)

# a 5x5 array of integer values filled with 10
# [[10 10 10 10 10]
#  [10 10 10 10 10]
#  [10 10 10 10 10]
#  [10 10 10 10 10]
#  [10 10 10 10 10]]
valueList = np.full((5,5), 10, dtype='int')
print(valueList)


