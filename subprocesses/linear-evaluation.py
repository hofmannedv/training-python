# -----------------------------------------------------------
# demonstrates running a function (sub) on a dataset in
# linear order
#
# (C) 2017-2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

def square(x):
    # calculate the square of the value of x
    return x*x

if __name__ == '__main__':

    # define a dataset of 50 numbers
    dataset = range(500)

    result = []
    for i in dataset:
        result.append(square(i))

    for i in result:
        pass
        #print (i)
