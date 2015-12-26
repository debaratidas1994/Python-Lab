"""
Write a client-server program using sockets. Client sends a tuple
containing two strings. One is the input string and other is a string which
denotes operation to be performed on the input string. Once the server
receives the tuple, it performs the operation on the string and sends the
result back to the client where it is printed.

 If the operation is "rev", server must reverse the string.

 If the operation is "cap", server must convert the string to
uppercase.

 If the operation is "encr", server must encrypt the string. [ "abc" ->
"bcd", "time" ->"ujnf" ]

 If the operation is not defined, server must send back "Invalid
Operation".

Demonstrate TCP and UDP communication.
"""
from socket import *
import pickle
s=socket(AF_INET,SOCK_STREAM)
s.connect(('localhost',8000))
while True:
	ch=input('Enter choice')
	st=input('Enter string')
	data=pickle.dumps((st,ch))
	s.send(data)
	data=s.recv(2048)
	data=data.decode()
	print(data)
	if(data=="Invalid Operation"):
		break
