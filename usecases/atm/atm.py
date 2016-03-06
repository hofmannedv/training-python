# -----------------------------------------------------------
# find the atm with the lowest rate from a list of atms
#
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# developed as part of the AtmFinder/OptiCash project during
# the SIX Hackathon Zurich, March 4-6, 2016
#
# -----------------------------------------------------------

def getATMsData():
	# deliver the ATM data
	# nearly-fictional Zurich-based ATMs
	data = {
		'Credit Suisse ATM': {'visa': 0.06, 'maestro': 0.03, 'mastercard': 0.015},
		'Postman KV Business School': {'visa': 0.07, 'maestro': 0.04, 'mastercard': 0.03},
		'ZKB ATM': {'visa': 0.06, 'maestro': 0.02, 'mastercard': 0.03},
		'Postmat Swisscom Businesspark': {'visa': 0.06, 'maestro': 0.04, 'mastercard': 0.03},
		'Postmat Einkaufszentrum Puls5': {'visa': 0.08, 'maestro': 0.02, 'mastercard': 0.03},
		'UBS - Bancomat': {'visa': 0.09, 'maestro': 0.04, 'mastercard': 0.03},
		'Raiffeisen': {'visa': 0.09, 'maestro': 0.04, 'mastercard': 0.03}
	}
	
	return data

def getATMColour(atmValue, minimum, maximum):
	colour = "red"		# default return value
	
	if atmValue == -1:
		colour = "black"	# no information
	else:
		# calculate the segment markers
		delta = (maximum - minimum) / 3
		m1 = minimum + delta
		m2 = maximum - delta
		
		if atmValue < m2:
			colour = "orange"
		if atmValue < m1:
			colour = "green"
	
	return colour

def evaluateATM(card,atm):
	value = -1 # set default value: not available
	
	if card in atm.keys():
		# retrieve specific value for the card on that ATM
		value = atm[card]
	
	# return the value
	return value

def evaluateAllATMs(card):
	# get all ATM data
	atmsData = getATMsData()
	
	minimum = 1
	maximum = 0
	
	# loop for all ATMs to calculate the minimum and maximum fee
	for atm in atmsData:
		value = evaluateATM(card,atmsData[atm])
		
		if value > -1:
			if value < minimum: minimum = value
			if value > maximum: maximum = value
		
	# loop for all ATMs
	resultList = []
	for atm in atmsData:
		# evaluate this ATM
		value = evaluateATM(card,atmsData[atm])
		
		# calculate the marker's colour
		colour = getATMColour(value, minimum, maximum)
		
		# setup the output entry
		atmEntry = [atm,value,colour]
		
		# add the output entry to the result list
		resultList.append(atmEntry)
		
	# sort the result list by the fee value (2nd column)
	sortedList = sorted(resultList, key = lambda x: float(x[1]))
	return sortedList

# === MAIN ===

# define the cards
cards = {"maestro", "visa", "mastercard", "paypal"}

for currentCard in cards:
	# calculate the results for all ATMs in the list
	resultList = evaluateAllATMs(currentCard)
	
	print ("card: %s" % (currentCard))
	
	# assume that we have one "best" ATM
	bestATM = resultList[0]
	atmName = bestATM[0]
	atmRate = bestATM[1]
	
	if atmRate == -1:
		print("not accepted by an ATM from the list")
	else:
		# maybe we have more than one: check the list
		for atm in resultList:
			if atmRate == atm[1]:
				atmName = atm[0]
				print ("name: %s - rate: %s" % (atmName,atmRate))
			else:
				break
	
	print ("")

