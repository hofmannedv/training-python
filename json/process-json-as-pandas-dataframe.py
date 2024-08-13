# Python Data Science examples
# (C) 2024 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# load a JSON data file into a Pandas dataframe

# use Pandas, and JSON module
import pandas as pd
import json

# define name of the JSON data file
data = "data.json"

# load data into dataframe
df = pd.read_json(data)

# sort dataframe by age, and output dataframe 
print(df.sort_values("Age"))
