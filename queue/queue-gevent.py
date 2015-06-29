# -----------------------------------------------------------
# basic implementation of processing a queue using gevent
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define imported module
import gevent
from gevent.queue import Queue

# define queue for tasks with size 10, and for the computation results
tasks = Queue(maxsize=10)
results = Queue()

# define worker function
def calculate(processName):

	# output: evaluation started
	print("[%s] evaluation routine starts" % processName)
	while True:
		newValue = tasks.get()
		if newValue < 0:
			# output: evaluation is finished
			print("[%s] evaluation routine quits" % processName)

			# indicate: finished
			results.put(-1)

			break
		else:

			# compute result
			compute = newValue * newValue

			# output received value, and calculation result
			print("[%s] received value: %i" % (processName, newValue))
			print("[%s] calculated value: %i" % (processName, compute))

			# add result to the queue
			results.put(compute)

	return

#def boss ():
#
#	# fill task queue
#	taskList = [43, 1, 78, 56, 42, 8, 183, 334]
#	for singleTask in taskList:
#		tasks.put(singleTask)
#
#	return

if __name__ == "__main__":
	
	# define event handler
	# bossEvent = gevent.spawn(boss)
	# eventList = [bossEvent]
	eventList = []

	# define worker pool
	numberOfWorkers = 4

	# initiate the worker processes
	for i in range(numberOfWorkers):

		# set worker name
		workerName = "W%i" % i

		# create worker, and connect to function, and task queue
		newWorker = gevent.spawn(calculate, workerName)

		# add new worker to the list of workers
		eventList.append(newWorker)

	# fill task queue
	taskList = [43, 1, 78, 56, 42, 8, 183, 334, 41, 5, 18, 10, 22]
	for singleTask in taskList:
		tasks.put(singleTask)

	# attach quit signals for the workers
	for i in range(numberOfWorkers):
		tasks.put(-1)

	# combine gevents
	gevent.joinall(eventList)

	# read calculation results
	workersThatFinished = 0
	while True:
		# read result
		newResult = results.get()

		# have a look at the results
		if newResult == -1:
			# one worker has finished
			workersThatFinished += 1

			if workersThatFinished == numberOfWorkers:
				break
		else:
			# output result
			print("result:", newResult)

