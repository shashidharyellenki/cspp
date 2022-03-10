import socket

clinetSocket = socket.socket()

clinetSocket.connect(('localhost', 9999))

print(clinetSocket.recv(1024))