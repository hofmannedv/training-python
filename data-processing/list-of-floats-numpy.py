# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# create a list of float values

# use numpy module under the local name np
import numpy as np

# define a list of mixed data types
# all elements in an np.array have to have the same data type
# numpy will upcast them to float values
valueList1 = np.array([1, 2.0, 3, 4, 5])
print(valueList1)                # [1.0, 2.0, 3.0, 4.0, 5.0]

# define a list, and set the data type explicitly
valueList2 = np.array([1, 2, 3, 4, 5], dtype='float32')
print(valueList2)                # [1.0, 2.0, 3.0, 4.0, 5.0]

