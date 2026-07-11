# -----------------------------------------------------------
# Python Data Science examples
# Create an array with specific values
#
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# use pandas module under the local name pd
import pandas as pd

def colourize(value):
    """return a colour statement based on the value parameter"""
    colour = "red" if value < 0 else "green"
    return "color: %s" % colour

# define dataset as dataframe
dataset = {
    "column1" : [10, -5, 7],
    "column2" : [-3, 12, 8]
}
df = pd.DataFrame(dataset)

# apply colour per value
df.style.applymap(colourize)

# output dataframe
print(df)
