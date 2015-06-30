# -----------------------------------------------------------
# verify a stock file to check for re-orders
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import python modules
import csv,sys

# define order, reorder, and stock list
orderList = []
stockList = {}
reorderList = []

# read stock list from local database (csv file)

# define local database file
datafileName = "stock.txt"

lines = 0
with open(datafileName) as csvfile:
	# read the data from csv file, and store the fields in the product 	# list
	# the first line contains the names of the columns that are used as keys
	reader = csv.DictReader(csvfile)

	for row in reader:
		# read columns
		productBarcode, productCurrent, productReorder, productTarget = row["barcode"], row["current"], row["reorder"], row["target"]

		print (("reading: barcode, current, reorder, target: %s,%s,%s,%s") % (productBarcode, productCurrent, productReorder, productTarget))

		# create stock item
		stockList[productBarcode] = {
			"current": int(productCurrent),
			"reorder": int(productReorder),
			"target": int(productTarget),
		}

		# increase the line counter
		lines += 1

# output the number of lines read from database
print ("... read", lines, "lines")
#print (stockList)

# define order list with three orders
orderList = [
	[
		{"barcode":12345670, "quantity":2},
		{"barcode":12345687, "quantity":3}
	],
	[
		{"barcode":12345694, "quantity":1}
	],
	[
		{"barcode":12345717, "quantity":1},
		{"barcode":12345700, "quantity":5},
		{"barcode":12345724, "quantity":2}
	]
]

print (" ")

for currentOrder in orderList:
	# process order
	for item in currentOrder:
		productBarcode = str(item["barcode"])
		productQuantity = item["quantity"]

		print("%i x %s:" % (productQuantity, productBarcode))

		availableQuantity = stockList[productBarcode]["current"]
		remainingQuantity = availableQuantity - productQuantity
		if remainingQuantity > -1:
			print("requested: %i of %s" % (productQuantity,productBarcode))
			print("delivered: %i of %s" % (productQuantity,productBarcode))
			stockList[productBarcode]["current"] = remainingQuantity
		else:
			print("requested: %i of %s" % (productQuantity,productBarcode))
			print("delivered: %i of %s" % (availableQuantity,productBarcode))
			stockList[productBarcode]["current"] = 0
		
			# adjust reorder list

		print (" ")

# analyze stock list and initiate an re-order
barcodeList = stockList.keys()

for productBarcode in barcodeList:

	currentValue = stockList[productBarcode]["current"]
	reorderValue = stockList[productBarcode]["reorder"]
	targetValue = stockList[productBarcode]["target"]

	if currentValue < reorderValue:
		reorderEntry = {
			"barcode": productBarcode,
			"reorder": targetValue - currentValue
		}

		reorderList.append(reorderEntry)

# prepare the content of the output file
outputfileContent = []
outputfileContent.append("-" * 40)
outputfileContent.append(" items to be reordered:")
outputfileContent.append("-" * 40)

for item in reorderList:
	outputfileContent.append("%5i x %s" % (item["reorder"], item["barcode"]))

outputfileContent.append("-" * 40)

# write to file
fileHandle = open("reorder.txt", "w")

# line by line
for line in outputfileContent:
	# display output
	print (line)
	# write to file
	fileHandle.write(line + "\n")

# close file
fileHandle.close()


