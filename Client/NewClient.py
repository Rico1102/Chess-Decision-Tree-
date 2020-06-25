import socket
import json

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print('Socket Creation Error\nCause : ', e)
    exit()

PORT = 5100


def startChat(server, uid):
    turn = 0
    while True:
        turn += 1
        if turn % 2 == uid % 2:
            print('Sending')
            message = input('Client : ')
            server.send(bytes(message, 'UTF-8'))
            if message.strip().lower() == 'exit':
                s.close()
                break
        else:
            print('Listening')
            message = server.recv(1024).decode()
            print(message)
            if message.split(':')[1].strip().lower() == 'exit':
                break


s.connect(('127.0.0.1', PORT))

msg = s.recv(1024).decode()
print(msg)
msg = s.recv(1024).decode()
print(msg)
uid = json.loads(msg)
uid = uid['id']
msg = s.recv(1024).decode()
print(msg)
msg = s.recv(1024).decode()
print(msg)
msg = s.recv(1024).decode()
print(msg)
msg = s.recv(1024).decode()
print(msg)
if msg.lower() == 'start':
    startChat(s, uid)
    s.close()
elif msg.lower() == 'exit':
    s.close()
    exit()
