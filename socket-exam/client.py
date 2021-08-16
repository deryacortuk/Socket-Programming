import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((socket.gethostname(), 8000))

HEADER = 17

while True:
    messages = ''
    new_message = True
    
    while True:
    
        message = client.recv(16)
        
        if new_message:
            print(f'new message length: {message[:HEADER]}')
            msglen = len(message[:HEADER])            
            new_message = False
            
        messages += message.decode("utf-8")
        
        if len(messages)-HEADER == msglen:
            print("full message recieved")
            print(messages[HEADER:])
            new_message = True
            messages = ''   
        print(messages)
    

