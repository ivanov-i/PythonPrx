from unittest import TestCase
import socket

from ProxyApp.generic_proxy import GenericProxy

class TestProxy(TestCase):
    def test_that_listens_on_some_port(self):
        address = ('127.0.0.1', 8333)
        proxy = GenericProxy(address)
        proxy.start()
        client = socket.create_connection(address)
        client.close()
