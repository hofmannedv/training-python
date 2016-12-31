# -----------------------------------------------------------
# deepthought_setup.py -- setup module to create extensions
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
from distutils.core import setup, Extension

# define module sources
moduleSources = ['deepthought.c', 'deepthought_wrap.c']

# define module description
deepthoughtModule = Extension('_deepthought', sources = moduleSources, )

# set detailed module description
setup (name        = 'deepthought',
       version     = '0.1',
       author      = 'Farid Hajji/Frank Hofmann',
       description = 'complex example module',
       ext_modules = [deepthoughtModule],
       py_modules  = ["deepthought"]
)
