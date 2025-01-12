# -----------------------------------------------------------
# demonstrates how to use a two threads with the help of a
# queue, and do calculations
#
# idea taken from this tutorial:
# https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread
#
# (C) 2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# include standard modules
from threading import Thread
import queue

def square(x, queue):
    # calculate the square of the value of x
    # calculation is stored at the end of the queue
    queue.put(x * x)

if __name__ == '__main__':

    # define the dataset
    data1 = 5
    data2 = 10
    print ("dataset:", data1, data2)

    # define empty queue
    dataQueue = queue.Queue()

    # define thread 1
    thread1 = Thread(target=square, args=(data1, dataQueue))
    thread1.start()

    # define thread 2
    thread2 = Thread(target=square, args=(data2, dataQueue))
    thread2.start()

    # end thread 1 and 2
    thread1.join()
    thread2.join()

    print ("result 1:", dataQueue.get())
    print ("result 2:", dataQueue.get())

