# -----------------------------------------------------------
# basic implementation of a queue for multiprocessing
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# define basic module
import multiprocessing

# define worker function
def calculate(processName, tasks, results):

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

if __name__ == "__main__":
	
	# define ipc manager
	manager = multiprocessing.Manager()

	# define queue for tasks, and for the computation results
	tasks = manager.Queue()
	results = manager.Queue()

	# define process pool with two processes
	numberOfProcesses = 4
	pool = multiprocessing.Pool(processes=numberOfProcesses)
	processes = []

	# initiate the worker processes
	for i in range(numberOfProcesses):

		# set process name
		processName = "P%i" % i

		# create process, and connect to function, and task queue
		newProcess = multiprocessing.Process(target=calculate, args=(processName,tasks,results))

		# add new process to the list of processes
		processes.append(newProcess)

		# start the process
		newProcess.start()

	# fill task queue
	taskList = [43, 1, 78, 56, 42, 8, 183, 334]
	for singleTask in taskList:
		tasks.put(singleTask)

	# meanwhile, do sth. else ...

	# quit the worker processes
	for i in range(numberOfProcesses):
		tasks.put(-1)

	# read calculation results
	processesThatFinished = 0
	while True:
		# read result
		newResult = results.get()

		# have a look at the results
		if newResult == -1:
			# one process has finished
			processesThatFinished += 1

			if processesThatFinished == numberOfProcesses:
				break
		else:
			# output result
			print("result:", newResult)

