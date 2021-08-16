import socket
import threading


Port = 8000
Server =  "172.25.80.1"                #socket.gethostbyname(socket.gethostname())
Address = (Server,Port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(Address)
server.listen()

DISCONNECT_MESSAGE = "!DISCONNECT"


def client_handle(conn,addr):
    print(f'[NEW CONNECTION] {addr} connected.')
    
    connected =True
    while connected:
        message_length = conn.recv(64).decode('utf-8')
        
        if message_length:            
        
            message_length = int(message_length)
            message = conn.recv(message_length).decode('utf-8')
        
            if message == DISCONNECT_MESSAGE:
                connected =False
            
        print(f'[{addr}] {message}')
    conn.close()           
                             
    

def start():
   
    print(f'[LISTENING] Server is listening on {Server}')
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client_handle, args=(conn,addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS {threading.activeCount() - 1}')   
     

print("Server is starting...")
start()



"""with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(Address)
    server.listen()
    conn, addr = server.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)"""