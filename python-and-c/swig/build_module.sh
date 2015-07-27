#!/bin/sh

# -----------------------------------------------------------
# shell script to compile the _deepthought.so module
#
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
#
# idea and source code based on:
# Farid Hajji: Das Python Praxisbuch, Addison-Wesley, 2008, 
# ISBN 978-3-8273-2543-3
# -----------------------------------------------------------

# create interface file using swig
swig -python deepthought.i

# compile _deepthought.so module
python deepthought_setup.py build_ext --inplace
