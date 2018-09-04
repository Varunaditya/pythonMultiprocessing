# A program that uses the Manager class of the server process to synchronize data among various processes.
# Manager class supports a lot more data types as compared to synchronized variables and arrays but are slower.
# Author: Varunaditya Jadwal 

import multiprocessing

def printingRecords(records):
	for record in records:
		print('Name: {0}\tScore: {1}'.format(record[0], record[1]))


def insertRecord(record, records):
	records.append(record)
	print('The new record was added successfully!')

if __name__ == '__main__':
	with multiprocessing.Manager() as manager:
		records = manager.list([('A', 1), ('B', 2), ('C', 3)])
		recordToBeInserted = ('D', 4)
		p1 = multiprocessing.Process(target = insertRecord, args = (recordToBeInserted, records))
		p2 = multiprocessing.Process(target = printingRecords, args = (records,))
		p1.start()
		p1.join()
		p2.start()
		p2.join()