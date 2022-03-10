import socket,os,subprocess,mimetypes

socketconnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketconnection.bind(('127.0.0.1',8888))
socketconnection.listen(1)
print('waiting for the localhost connetion to connet...')
while True:
    connection, connectionAddress = socketconnection.accept()
    print('connected to the:', connectionAddress)
    googleQuery= connection.recv(1024).decode()
    splitLink = googleQuery.splitlines()[0]
    print("split:------->",splitLink)

    
    socketconnection.close()

