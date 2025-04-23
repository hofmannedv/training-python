# -----------------------------------------------------------
# add two values, and output its sum
#o
# (C) 2014-2025 Frank Hofmann, Berlin/Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define two summands
op1 = 100
op2 = 50

# calculate the total sum
total = op1 + op2

# output the total sum
# in python 2.x: output is different (list vs. string)
# ('Total:', 100, '+', 50, '=', 150)
# Total: 100 + 50 = 150
#
# in python 3.x: output is similar in both cases
# Total: 100 + 50 = 150
# Total: 100 + 50 = 150
#
# ... using python-like syntax
print ("Total:", op1, "+", op2, "=", total)
#
# ... using C-like syntax
print ("Total: %i + %i = %i" % (op1, op2, total))
