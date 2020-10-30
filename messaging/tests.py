import unittest
import socketio

# Create your tests here.

class SocketClientTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_socket_client_connection(self):
        socket = socketio.Client(ssl_verify=False)
        socket.connect(
            "https://iss.ishraak.com:443?server_token=xNTk3ODk0ODE5LCJqdGkiOiJiMGYxODEyOWI0Mjk0OGU4YmFjMmQwMWRmNDdlNTM0YyIsInVzZXJfaWQiOjUwfQ")