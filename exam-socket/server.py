import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((socket.gethostname(),8000))

server.listen()


def receive(connection):
    while True:
        message = connection.recv(1024).decode('utf-8')
        if message:
            print(message)
            
def send_message(conn)  :          
    while True:
        message = '@server:'
        message += input("")
        conn.send(message.encode('utf-8'))
        
def start():    
    
    print(f'[LISTENING] Server is listening on...')
    while True:
        conn, addr = server.accept()
        conn.send("Connected successfully!".encode('utf-8'))           
                
               
        
        thread_r = threading.Thread(target=receive, args=(conn,))
        thread_r.start()
        thread_s = threading.Thread(target=send_message,args=(conn,))
        thread_s.start()
        
print("Connection...")
start()
        
        
        

