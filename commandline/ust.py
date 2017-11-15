#!/usr/bin/python

"""Usage:
    ./ust.py <value>
    ./ust.py -t <percentage> <value>
    ./ust.py --tax=percentage <value>
   
   Options:
    -t <percentage> <value> --tax=<percentage> <value>  calculate tax [default: 19]
"""

# include docopt module
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print (arguments)
    
    value = int(arguments["<value>"])
    percentage = int(arguments["--tax"])
    tax = value * percentage / 100
    print("the %i percent tax for %i is %.2f" % (percentage, value,tax))
