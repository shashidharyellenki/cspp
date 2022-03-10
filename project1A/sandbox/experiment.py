import socket
import sys

sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddress = ('localhost', 10000)
print('starting up on %s port %s ' % serverAddress)
sock.bind(serverAddress)
sock.listen(1)
while True:
    print('waiting for connection')
    connection, connectionAddress = sock.accept()
    print(f'connection address from ${connectionAddress}')
    data = connection.recv(1024)
    print(data)
    break