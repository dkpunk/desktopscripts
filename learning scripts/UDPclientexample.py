from socket import *
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpCLiSock = socket(AF_INET,SOCK_DGRAM)
while True:
	data = input('>')
	if not data:
		break
	udpCLiSock.sendto(data,ADDR)
	data,ADDR = udpCLiSock.recvfrom(BUFSIZ)
	if not data:
		break
	print(data)
udpCLiSock.close()
