# -----------------------------------------------------------
# solve the knapsack problem with the help of combinations
# using the itertools module
#o
# see: Knapsack Problem Algorithm (Wikipedia)
# https://en.wikipedia.org/wiki/Knapsack_problem
#
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

from itertools import combinations

def totalWeight(itemlist):
    """calculates the weight of all the items from the item list"""
    total = 0                          # assume: empty item list

    for item in itemlist:
        total = total + item["weight"]

    return total

def isWithinTransportLimit(itemlist, transportLimit):
    """takes an item list, and returns True if the total weight 
       is within the transport limit"""

    weight = totalWeight(itemlist)
    return weight <= transportLimit

def determineBestSelection(itemlist, transportLimit):
    """finds the best selection of items for the given transport limit
       best means: as many items as possible"""

    results = []                       # start with an empty list of results

    # determine all the possible solutions starting with a single item
    for run in range(1, len(itemlist) + 1):
        for currentTestCase in combinations(itemlist, run):
            basket = list(currentTestCase)
            if isWithinTransportLimit(basket, transportLimit):
                results.append(currentTestCase)

    # analyze the solutions
    numberOfItems = 0                  # assume: no items
    bestKnapsack = None                # assume: no solution

    for solution in results:
        if len(solution) > numberOfItems:
            bestKnapsack = solution    # found a new selection with more items

    return bestKnapsack    

# define item list as follows:
# 2x cucumber, 400g each
# 2x joghurt, 500g each
# 1x chocolate, 85g
# 1x icecream, 1000g

shoppingList = [
    {"id": 1, "name": "cucumber", "weight": 400},
    {"id": 1, "name": "cucumber", "weight": 400},
    {"id": 2, "name": "joghurt", "weight": 500},
    {"id": 2, "name": "joghurt", "weight": 500},
    {"id": 3, "name": "chocolate", "weight": 85},
    {"id": 4, "name": "icecream", "weight": 1000}
]

# calculate the total of the shopping list
total = totalWeight(shoppingList)
print("total weight of the shopping list: %ig" % total)

# define transport limit
transportLimit = 2000                  #  2000g, or 2kg

bestSolution = determineBestSelection(shoppingList, transportLimit)
print("best solution for transport limit of %ig:" % transportLimit)
for item in bestSolution:
    print("%s (%ig)" % (item["name"], item["weight"]))
