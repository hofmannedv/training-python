# -----------------------------------------------------------
# Python Data Science examples
# (C) 2025 Frank Hofmann, Germany 
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# calculate random 2d data points, and store them in a file 
# points.data as two values per line separated by comma (pickle format)
# -----------------------------------------------------------

import random
import pickle

if __name__ == '__main__':

    # define number of data points
    number = 500

    # define output file
    outputFile = "points.data"

    # define cloud of points as a list of tuples
    points = [(int(random.random()*50), int(random.random()*50)) for value in range(number)]

    with open(outputFile, 'wb') as fp:
        pickle.dump(points, fp)

    # print dumped points
    print(points)
