# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# create a list of equally distributed values within a value range

# use numpy module under the local name np
import numpy as np

# value range from 2.0 to 3.0 (inclusive)
# 11 float values
valueList = np.linspace(2.0, 3.0, 11)
print(valueList)                # 2.0, 2.1, ... 3.0

# value range from 10 to 100 (inclusive)
# 10 float values
valueList = np.linspace(10, 100, 10)
print(valueList)                # 10.0, 20.0, ... 100.0

# value range from 10 to 100 (inclusive)
# 10 integer values
valueList = np.linspace(10, 100, num=10, dtype=int)
print(valueList)                # 10, 20, ... 100

# value range from 10 to 100 (without the end point)
# 10 integer values
valueList = np.linspace(10, 110, num=10, dtype=int, endpoint=False)
print(valueList)                # 10, 20, ... 100
