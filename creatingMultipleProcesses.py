# A program that uses the multiprocessing library to create multiple processes 
# which can target similar or different functions. This example let's them target one function.
# Author: Varunaditya Jadwal

import multiprocessing
import os

def target1():
	# os.getpid() gives the process id of the current process
	print('ID of process #1 is: {}'.format(os.getpid())) 

def target2():
	print('ID of process #2 is: {}'.format(os.getpid()))

if __name__ == '__main__':
	print('ID of the main process is: {}'.format(os.getpid()))
	process1 = multiprocessing.Process(target = target1) 
	process2 = multiprocessing.Process(target = target2) 
	process1.start()
	process2.start()
	process1.join()
	process2.join()
	print('Execution of both the processes has been completed.')
	# <process object>.is_alive() returns whether the process related to the current object is alive or not.
	print('Is Process #1 still running: {}'.format(process1.is_alive()))
	print('Is Process #2 still running: {}'.format(process2.is_alive()))
	