# -----------------------------------------------------------
# demonstrates how to generate fake names using the faker module
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# import Faker class
from faker import Faker

# generate a Faker object
fake = Faker()

number = 1
while number < 11:
    newName = fake.name()
    print(f"{number:2d} {newName}")
    number = number + 1
