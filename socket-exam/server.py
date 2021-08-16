import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((socket.gethostname(),8000))

server.listen(5)

HEADER = 17

while True:
    clientsocket, address = server.accept()
    print(f'Connection from {address} has been established!')
    
    message = "Welcome to the server!"

    message = f'{len(message):<{HEADER}}'+ message
    
    clientsocket.send(bytes(message, "utf-8"))

    
    
    

