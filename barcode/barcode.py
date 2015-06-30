# -----------------------------------------------------------
# python module to evaluate barcodes
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import standard modules
import re

def validateBarcode(barcode):

	# set default value: assume False
	valid = False

	# convert to string in case we get an integer value
	barcodeString = str(barcode)

	# test formal criteria
	# - test for the length of 8 characters
	if not len(barcodeString) == 8:
		return valid

	# - test for eight digits using a regular expression
	pattern = "^\d{8}$"
	rePattern = re.compile(pattern)

	# check for pattern
	if re.match(rePattern, barcodeString):

		# set default barcode sum
		barcodeSum = 0

		# go through position 0 to 6 of the barcode string
		for position in range(7):

			# retrieve according barcode number
			barcodeNumber = int(barcodeString[position])

			# even numbers are added three times, otherwise just once
			if position % 2 == 0:
				barcodeSum += barcodeNumber * 3
			else:
				barcodeSum += barcodeNumber

		# calculate validation bit according to the validation algorithm
		validationBit = ((barcodeSum // 10) + 1) * 10 - barcodeSum

		# compare validation bit with the 8th number of the barcode
		if validationBit == int(barcodeString[7]):
			valid = True

	return valid

# test the module functions
if __name__ == "__main__":

	# assume a list of barcodes
	barcodeList = ["13245627", "14677231", "94433714", "1234"]

	# got through the list, and validate each entry
	for barcode in barcodeList:
		if validateBarcode(barcode):
			print ("barcode %s is valid" % barcode)
		else:
			
			print ("barcode %s is not valid" % barcode)

