import socket
import threading

host =  "172.25.80.1"
port = 8000
address = (host,port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen()

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)
        
        
def handle(client):
    while True:
        try:
            message =client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f'{username} left the chat!'.encode('utf-8'))
            usernames.remove(username)
            break
        
def receive():
    while True:
        conn, addr = server.accept()
        print(f"Connected with {str(addr)}")
        conn.send('user'.encode('utf-8'))
        username = conn.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(conn)
        print(f'username of the client is {username}!')
        broadcast(f'{username} joined the chat'.encode('utf-8'))
        conn.send('connected to the server'.encode('utf-8'))
        
        thread = threading.Thread(target=handle,args=(conn,))
        thread.start()

print("server is running...") 
receive()
        
            

