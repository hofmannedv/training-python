# -----------------------------------------------------------
# solve the knapsack problem based on a sorted list, and
# recursion
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

def totalWeight(itemlist):
    """calculates the weight of all the items from the item list"""
    total = 0                          # assume: empty item list

    for item in itemlist:
        total = total + item["weight"]

    return total

def determineBestSelection(itemlist, transportLimit, alreadyInBag):
    """finds the best selection of items for the given transport limit
       best means: as many items as possible"""

    results = []                       # start with an empty list of results

    if len(itemlist):
        firstItem = itemlist.pop(0)
        remainingWeight = transportLimit - firstItem["weight"]
        if remainingWeight > 0:
            results = [firstItem] + determineBestSelection(itemlist, remainingWeight, alreadyInBag + 1)
        elif remainingWeight == 0:
            results = [firstItem]
    
    return results
                
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

# sort shopping list by size
shoppingList.sort(key=lambda x: x["weight"])

bestSolution = determineBestSelection(shoppingList, transportLimit, 0)
print("best solution for transport limit of %ig:" % transportLimit)
for item in bestSolution:
    print("%s (%ig)" % (item["name"], item["weight"]))
