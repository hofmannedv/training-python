# -----------------------------------------------------------
# demonstrates how to run two functions in parallel using the
# multiprocessing library
#
# idea taken from this post:
# https://stackoverflow.com/questions/7207309/python-how-can-i-run-python-functions-in-parallel
#o
# (C) 2017-2025 Frank Hofmann, Berlin, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# include standard modules
from multiprocessing import Process
import os

def func1(cycles):
  print ('func1: starting with %i cycles' % cycles)
  for i in range(cycles): pass
  print ('func1: finishing')

def func2(cycles):
  print ('func2: starting with %i cycles' % cycles)
  for i in range(cycles): pass
  print ('func2: finishing')

if __name__ == '__main__':
  # getting the process ids
  print('parent process: %i' % os.getppid())
  print('process id: %i' % os.getpid())

  # initialising two processes, and starting p1, and p2
  p1 = Process(target=func1, args=(500000,))
  p1.start()
  p2 = Process(target=func2, args=(200000,))
  p2.start()

  # wait for terminating p1 and p2
  p1.join()
  p2.join()

