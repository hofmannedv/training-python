# -----------------------------------------------------------
# demonstrates how to generate fake employee data using the faker module
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# 
# inspired by this article:
# Bala Priya C: Pandas vs. Polars: A Complete Comparison of Syntax, Speed, and Memory
# https://www.kdnuggets.com/pandas-vs-polars-a-complete-comparison-of-syntax-speed-and-memory
# -----------------------------------------------------------

# import faker, and random module
from faker import Faker
import random

# generate a Faker object
fake = Faker()

# define some more randomness
random.seed(42)

numberOfEmplyees = 10

data = []
for i in range(numberOfEmplyees):
  dataset = {
    "userId": i,
    "name": fake.name(),
    "email": fake.email(),
    "salary": random.randint(30000, 100000),
    "department": random.choice(['Engineering', 'Sales', 'Marketing', 'HR', 'Finance'])
  }
  data.append(dataset)

for entry in data:
    userId = entry["userId"]
    name = entry["name"]
    email = entry["email"]
    salary = entry["salary"]
    department = entry["department"]
    print(f"{userId:2d} {name:<25} {email:<25} {salary:6d} {department:<20}")
