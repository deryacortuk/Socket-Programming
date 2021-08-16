import socket
import threading

username = input("choose a username: ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host =  "172.25.80.1"
port = 8000
address = (host,port)
client.connect(address)

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'user':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("an error occured!")
            client.close()
            break
        
def write():
    while True:
        message = f'{username} : {input(" ")}'
        client.send(message.encode('utf-8'))
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()