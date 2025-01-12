# -----------------------------------------------------------
# demonstrates how to use a pool of threads with the help of
# the ThreadPool class provided by the multiprocessing 
# library, and do calculations
#
# idea taken from this tutorial:
# https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread
#
# (C) 2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# include standard modules
from multiprocessing.pool import ThreadPool

def square(x):
    # calculate the square of the value of x
    return x*x

if __name__ == '__main__':

    # define the dataset
    dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print ("dataset:", dataset)

    # define result as empty list
    result = []

    # run this with a pool of 5 agents 
    agents = 5
    chunksize = 3

    with ThreadPool(agents) as pool:
        for i in pool.map(square, dataset, chunksize):
            result.append(i)

    print ("result:", result)
