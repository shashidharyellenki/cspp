import socket
import os
import subprocess

Socket = socket.socket()

host="192.168.1.4"
port=9999

Socket.connect((host,port))
serverMessage = Socket.recv(1024).decode()
print(serverMessage)
serverInput = input()
Socket.send(serverInput.encode())
ThanksReplt = Socket.recv(1024).decode()
print(ThanksReplt)
