# -----------------------------------------------------------
# basic implementation of multi-threading
#o
# (C) 2019-2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# define basic module
import threading, random, time

def myCalculator(threadName, value):
    "do the calculation as a separate thread"
    pause = random.random()
    time.sleep(pause)
    print("[%s] the square of %i is %i" % (threadName, value, value * value))
    return

items = [55, 75, 30, 4, 25]
threads = []

for threadId in range(5):
    threadName = "Calculation-{}".format(threadId + 1)
    value = items[threadId]
    currentThread = threading.Thread(target=myCalculator, args=(threadName, value))
    threads.append(currentThread)
    currentThread.start()

