import socket
import select

HEADER = 50

IP = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((IP,PORT))

server.listen()

sockets_list = [server]

clients = {}


def receive(client_socket):
    try:
        message = client_socket.recv(HEADER)
        
        if not len(message):
            return False
        message_length = int(message.decode("utf-8").strip())
        return {"header": message, "data": client_socket.recv(message_length)}           
        
        
    except:
        return False
    
while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [],sockets_list)
    for notified in read_sockets:
        if notified == server:
            client_socket, client_address = server.accept()
            
            user = receive(client_socket)
            
            if user is False:
                continue
            
            sockets_list.append(client_socket)
            clients[client_socket] = user
            
            print(f"New connection from {client_address[0]} : {client_address[1]} username: {user['data'].decode('utf-8')}")
        
        else:
            message = receive(notified)
            
            if message is False:
                print(f"Closed connection from {clients[notified]['data'].decode('utf-8')}")
                
                sockets_list.remove(notified)
                
                del clients[notified]
                continue
            
            user = clients[notified]
            print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")
            
            for client_socket in clients:
                if client_socket != notified:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
                    
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
        