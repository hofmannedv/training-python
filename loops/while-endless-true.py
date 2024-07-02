# -----------------------------------------------------------
# demonstrates the usage of an endless while loop using True 
# to interate through a list
#o
# (C) 2024 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list
shoppingCart = ["banana", "apple", "grapefruit", "peach"] * 1000000

# initiate index
itemIndex = 0

while True:
    if itemIndex < len(shoppingCart):
        print (itemIndex, shoppingCart[itemIndex])
        # increment itemIndex
        itemIndex += 1
    else:
        break
