# Python Data Science examples
# (C) 2022 Frank Hofmann <frank.hofmann@efho.de>
# License: GNU Public License (GPL)

# sort a list by two keys

# use numpy module under the local name np
import numpy as np

# define data type
datatype = [
    ('name', 'S10'),      # 10 characters
    ('maxspeed', int),    # integer
    ('numberplate', 'S8') # 8 characters
]

# define a list 
values = [
    ('Audi A4', 160, 'CA144534'),
    ('Ford Ka', 145, 'CA285137'),
    ('VW Polo', 145, 'CA671123')
]

# define data array
a = np.array(values, dtype=datatype)

# sort by numberplate
sortedByNumberplate = np.sort(a, order='numberplate')
print(sortedByNumberplate)

# sort by speed, first, and by name, next
sortedBySpeedAndName = np.sort(a, order=['maxspeed', 'name'])
print(sortedBySpeedAndName)
