from socket import *
from threading import *
import pickle
sock=socket(AF_INET,SOCK_DGRAM)
sock.bind(('localhost',8000))
		
while True:
		data,addr=sock.recvfrom(2048)
		data=pickle.loads(data)
		if data[1]=='rev':
			sock.sendto(data[0][::-1].encode(),addr)
		elif data[1]=='cap':
			sock.sendto(data[0].upper().encode(),addr)
		elif data[1]=='encr':
			p=[chr((ord(i)-ord('a')+1)%26+ord('a')) for i in data[0]]
			sock.sendto(''.join(p).encode(),addr)
		else:
			sock.sendto('Invalid Operation'.encode(),addr)

