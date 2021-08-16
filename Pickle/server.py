import socket
import pickle
import time


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))
server.listen()

HEADER = 20



while True:
    clientsocket, address = server.accept()
    print(f'Connection from {address} has been established!')
    
    dc = {
    1: "Hello",
    2: "World!",
    3: "Pickle",
    4: "Socket",
    5: "Python"
}

    
    message = pickle.dumps(dc)
    message = bytes(f'{len(message): <{HEADER}}', "utf-8") + message
    
    clientsocket.send(message)


