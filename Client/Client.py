import socket


class Client:
    def __init__(self):
        self.sock = socket.socket()

    def connect(self, ip, port):
        self.sock.connect((ip, port))

    def assign(self):
        num = int(self.sock.recv(1024).decode())
        print('Client got the following number ', num)
        return num

    def send(self, msg):
        b_msg = bytes(msg, 'UTF-8')
        self.sock.send(b_msg)

    def receive(self):
        r = self.sock.recv(1024)
        data = r.decode()
        return data

    def close(self):
        self.sock.close()
