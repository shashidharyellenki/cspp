import socket
import threading
import timeit

Soc = socket.socket()
host="192.168.1.4"
port=9999
Soc.bind((host,port))
Soc.listen()
Threadlst=[]
def starting():
        while True:
            print("server started...")
            conversation, conversationAdress = Soc.accept()
            thread = threading.Thread(target=handling, args=(conversation,conversationAdress, ))
            # activeConnections(thread)
            Threadlst.append(thread)
            # Threadlst.append(thread.start())
            thread.start()
            # thread.join()
        

def handling(conversation, conversationAdress):
    print(f'your connected with {conversationAdress[0]} ip and {conversationAdress[1]} port')
    query="Enter your Name?"
    conversation.send(query.encode())
    clientResponse = conversation.recv(1024).decode()
    print(f'Client notted as {clientResponse}')
    thanksMessage = f"thanks {clientResponse} for sending your name"
    conversation.send(thanksMessage.encode())
    conversation.close()

def executing(list):
    for thread in list:
        thread.join()

def main():
    executing(Threadlst)
    starting()

if __name__ == "__main__":
    main()