# -----------------------------------------------------------
# implementation of "Too much milk" problem using two threads
# with synchronisation
#o
# (C) 2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define basic module
from threading import Thread
import random, time

# define the availability of milk in the fridge as a global 
# variable: milk is not there
milk = False

# define processing the task "buying milk" as a global variable
# define task as "is not taken, yet"
taskBuyingMilkOpen = True

def buyMilk(threadName):
    '''execute the task: buy milk'''

    global milk
    global taskBuyingMilkOpen

    print("[%s] checking for milk in the fridge ... " % (threadName))
    print("[%s] status of milk: " % (threadName), milk)
    if not milk:
        print("[%s] checking for task still being open ... " % (threadName))
        print("[%s] status of task: " % (threadName), taskBuyingMilkOpen)
        if taskBuyingMilkOpen:
            taskBuyingMilkOpen = False
            print("[%s] buying milk ... " % (threadName))
            pause = random.random()
            time.sleep(pause)
            print("[%s] bought milk" % (threadName))
    return

# define thread 1
thread1 = Thread(target=buyMilk, args=(1,))
thread1.start()

# define thread 2
thread2 = Thread(target=buyMilk, args=(2,))
thread2.start()

# end thread 1 and 2
thread1.join()
thread2.join()
