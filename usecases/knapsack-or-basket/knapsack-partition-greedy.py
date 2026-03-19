# -----------------------------------------------------------
# solve the knapsack problem by dividing the items equally 
# between the participants according to the article's weights. 
# Based on a greedy approach.
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

def distributeItemsEqually(shoppingList, people=["buyer 1", "buyer 2"]):
    """distribute the items equally between the buyers, based on weight"""

    if people == []:
        # shopping list cannot be distributed: no buyers
        return None

    # define baskets per buyer
    results = []
    for buyer in people:
        newBuyer = {"name": buyer, "shoppingList": []}
        results.append(newBuyer)

    if len(people) == 1:
        # no need to distribute the shopping list: just a single buyer
        newBuyer = results[0]
        newBuyer["shoppingList"] = shoppingList
        results = [newBuyer]
        return results

    if not len(shoppingList):
        # shopping list cannot be divided: is empty
        return results

    # sort items list by weight in descending order
    shoppingList.sort(key=lambda x: x["weight"], reverse=True)
    print("sorted shopping list:", shoppingList)

    # divide items equally
    for article in shoppingList:
        articleWeight = article["weight"]
        print("processing %s ..." % article["name"])

        compareWeight = -1
        chosenBuyer = None
        for buyer in results:
            basket = buyer["shoppingList"]
            basketWeight = totalWeight(basket)

            if compareWeight < 0:
                compareWeight = basketWeight
                chosenBuyer = buyer

            if basketWeight < compareWeight:
                compareWeight = basketWeight
                chosenBuyer = buyer

        # update basket
        print("extend shopping list for %s ..." % chosenBuyer["name"])
        basket = chosenBuyer["shoppingList"]
        basket.append(article)
        chosenBuyer["shoppingList"] = basket

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

distribution = distributeItemsEqually(shoppingList, ["John", "Alfred", "Martha"])

for buyer in distribution:
    name = buyer["name"]
    basket = buyer["shoppingList"]
    print(" ")
    print("Shopping list for %s" % name)
    for article in basket:
        print("%s (%ig)" % (article["name"],article["weight"]))
