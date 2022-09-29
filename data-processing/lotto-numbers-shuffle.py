# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# create a shuffled array of lotto numbers

# use numpy module under the local name np
import numpy as np

# an array of numbers from 1 to 10
lottoNumbers = np.array([1,2,3,4,5,6,7,8,9,10])

# shuffle the numbers
np.random.shuffle(lottoNumbers)

# output the lotto numbers
print(lottoNumbers)
