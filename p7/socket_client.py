import json
from threading import Thread

import socketio

class SocketClient:
    socket = socketio.Client(ssl_verify=False)

    @staticmethod
    @socket.on("receive")
    def _receive(data):
        data = json.loads(data)
        if data.get("type") == "status":
            if data.get("text") == "valid":
                print("authenticated")
        else:
            print("invalid credential")
            SocketClient.socket.disconnect()

    @classmethod
    def send(cls, data):
        msg_thread = Thread(target=cls._send, args=(data,))
        msg_thread.start()

    ##ToDO
    @classmethod
    def _send(cls, data):
        if not cls.socket.connected:
            cls.socket.connect(
                "https://iss.ishraak.com:443?server_token=xNTk3ODk0ODE5LCJqdGkiOiJiMGYxODEyOWI0Mjk0OGU4YmFjMmQwMWRmNDdlNTM0YyIsInVzZXJfaWQiOjUwfQ")
        if cls.socket.connected:
            msg = json.dumps(data)
            print(msg)
            cls.socket.emit('send', msg)