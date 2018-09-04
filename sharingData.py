# A program that uses synchronized variables from the multiprocessing library to share
# data among various processes.
# Syntax: <variableName> = multiprocessing.Value(<dataType>)
# Author: Varunaditya Jadwal

import multiprocessing

def fibonacci(N, sum):
	series = [0,1]
	for i in range(2,N+3):
		series.append(series[i - 2] + series[i - 1])
	# assigning the synchronized variable a value
	sum.value = series[-1] - 1
	print('Sum as evaluated in process #1: {}'.format(sum.value))

if __name__ == '__main__':
	N = 10
	# creating a synchronized variable for sharing of data among various processes
	sum = multiprocessing.Value('i')
	p1 = multiprocessing.Process(target = fibonacci, args = (N, sum))
	p1.start()
	p1.join()
	print('Sum as evaluated in main process: {}'.format(sum.value))