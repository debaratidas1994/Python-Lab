from socket import *
import pickle
s=socket(AF_INET,SOCK_DGRAM)
while True:
	ch=input('Enter choice')
	st=input('Enter string')
	data=pickle.dumps((st,ch))
	s.sendto(data,('localhost',8000))
	data,add=s.recvfrom(2048)
	data=data.decode()
	print(data)
	if(data=="Invalid Operation"):
		break
