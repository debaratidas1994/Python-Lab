from socket import *
from threading import *
import pickle
s=socket(AF_INET,SOCK_STREAM)
s.bind(('localhost',8000))
s.listen(5)
def fun(sock):
	while True:
		data=sock.recv(2048)
		data=pickle.loads(data)
		if data[1]=='rev':
			sock.send(data[0][::-1].encode())
		elif data[1]=='cap':
			sock.send(data[0].upper().encode())
		elif data[1]=='encr':
			p=[chr((ord(i)-ord('a')+1)%26+ord('a')) for i in data[0]]
			sock.send(''.join(p).encode())
		else:
			sock.send('Invalid Operation'.encode())
			sock.close()
			break
while True:
	sock,add=s.accept()
	Thread(target=fun,args=(sock,)).start()
