# -------------------------------------------------------------
# basic implementation of multi-threading using multiprocessing
#o
# (C) 2019-2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -------------------------------------------------------------

# define basic module
import multiprocessing, random, time

def myCalculator(processName, value):
    "do the calculation as a separate thread"
    pause = random.random()
    time.sleep(pause)
    print("[%s] the square of %i is %i" % (processName, value, value * value))
    return

items = [55, 75, 30, 4, 25]
processes = []

for processId in range(5):
    processName = "Calculation-{}".format(processId + 1)
    value = items[processId]
    currentProcess = multiprocessing.Process(target=myCalculator, args=(processName, value, ))
    processes.append(currentProcess)
    currentProcess.start()

