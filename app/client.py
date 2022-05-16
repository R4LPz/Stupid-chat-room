import socket as Socket
import select 
import sys


socket = Socket.socket()
host = Socket.gethostname()
port = 4321
socket.connect((host,port))

socket_list = [socket, sys.stdin]

while True:
    readable_socks, _, _ = select.select(socket_list, [], [])
    
    for sock in readable_socks:
        if sock == socket:
            message = sock.recv(1024).decode()
            sys.stdout.write(message)
        else:
            message = sys.stdin.readline()
            socket.send(message.encode())
        sys.stdout.flush()

socket.close()

