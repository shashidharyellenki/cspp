
import os
import socket
import mimetypes
socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketConnection.bind(('127.0.0.1',8888))
socketConnection.listen()
print('waiting for connection.......')
while True:
    connection, connectionAddress = socketConnection.accept()
    print(f'your connected with {connectionAddress}')
    fullQuery = connection.recv(1024).decode()
    splitQuery = fullQuery.splitlines()
    dirpath = splitQuery[0].split(" ")[1]
    # print("dirpath",dirpath)
    fileRequest = dirpath.split('/')[-1]
    # print(fileRequest)
    root = os.getcwd()
    dataUrl = root+dirpath
    fileNames = os.listdir("E:\\msit\\computer systems\\project1C\\ComputerSystems-p3\\bin")
    # print(fileNames)
    if dirpath == '/bin':
        head = 'HTTP/1.1 200 OK \n Content-Type:text/html \n Content-Length:1024 \n Connection: close\n\n'
        for file in fileNames:
            head+=f'<a href="{os.path.join(dirpath,file)}">{file}</a><br>'
        connection.sendall(head.encode())
    elif os.path.isfile(dataUrl):
        f = open(dataUrl,'r')
        readingFile = f.read()
        f.close()
        head = 'HTTP/1.1 200 OK \n Content-Type:text/plain \n Content-Length:1024 \n Connection: close\n\n'
        print(exec(readingFile),"this is print")
        head+="s"
        connection.sendall(head.encode())

    connection.close()