# -----------------------------------------------------------
# demonstrates the usage of a for loop to interate through a list
# of items in a shopping cart
#o
# (C) 2014 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define list
shoppingCart = [
	{"description": "banana", "amount": 1, "price": 3.0},
	{"description": "apple", "amount": 2, "price": 1.50},
	{"description": "grapefruit", "amount" : 4, "price": 0.66}
]

# initiate total
total = 0.0
items = 0

# output list content
for item in shoppingCart:
	description = item["description"]
	amount = item["amount"]
	price = item["price"]

	items += amount
	subtotal = amount * price
	total += subtotal

	print (amount, description, price, "(", subtotal, ")")

print ("-------------------------------")
print ("total:", total)

