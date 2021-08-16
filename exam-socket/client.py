import socket
from threading import Thread

port = 8000
host = "172.25.80.1"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((host,port))

def receive(conn):
    while True:
        
            message = conn.recv(1024).decode('utf-8')
            if message:
                print(message)            
       
    
    
def write():
    while True:
        message = "client@ "
        message += input(" ")
        client.send(message.encode('utf-8'))
 
 
         
receive_thread = Thread(target=receive, args=(client,))
receive_thread.start()

write_thread = Thread(target=write)
write_thread.start()
 
    