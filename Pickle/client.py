import pickle
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((socket.gethostname(), 1234))

HEADER = 20

while True:
    full_message = b''
    new_message = True
     
    while True:
         
        message = client.recv(64)
         
        if new_message:
             
            print(f'new message length: {message[:HEADER]}')
            message_len = len(message[:HEADER])
            new_message = False
             
        full_message += message
         
        if len(full_message)-HEADER == message_len:
             
            print("full message recv")
            print(full_message[HEADER:])
             
            dc = pickle.loads(full_message[HEADER:])
            print(dc)
             
            new_message = True
            full_message = b''
        print(full_message)
             