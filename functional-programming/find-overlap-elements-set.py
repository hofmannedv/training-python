# -----------------------------------------------------------
# demonstrates finding similar elements in a list using a 
# set, and the union operator
#o
# (C) 2024 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

ListeA = [1,2,3,4,5] * 1000
ListeB = [2,3,4,5,6] * 1000

overlaps = set(ListeA) & set(ListeB)

print(overlaps)

