# -----------------------------------------------------------
# Python Data Science examples
# (C) 2025 Frank Hofmann, Germany 
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# calculate the square root sum for a list of integers
#
# inspired by code for multiple cores by Jason Brownlee:
# How to Use 100% of All CPU Cores in Python
# https://superfastpython.com/python-use-all-cpu-cores/
# -----------------------------------------------------------

import math
from multiprocessing import Pool
 
# define a cpu-intensive task
def task(arg):
    result = sum([math.sqrt(i) for i in range(1, arg)])
    print(f"{arg}: {result}")
    return result
 
# main program
if __name__ == '__main__':
    # report a message
    print('Starting task...')

    # create the process pool for 8 cpu cores
    with Pool(8) as pool:
        # perform calculations
        results = pool.map(task, range(1,5))
        print (results)

    # report a message
    print('Done.')
