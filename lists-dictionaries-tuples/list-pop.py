# -----------------------------------------------------------
# demonstrates how to use a list as a stack
#o
# (C) 2015-2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define list (stack)
stack = [3, 7, 12, 15]
print("original stack:", stack)

# retrieve the last item from the list using pop() in an endless loop
while True:
    try:
        # pop last element
        # retrieve the element
        value = stack.pop()
        print("taken from stack:", value)
        print("current stack:", stack)
    except:
        # list is empty -- we cannot take more elements
        print("at the end of list")
        break
