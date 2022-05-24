import socket as Socket 
from _thread import *


server_socket = Socket.socket()
host = Socket.gethostname()
port = 4321
chat_members = []

server_socket.bind((host,port))
print('Server is running in port ', port)

server_socket.listen(2)

def client_process(connection, address):
    connection.send('Welcome to the chat room! \n'.encode())
    while True:
        message = connection.recv(1024).decode()
        if message:
            message = f'({address[1]}) {message}'
            broadcast(connection,message)
        
def broadcast(connection,message):
    for member in chat_members:
        if member != connection:
            member.send(message.encode())

while True:
    connection, address = server_socket.accept()
    print('recive a connection from: ', address)
    chat_members.append(connection)
    start_new_thread(client_process, (connection,address))

server_socket.close()