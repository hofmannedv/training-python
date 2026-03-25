# -----------------------------------------------------------
# calculate the number of days between timestamps
#o
# (C) 2019-2026 Frank Hofmann, Besancon/Freiburg, France
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# import standard modules
from datetime import date

firstTimestamp = date(2019, 1, 15)
lastTimestamp = date(2019, 4, 15)
numberOfDays = lastTimestamp - firstTimestamp
print("number of days between 2019-01-15 and 2019-04-15:", numberOfDays)
