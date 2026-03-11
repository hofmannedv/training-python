# -----------------------------------------------------------
# Python Data Science examples
# Create an array with specific values
#
# (C) 2022-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

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

