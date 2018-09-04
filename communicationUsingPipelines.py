# A program that uses Pipeline to share data among two processes.
# The pipeline() yields two endpoints to establish communications
# which can be used by two processes to share data or information.
# Author: Varunaditya Jadwal

import multiprocessing

def sender(connectionObject, messages):
	for message in messages:
		connectionObject.send(message)
		print('Message Sent: {}'.format(message))

def receiver(connectionObject):
	while(1):
		message = connectionObject.recv()
		if message == 'END':
			break
		print('Message Received: {}'.format(message))

if __name__ == '__main__':
	connectionObject1, connectionObject2 = multiprocessing.Pipe()
	messages = ['MSG#1', 'MSG#2','MSG#3','MSG#4','MSG#5', 'END']
	p1 = multiprocessing.Process(target = sender, args = (connectionObject1, messages))
	p2 = multiprocessing.Process(target = receiver, args = (connectionObject2,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
