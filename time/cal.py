# -----------------------------------------------------------
# display a calendar for the current month
#o
# (C) 2019-2026 Frank Hofmann, Besancon/Freiburg
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# import required calendar module
import calendar

cal = calendar.month(2019, 4)
print ("Here is the calendar:")
print (cal)
