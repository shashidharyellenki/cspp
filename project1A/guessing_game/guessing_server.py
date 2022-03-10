'''
    Write a python server program that
        0. initialized a socket connection on localhost and port 10000
        1. accepts a connection from a  client
        2. receives a "Hi <name>" message from the client
        3. generates a random numbers and keeps it a secret
        4. sends a message "READY" to the client
        5. waits for the client to send a guess
        6. checks if the number is
            6.1 equal to the secret then it should send a message "Correct! <name> took X attempts to guess the secret"
            6.2 send a message "HIGH" if the guess is greater than the secret
            6.3 send a message "LOW" if the guess is lower than the secrent
        7. closes the client connection and waits for the next one
'''

import random
import socket
import sys 
#creating a socket
serverSocket = socket.socket()
#binding the socket with the ip and port address
serverSocket.bind(('127.0.0.1', 10002))
#socket will listen request from the client
serverSocket.listen(1)
#making infinte loop to listen client requests 

while True:
    connection, connectionAddress = serverSocket.accept()
    print('connected with', connectionAddress)
    #accepting the name from the user
    userName = connection.recv(1024).decode()
    userNameHi =userName.replace('Hi',"")
    print(userNameHi)
    #generating a random number
    secretNumber = random.randint(0,100)
    #sending ready message to client
    connection.send('READY'.encode())
    #accepting the client's SecretNumber
    running=1
    count=0
    while running:
        clientResponse = int(connection.recv(1024).decode())
        count+=1
        #checking weather the number is == or < or > than the secret number
        if clientResponse == secretNumber:
            running=0
            # connection.send(bytes('FoundAnswer', 'utf-8'))
            connection.send( f'Correct!  {userNameHi} took  {count}  attempts to guess the secret'.encode())
        elif clientResponse > secretNumber:
            connection.send('HIGH' .encode())
        else:
            connection.send( 'LOW'.encode())
    connection.close()

