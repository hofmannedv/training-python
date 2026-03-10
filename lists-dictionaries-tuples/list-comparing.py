# -----------------------------------------------------------
# demonstrates how to compare lists element by element
#o
# (C) 2015-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# NOTE: works for Python 2.x, only
# cmp function removed in Python 3.x

# define three lists
numbers1 = [23, 61, 82]
numbers2 = [1, 155, 17]
numbers3 = [61, 23, 82]
numbers4 = [23, 61, 82]

# output dictionary content (key-value-pairs)
print (numbers1)
print (numbers2)
print (numbers3)
print (numbers4)

# compare the lists
# list 1 and 2 (returns 1: greater than)
print(cmp(numbers1, numbers2))
# list 1 and 3 (returns -1: lower than)
print(cmp(numbers1, numbers3))
# list 2 and 3 (returns -1: lower than)
print(cmp(numbers2, numbers3))
# list 1 and 4 (returns 0: equal)
print(cmp(numbers1, numbers4))
