'''
    Write a python client program that
        0. connects to localhost and port 10000
        1. send a "Hi <name>" message
        2. waits for the server to send the "READY" message
        3. guess a number and send to the server
        4. wait for the server to send the message
        5. Read the message and make a decision based on the following
            4.1 Close the client if the message is of the form "Correct! <name> took X attempts to guess the secret"
            4.2 Use the clue given by the server and repeat from step 3
'''


import socket
import sys
#creating clinet socket
clientSocket = socket.socket()
#connecting client socket with the server socket
clientSocket.connect(('127.0.0.1', 10002))
clientMessageName = input("Enter your name ")
clientMessage = 'Hi'+clientMessageName
clientSocket.send(bytes(clientMessage, 'utf-8'))

serverResponse = clientSocket.recv(1024).decode()
running=1
if 'READY' == serverResponse: 
    while running:
        guessAnswer = input("Enter your guess ")
        clientSocket.send(bytes(guessAnswer, 'utf-8'))
        serverAnswer = clientSocket.recv(1024).decode()
        if serverAnswer.startswith('Correct!'):
            running=0
        print(serverAnswer)
        