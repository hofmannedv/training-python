# -----------------------------------------------------------
# demonstrates finding the maximum value 
#o
# (C) 2024 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# importing the memory profiler library
from memory_profiler import profile

# instantiating the decorator
@profile
def findMax():
    # define a list of numbers
    numbers = [1, 3, 5, 6, 2] * 100000

    # apply max() to numbers
    print("The maximum element of the list is", max(numbers))

if __name__ == '__main__':
    findMax()
