# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# create an array, and measure the time to fill it both with, and
# without an function call

# use numpy module under the local name np
import numpy as np

# use timeit module
import timeit

def add(a,b):
    return a + b

# define the two datasets
x = np.zeros(1000)
y = np.zeros(1000)

# define timer with code to be run: function call
t = timeit.Timer(
    'for i in range(len(x)): x[i] = add(i, i+1)', \
    setup='from __main__ import add, x'
)

# run code 10000 times
xTime = t.timeit(10000)
print('Time, function call: {:g} seconds'.format(xTime))

# define timer with code to be run: no function call
t = timeit.Timer(
    'for i in range(len(y)): y[i] = i + (i+1)', \
    setup='from __main__ import add, y'
)

# run code 10000 times
yTime = t.timeit(10000)
print('Time, without function call: {:g} seconds'.format(yTime))
