"""
Write a program where one process acts like a server and the other the
client. Each time the client communicates a number, the server returns the
square of it. Avoid racing using semaphores. Avoid catering to the same
request twice. Let parent process (client) read the number from keyboard
and child process (server) computes the square and prints it and this must
happen continuously until the number sent is -1. If the number sent is -1,
terminate the child process and end the program. Make use of shared
variable.
"""
from multiprocessing import *

class Server(Process):
	def __init__(self):
		Process.__init__(self)
	def run(self):
		while True:
			s1.acquire()
			x.value=x.value*x.value
			s2.release()
class Client(Process):
	def __init__(self):
		Process.__init__(self)
	def run(self):
		s=set()
		while True:
			s3.release()
			s4.acquire()
			s1.release()
			s2.acquire()
			print(x.value)			
def get_input():
	while True:
		s3.acquire()
		x.value=int(input('Enter number'))
		if x.value==-1:
			server.terminate()
			client.terminate()
			break
		s4.release()

if __name__=='__main__':
	set_start_method('fork')
	main=current_process()
	x=Value('i')
	s1=Semaphore(0)
	s2=Semaphore(0)
	s3=Semaphore(0)
	s4=Semaphore(0)
	server=Server()
	server.start()
	client=Client()
	client.start()
	get_input()
