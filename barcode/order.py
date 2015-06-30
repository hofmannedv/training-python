# -----------------------------------------------------------
# enter a barcode to order an item from a list of products
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import python modules
import barcode,csv

# define order, and product list
orderList = []
productList = {}

# read product list from local database (csv file)

# define local database file
datafileName = "database.txt"

lines = 0
with open(datafileName) as csvfile:
	# read the data from csv file, and store the fields in the product 	# list
	# the first line contains the names of the columns that are used as keys
	reader = csv.DictReader(csvfile)

	for row in reader:
		# read columns
		productBarcode, productDescription, productPrice = row["barcode"], row["description"], float(row["price"])

		print (("reading: barcode, description, price: %s,%s,%s") % (productBarcode, productDescription, productPrice))

		# create product item
		productList[productBarcode] = {
			"description": productDescription,
			"price": float(productPrice)
		}

		# increase the line counter
		lines += 1

# output the number of lines read from database
print ("... read", lines, "lines")

# loop as long as the user quits the program
while True:
	# assume a total of 0
	total = 0.00

	# display current order
	# - header
	print("your order consists of the following items:")
	print("-" * 70)
	print("%10s %40s %3s %5s %5s" % ("barcode", "description", "qty", "price", "total"))
	print("-" * 70)
	for item in orderList:
		productBarcode = item["barcode"]
		productQuantity = item["quantity"]
		productDescription = productList[productBarcode]["description"]
		productSinglePrice = productList[productBarcode]["price"]
		productTotalPrice = productQuantity * productSinglePrice

		# - item details	
		print("%10s %40s %3i %5s %5.2f" % (productBarcode, productDescription, productQuantity, productSinglePrice, productTotalPrice))

		# calculate the total
		total += productTotalPrice

	# - footer
	print("-" * 70)
	print("total cost of order: %5.2f" % total)
	print("-" * 70)

	# wait for user input
	print(" ") 
	action = input("your next action -- enter a new barcode, or type Q to quit: ")

	# validate action
	action = action.strip()

	if action in ("q", "Q"):
		# user wants to quit, so exit the loop.
		break

	# interpret action as new barcode
	productBarcode = action

	# validate barcode
	if barcode.validateBarcode(productBarcode):

		# retrieve the list of barcodes from the product list
		barcodeList = productList.keys()
		if productBarcode in barcodeList:

			# retrieve the product description
			productDescription = productList[productBarcode]["description"]
			productQuantity = input("enter quantity for %s: " % productDescription)

			# remove whitespaces and trailing characters
			productQuantity = float(productQuantity.strip())

			if len(orderList) == 0:
				orderList = [{"barcode": productBarcode, "quantity": productQuantity}]
			else:
				# assume that we did not update the item, yet
				updated = False

				# is the ordered item already in the basket?
				for i in range(len(orderList)):
					currentItem = orderList[i]
					if currentItem["barcode"] == productBarcode:
						# item was discoverd -- so increase the quantity
						orderList[i]["quantity"] += productQuantity

						# item was updated
						updated = True

						# quit the for loop
						break

				# the ordered item is still not in our list, so just add it
				if not updated:
					# create a new list entry
					currentItem = {"barcode": productBarcode, "quantity": productQuantity}

					# append it to the order list
					orderList.append(currentItem)

		else:
			# display error message
			print ("there is no product with this barcode")
			print (" ")
	else:
		# display error message
		print ("the entered barcode is invalid:", productBarcode)
		print (" ")


