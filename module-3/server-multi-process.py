#!/usr/bin/python
#
# Simple multi-process ECHO server
# for upto 10 clients using fork()
#
# Mark Osborn 03/06/2013
#
# This one only runs on Linux/Unix
# No error checking yet; if any process chokes
# it will all grind to a halt!
#

import os
import socket
from datetime import datetime

def newConnection(clientSock, addr):
    while True:
        data = 'dummy'
        while len(data):

            data = clientSock.recv(2048)
            time = str(datetime.now())
            print time
            print "PID: %d" %os.getpid()
            print "Client sent: ", data
            clientSock.send(data)

        clientSock.close()

def server():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(("0.0.0.0", 9000))
    s.listen(10)

    while True:
        print "Process %d waiting for a client..." %os.getpid()
        clientSock, addr = s.accept()

        print "Received connection from: ", addr
        childpid = os.fork()

        if childpid == 0:
            newConnection (clientSock, addr)
        else:
            pass

server()



