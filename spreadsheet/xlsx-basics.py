# Demonstrate usage of OpenPyxl to store data an Excel sheet
# Excel spreadsheet
#
# (C) 2024 Frank Hofmann, Freiburg, Germany <info@efho.de>
# Published under GNU Public License (GPL)
#
# Inspired by examples from:
# https://realpython.com/openpyxl-excel-spreadsheets-python/

from openpyxl import Workbook

# define workbook, and switch to the active spreadsheet
workbook = Workbook()
spreadsheet = workbook.active

# set spreadsheet title
spreadsheet.title = "Example Data"

# store data in cells A1, and B1 (first rows of the first, and second column)
spreadsheet["A1"] = "hello"
spreadsheet["B1"] = "world!"

# store the file as hello_world.xlsx
workbook.save(filename="hello_world.xlsx")

