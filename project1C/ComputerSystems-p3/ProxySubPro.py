import socket, os, subprocess, mimetypes
socketconnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketconnection.bind(('127.0.0.1',9999))
socketconnection.listen()
print('Wating to get connected with the localhost...')
while True:
    root = os.getcwd()
    # print('root:' , root)
    connection, connectionAddress = socketconnection.accept()
    print('sucessfully connected with the: ', connectionAddress)
    googleQuery = connection.recv(1024).decode()
    splitGoogleQuery = googleQuery.splitlines()[0].split(" ")[1]
    print('***',splitGoogleQuery)
    wwwFilename = splitGoogleQuery.split('/')[-1]
    print(wwwFilename,'-------wwwfilename----')
    fileReqest = root+splitGoogleQuery
    print(fileReqest,'....')
    fileNames = os.listdir("E:\\msit\\computer systems\\project1C\\ComputerSystems-p3\\bin")
    WWWFileNames = os.listdir('E:\msit\computer systems\project1C\ComputerSystems-p3\www')
    head = 'HTTP/1.1 200 OK \n Content-Type:text/html \n Content-Length:1024 \n Connection: close\n\n'
    '''---------------code for rendering files from bin folder--------------------------------------'''
    if splitGoogleQuery == '/bin':
        for file in fileNames:
            head+=f'<a href="{os.path.join(splitGoogleQuery,file)}">{file}</a><br>'
        connection.sendall(head.encode())
    elif splitGoogleQuery == '/www':
        '''-----------------------code for rendering www files to the browser-----------------------'''
        for file in WWWFileNames:
            head+=f'<a href="{os.path.join(splitGoogleQuery,file)}">{file}</a><br>'
        connection.sendall(head.encode())
    elif os.path.isfile(fileReqest):
        '''--------------------code for opening file in the broswer----------------------------'''
        if wwwFilename in WWWFileNames:
            f = open(fileReqest, 'rb')
            reading = f.read()
            f.close()
            head = f'HTTP/1.1 200 OK \n Content-Type:{mimetypes.MimeTypes().guess_type(wwwFilename)[0]} \n Content-Length:{str(len(reading))} \n Connection: close\n\n'
            head= head.encode('utf-8')
            head+=reading
            connection.sendall(head)
        elif splitGoogleQuery == '/bin/ls':
            result = os.popen('dir')
            reading = result.read()
            head = f'HTTP/1.1 200 OK \n Content-Type:text/html \n Content-Length:{str(len(reading))} \n Connection: close\n\n'
            head+=reading
            connection.sendall(head.encode())
        elif splitGoogleQuery == '/bin/du':
            result = os.popen('diskusage')
            reading = result.read()
            head = f'HTTP/1.1 200 OK \n Content-Type:text/html \n Content-Length:{str(len(reading))} \n Connection: close\n\n'
            head+=reading
            connection.sendall(head.encode())
        elif splitGoogleQuery =='/bin/test.py':
            '''------------ executing the test.py file to the browser--------------------'''
            print('shashihdar')
            output = subprocess.Popen(['python', 'E:\\msit\\computer systems\\project1C\\ComputerSystems-p3\\bin\\test.py'], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print('shashidhar')
            out, err = output.communicate()
            result = out.decode()
            print(result,'result')
            head = 'HTTP/1.1 200 OK \n Content-Type:text/plain \n Content-Length:1024 \n Connection: close\n\n'
            head+=result
            connection.sendall(head.encode())
    else:
        '''-----------if user sends invalid respose error message--------------------'''
        data="<h1>Invalid request</h1><h2>404 file not found</h2>"
        newLine='\n'
        message = "HTTP/1.1 200 OK"+newLine
        message+= "Content-Type: text/html"+newLine
        message+="Content-Lenght: " + str(len(data))+newLine
        message+="Connection: close"+newLine
        message+=newLine
        message+=data
        connection.sendall(bytes(message,'utf-8'))
    connection.close()
