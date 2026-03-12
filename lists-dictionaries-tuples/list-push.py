# -----------------------------------------------------------
# demonstrates how to push items to the end of a list
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define list (amounts)

article1 = {"number": 43, "amount": 2}
article2 = {"number": 45, "amount": 6}
article3 = {"number": 41, "amount": 3}

order = [article1, article2, article3]
packageList = []
for article in order:
    number = article["number"]
    amount = article["amount"]
    while amount > 0:
        newArticle = {"number": number, "amount": 1}
        packageList.append(newArticle)
        amount = amount - 1

print(packageList)

itemsPerParcel = 5
parcelList = []
articlesPerParcel = []
while len(packageList):
    article = packageList.pop(0)
    articlesPerParcel.append(article)
    if len(articlesPerParcel) == itemsPerParcel:
       parcelList.append(articlesPerParcel)
       articlesPerParcel = []

if len(articlesPerParcel):
    parcelList.append(articlesPerParcel)

print(parcelList)
