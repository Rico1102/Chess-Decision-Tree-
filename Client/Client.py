import socket
import json


class Client:
    def __init__(self):
        self.sock = socket.socket()

    def connect(self, ip, port):
        self.sock.connect((ip, port))

    def assign(self):
        msg = self.sock.recv(1024).decode()
        uid = json.loads(msg)
        uid = uid['id']
        print('Client got the following UID ', uid)
        return uid

    def send(self, msg):
        b_msg = bytes(msg, 'UTF-8')
        self.sock.send(b_msg)

    def find_opponent(self):
        r = json.loads(self.sock.recv(1024).decode())
        if r['status']:
            print("Opponent Found")

    def receive(self, que):
        r = self.sock.recv(1024)
        que.put(r.decode())

    def close(self):
        self.sock.close()
