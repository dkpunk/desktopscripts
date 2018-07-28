

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)


from time import ctime
HOST = ''
PORT = 21567
ADDR = (HOST,PORT)

class MyRequestHandler(SRH):
	def handler(self):
		print('..connected from:',self.client_address)
		self.wfile.write('[%s] %s' %(ctime(),self.rfile.readline()))
tcpServ = TCP(ADDR,MyRequestHandler)
print('waiting for connection')
tcpServ.serve_forever()



'''
Lines 1–9
The initial stuff consists of importing the right classes from SocketServer.
Note that we are using the multiline import feature introduced in Python 2.4.
If you are using an earlier version of Python, then you will have to use the
fully-qualified module.attribute names or put both attribute imports on
the same line:
from SocketServer import TCPServer as TCP, StreamRequestHandler as SRH
Lines 11–15
The bulk of the work happens here. We derive our request handler MyRequest
Handler as a subclass of SocketServer’s StreamRequestHandler and override
its handle() method, which is stubbed out in the Base Request class with no
default action as:
def handle(self):
pass
The handle() method is called when an incoming message is received
from a client. The StreamRequestHandler class treats input and output
sockets as file-like objects, so we will use readline() to get the client message
and write() to send a string back to the client.
Accordingly, we need additional carriage return and NEWLINE characters
in both the client and server code. Actually, you will not see it in the
code because we are just reusing those which come from the client. Other
than these minor differences, it should look just like our earlier server.
7 HOST = ''
8 PORT = 21567
9 ADDR = (HOST, PORT)
10
11 class MyRequestHandler(SRH):
12 def handle(self):
13 print '...connected from:', self.client_address
14 self.wfile.write('[%s] %s' % (ctime(),
15 self.rfile.readline()))
16
17 tcpServ = TCP(ADDR, MyRequestHandler)
18 print 'waiting for connection...'
19 tcpServ.serve_forever()
2.4
82 Chapter 2 • Network Programming
Lines 17–19
The final bits of code create the TCP server with the given host information
and request handler class. We then have our entire infinite loop waiting
for and servicing client requests.
'''