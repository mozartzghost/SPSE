#/usr/bin/python
#
#Simple ECHO server for 1 client
#(Template for creating Python servers)
#Mark Osborn 03/06/2013
#
#

import socket
from datetime import datetime

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsocket.bind(("0.0.0.0", 9000))
tcpsocket.listen(1)

print "Waiting for a client..."
(client, (ip, port)) = tcpsocket.accept()

print "Received connection from: ", ip
print "Starting ECHO output..."

data = 'dummy'

while len(data):

        data = client.recv(2048)
        time = str(datetime.now())
        print time
        print "Client sent: ", data
        client.send(data)

print "Closing connection..."
client.close()
