import socket
from tkinter.tix import Tree


s = socket.socket()

s.bind(('localhost', 9999))

s.listen(1)

print('waiting for connetions')

while True:
    connection,connectionAddress = s.accept()
    print('connection established with', connectionAddress)

    connection.send(bytes('hello','utf-8'))
    connection.close()
