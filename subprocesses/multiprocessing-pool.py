# -----------------------------------------------------------
# demonstrates how to run a pool of functions in parallel 
# using the multiprocessing library, and do calculations
#
# idea taken from this tutorial:
# https://docs.python.org/3/library/multiprocessing.html
#
# (C) 2017-2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# include standard modules
from multiprocessing import Pool

def square(x):
    # calculate the square of the value of x
    return x*x

if __name__ == '__main__':

    # define the dataset
    dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print ("dataset:")
    print (dataset)

    # run this with a pool of 5 agents having a chunksize of 3 until finished
    agents = 5
    chunksize = 3
    with Pool(agents) as p:
        result = p.map(square, dataset, chunksize)

    print ("result:")
    print (result)
