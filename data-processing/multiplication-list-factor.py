# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# multiply the elements of a list with the same factor
# example: net value, calculate sales tax, and corresponding gross value

# use numpy module under the local name np
import numpy as np

# define net values
netValues = np.array([1500.00, 270.00, 345.00])

# define sales tax 
salesTax = 0.15

# calculate sales tax to be added to the net values
addedTax = netValues * salesTax
grossValues = netValues + addedTax

print(grossValues)
