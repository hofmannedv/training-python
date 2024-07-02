# -----------------------------------------------------------
# demonstrates finding similar elements in a list using a 
# for loop
#o
# (C) 2024 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

ListeA = [1,2,3,4,5] * 1000
ListeB = [2,3,4,5,6] * 1000
overlaps = []

for x in ListeA:
  for y in ListeB:
    if x==y:
      overlaps.append(x)

print(overlaps)

