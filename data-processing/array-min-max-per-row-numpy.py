# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# demonstrate the power of aggregate functions
# (so-called universal functions)
# determine the minimum, and maximum value per row, and column

# use numpy module under the local name np
import numpy as np

# define array of 10 elements
a = np.random.randint(20, size=(3, 4))
print("randomly computed values:")
print(a)

# determine the minimum, and the maximum values per column
minimumValues = a.min(axis=0)
maximumValues = a.max(axis=0)
print("minimum values per column:", minimumValues)
print("maximum values per column:", maximumValues)

# determine the minimum, and the maximum values per row
minimumValues = a.min(axis=1)
maximumValues = a.max(axis=1)
print("minimum values per row:", minimumValues)
print("maximum values per row:", maximumValues)
