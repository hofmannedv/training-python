# Demonstrate usage of OpenPyxl to store data an Excel sheet
# Excel spreadsheet
#
# (C) 2024 Frank Hofmann, Freiburg, Germany <info@efho.de>
# Published under GNU Public License (GPL)
#
# Inspired by examples from:
# https://realpython.com/openpyxl-excel-spreadsheets-python/

from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"

workbook.save(filename="hello_world.xlsx")

