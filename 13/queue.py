
'''

Implement two-way communication between parent and child processes using:
a) Pipe
b) Queue

'''
from multiprocessing import *

q=Queue()
def fun():
	print(current_process(),q.get())
	print(current_process(),q.get())	
	
if __name__=='__main__':
	p=Process(target=fun)
	p.start()
	q.put('hello from main')
	q.put('abc')
