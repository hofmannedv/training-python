# -----------------------------------------------------------
# example.py -- example program that uses the deepthought module
#
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# idea and source code based on:
# Farid Hajji: Das Python Praxisbuch, Addison-Wesley, 2008, 
# ISBN 978-3-8273-2543-3
# -----------------------------------------------------------

# import external modules
import deepthought

# call the answer function from the deepthought module
a = deepthought.answer()

# print answer
print ("the answer is %i" % a)
