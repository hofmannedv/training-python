# -----------------------------------------------------------
# demonstrates how to use hash functions:
# calculate sha256 hash for the contents of a file
#o
# (C) 2025 Frank Hofmann, Berlin/Freiburg, Germany
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# 
# inspired by this post on Stack Overflow:
# https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
# -----------------------------------------------------------

# import required Python modules
import sys
import hashlib

# define buffer size
bufferSize = 65536  # use chunks of 64kb

# initialize the SHA256 function
sha256 = hashlib.sha256()

# read file given as first parameter
with open(sys.argv[1], 'rb') as f:
    while True:
        # read data from file into buffer
        data = f.read(bufferSize)
        if not data:
            break

        # update calculated hash value
        sha256.update(data)

# output final hash
print("SHA256: {0}".format(sha256.hexdigest()))
