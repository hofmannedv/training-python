# -----------------------------------------------------------
# implementation of "Too much milk" problem using two threads
# and a lock
#o
# (C) 2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define basic module
from threading import Thread
from threading import Lock
import random, time

# define the availability of milk in the fridge as a global 
# variable: milk is not there
milk = False

# define a lock so that processing the task "buying milk" 
# can be executed by a single thread, only
lock = Lock()

def buyMilk(threadName):
    '''execute the task: buy milk'''

    global milk
    global lock

    print("[%s] checking for milk in the fridge ... " % (threadName))
    print("[%s] status of milk: " % (threadName), milk)
    with lock:
        print("[%s] taking the task (locked) ... " % (threadName))
        if not milk:
            print("[%s] buying milk ... " % (threadName))
            pause = random.random()
            time.sleep(pause)
            print("[%s] bought milk" % (threadName))
            milk = True
        else:
            print("[%s] no need to buy milk" % (threadName))
        print("[%s] task done (unlocked)" % (threadName))
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
