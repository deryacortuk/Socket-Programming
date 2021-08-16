import socket
import errno
import sys

HEADER = 50
IP = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((IP,PORT))
client.setblocking(False)

username_ = input("username: ")
username = username_.encode("utf-8")

username_header = f"{len(username):<{HEADER}}".encode("utf-8")
client.send(username_header + username)

while True:
    message = input(f"{username_} > ")
    
    if message:
        message = message.encode("utf-8")
        message_header = f"{len(message):<{HEADER}}".encode("utf-8")
        client.send(message_header + message)
    try:
        
       while True:
           username_header = client.recv(HEADER)
           if not len(username_header):
               print("connection closed!")
               sys.exit()
           username_length = int(username_header.decode("utf-8").strip())
           username =client.recv(username_length).decode("utf-8")
           
           message_header = client.recv(HEADER)
           message_length = int(message_header.decode("utf-8").strip())
           message = client.recv(message_length).decode("utf-8")
           
           print(f"{username} > {message}")
           
    except IOError as er:
        if er.errno != errno.EAGAIN and er.errno != errno.EWOULDBLOCK:
            print("Reading Error",str(er))
            sys.exit()
        continue      
           
    except Exception as er:
        print('General Error', str(er))
        sys.exit()
            
  
    
               
        
        




