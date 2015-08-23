import socket

class GenericProxy(object):
    def __init__(self, address):
        self.address = address

    def start(self):
        self.socket = socket.socket()
        self.socket.bind(self.address)
        self.socket.listen(10)
