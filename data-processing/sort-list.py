# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# create a sorted list

# use numpy module under the local name np
import numpy as np

# define unsorted list of integers, and an empty sortedList
numbers = [6, 41, 12, 3, 8]
sortedList = []

for entry in numbers:
    # calculate the insert position
    newPosition = np.searchsorted(sortedList, entry)

    # insert the value
    sortedList.insert(newPosition, entry)

    print("sorted list:", sortedList)
