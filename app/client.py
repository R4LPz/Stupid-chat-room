import socket as Socket
import select 
import sys


socket = Socket.socket()
host = Socket.gethostname()
port = 6666
socket.connect((host,port))

socket_list = [socket, sys.stdin]

while True:
    readable_socks, _, _ = select.select(socket_list, [], [])
    
    for sock in readable_socks:
        if sock == socket:
            message = sock.recv(1024).decode()
            if message.strip() == 'Bye Bye! Closing connetion!':
                sys.stdout.write(message)
                break
            sys.stdout.write(message)
        else:
            message = sys.stdin.readline()
            socket.send(message.encode())
        sys.stdout.flush()

socket.close()

