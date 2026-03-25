# -----------------------------------------------------------
# compare timestamps
#o
# (C) 2019-2026 Frank Hofmann, Besancon/Freiburg
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# import standard modules
import datetime

today = datetime.datetime.today()
oneDay = datetime.timedelta(days=1)
yesterday = today - oneDay
tomorrow = today + oneDay

timestampList = [yesterday, today, tomorrow]
now = datetime.datetime.now()

for entry in timestampList:
  if entry < now:
    print("timestamp is before now:        ", entry, "-", now)
  elif entry > now:
    print("timestamp is after now:         ", now, "-", entry)
  else:
    print("timestamp is exactly right now: ", now, "-", entry)
