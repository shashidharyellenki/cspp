import socket
import sys
class HTTPServer:
    '''
    making a default constructor
    '''
    def __init__(self, ip,port):
        self.ip=ip
        self.port=port
        #creating a socket connection
        socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        '''
        now we need to bind this socket connection with an ip address so we will be using bind()
        ip address is given in the lms portal
        '''
        socket_connection.bind((self.ip,port))
        '''
        we are listening to the clinets requests using this listen function 1 indicates that listen
        at most one connection at a time
        '''
        socket_connection.listen()
        '''
        we need to listen for connections all the time so making it infinte loop
        '''
       
        while True:
            print('waiting for the connection')
            '''
            accept will return two parts they are socket and address of the client we need to accept them
            at any cost so we are making two variables and storing them.
            (connection, [connection address])
            '''
            connection, clientAddress = socket_connection.accept()
            try:
                print("huraay... you're connected to the server", clientAddress)
                '''
                we are receving 1024 bytes from the clinet if we pass 0 bytes then the connections gets
                terminated bro
                '''
                data="<h1>Webserver under consturction</h1>"
                newLine='\n'
                message = "HTTP/1.1 200 OK"+newLine
                message+= "Content-Type: text/html"+newLine
                message+="Content-Lenght: " + str(len(data))+newLine
                message+="Connection: close"+newLine
                message+=newLine
                message+=data
                connection.sendall(bytes(message,'utf-8'))
                #connection.sendall(message.encode())
                
                connection.close()
            except:
                connection.send("exception".encode())

#main function
def main():
    HTTPServer('127.0.0.1', 8888)

if __name__ == "__main__":
    main()
