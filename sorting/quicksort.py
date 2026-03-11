# -----------------------------------------------------------
# sort a list using Quicksort
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

def quicksort(data):
    """sort data using Quicksort algorithm"""
    print("sorting", data)

    if len(data) < 2:
        # data contains less than two elements
        # no further sorting necessary
        return data

    # detect middle element
    position = len(data) // 2

    # define three lists to separate the data in relation to 
    # the middle element
    leftData = []
    middleData = []
    rightData = []

    # go though the data
    for currentValue in data:
        if currentValue < data[position]:
            leftData.append(currentValue)
        if currentValue > data[position]:
            rightData.append(currentValue)
        if currentValue == data[position]:
            middleData.append(currentValue)

    # sort left list (numbers lower than middle position
    sortedLeft = quicksort(leftData)
         
    # sort right list (numbers higher than middle position
    sortedRight = quicksort(rightData)
         
    # combine the sorted sub-lists
    sortedData = sortedLeft + middleData + sortedRight

    return sortedData

data = [34, 12, 67, 55, 10]
result = quicksort(data)
print(data, "->", result)

