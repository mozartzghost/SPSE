#/usr/bin/python
#
#Simple ECHO server for upto 10 clients
#(Templates for creating Python servers)
#Mark Osborn 03/06/2013
#
#

import thread
import socket
from datetime import datetime

def newConnection(clientSock, addr):
    while True:
        data = 'dummy'
        while len(data):
            
            data = clientSock.recv(2048)
            time = str(datetime.now())
            print time
            print "Client sent: ", data
            clientSock.send(data)
            
        clientSock.close()    
            
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("0.0.0.0", 9000))
s.listen(10)

while True:
    print "Waiting for a client..."
    clientSock, addr = s.accept()

    print "Received connection from: ", addr
    thread.start_new_thread(newConnection, (clientSock, addr))

