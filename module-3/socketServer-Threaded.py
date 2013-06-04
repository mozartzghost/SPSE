#!/usr/bin/python

import SocketServer


class EchoHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        print "Got connection from: ", self.client_address
        data = 'dummy'

        while len(data):
            data = self.request.recv(1024)
            print "Client sent: " +data
            self.request.send(data)

        print "Client left"




serverAddr = ("0.0.0.0", 9000)

server = SocketServer.ThreadingTCPServer(serverAddr, EchoHandler)

server.serve_forever()

