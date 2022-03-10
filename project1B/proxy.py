import mimetypes
import socket
import os
socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketConnection.bind(('127.0.0.1',10002))
socketConnection.listen(1)
print('waiting for connections...')
while True:
    connection, connectionAddress = socketConnection.accept()
    print(f'you are connected with {connectionAddress}')
    fullQuery = connection.recv(1024).decode()
    print(fullQuery)
    split_query = fullQuery.splitlines()
    dirpath = split_query[0].split(" ")[1]
    print("this is direpath",dirpath)
    fileRequest = dirpath.split('/')[-1]
    print(fileRequest)
    root = "E:\msit\computer systems\project1B" #chnage to your direcotru upto project1b
    data_url = root+dirpath
    print(data_url,"data_ur;")
    fileNames = os.listdir("E:\msit\computer systems\project1B\www")#chnage to your direcotry
    # print(fileNames)
    if dirpath=='/www':
        head = 'HTTP/1.1 200 OK \n Content-Type:text/html \n Content-Length:1024 \n Connection: close\n\n'
        for file in fileNames:
            head+=f'<a href="{os.path.join(dirpath,file)}">{file}</a><br>'
        connection.sendall(head.encode())
    elif os.path.isfile(data_url):
        print('data:',os.path.isfile(data_url))
        f= open(data_url,'rb')
        req = f.read()
        f.close()
        res = f'HTTP/1.1 200 ok \n Content-Type={mimetypes.MimeTypes().guess_type(fileRequest)[0]}\n Content-Length:{len(str(req))}\n Connection:close\n\n'
        res = res.encode('utf-8')
        res+=req
        connection.sendall(res)
    else:
        data="<h1>Webserver under consturction</h1>"
        newLine='\n'
        message = "HTTP/1.1 200 OK"+newLine
        message+= "Content-Type: text/html"+newLine
        message+="Content-Lenght: " + str(len(data))+newLine
        message+="Connection: close"+newLine
        message+=newLine
        message+=data
        connection.sendall(bytes(message,'utf-8'))
        # query = connection.recv(1024).decode()
    connection.close()