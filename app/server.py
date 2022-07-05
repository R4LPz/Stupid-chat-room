import socket as Socket 
from _thread import *
import logging
import os
from datetime import datetime


class Chat_room():
    
    def __init__(self):
        self.socket = Socket.socket()
        self.host = Socket.gethostname()
        self.port = 6666
        self.users_list = []
        self.datetime_today = datetime.today()
        self.date_today = self.datetime_today.strftime("%Y-%m-%d")
        if not 'backups' in os.listdir():
            os.mkdir('backups')
        if not 'logs' in os.listdir():
            os.mkdir('logs')
        logging.basicConfig(filename=f'./logs/{self.date_today}.log', encoding='utf-8', level=logging.DEBUG)

    def start_channel(self):
        self.socket.bind((self.host,self.port))
        self.socket.listen(10)
        print('Server is running in port :', self.port)
        logging.info(f'Server started - {self.datetime_today}')

    def join(self):
        while True:
            connection, address = self.socket.accept()
            logging.info(f'Recive a new  connection to - {self.datetime_today} -  {address}')
            self.users_list.append({'nickname': address[1],'address': address, 'connection': connection})
            start_new_thread(self.client_process, (connection,))
        self.socket.close()

    def client_process(self, connection):
        user = self.get_user_by_connection(connection)
        connection.send(f'Welcome to the chat room!\n'.encode())
        while True:
            message = connection.recv(1024).decode()
            self.call_command(message,user)

    def call_command(self, message,user):
        tokens = message.strip().split(' ')
        radical = tokens[0]        
        if len(tokens) > 1:
            parammeter = tokens[1]
        if radical == '<restore>':
            self.restore_messages(user["connection"])
        elif radical == '<users>':
            self.list_users(user["connection"])
        elif radical == '<quit>':                 
            user["connection"].send("Bye!".encode())
            user["connection"].close()
            self.users_list.remove(user)
        elif radical == '<nickname>' and parammeter:
            self.edit_nickname(user, parammeter)
        elif message:
            message = f'<{user["nickname"]}> {message}'
            logging.info(f'({user["nickname"]}) - {self.datetime_today} - sended a new message ')        
            self.log_message(message)
            self.broadcast(user, message)       

    def nickname_valid(self,nick):
        for user in self.users_list:
            if user["nickname"] == nick:
                return False
        return True

    def edit_nickname(self,user, nick):
        if self.nickname_valid(nick):
            user["nickname"] = nick
            user["connection"].send("Nickname updated\n".encode())
        else:
            user["connection"].send("Nickname already in use\n".encode())

    def get_user_by_connection(self, connection):
        for user in self.users_list:
            if user['connection'] == connection:
                return user

    def list_users(self, connection):
        for user in self.users_list:
            connection.send(f'* {user["nickname"]}\n'.encode())

    def restore_messages(self,connection):
        historic = open(f'./backups/{self.date_today}.txt', 'r').readlines()
        connection.send('------------------- Restored Messages -------------------\n'.encode())
        for line in historic:
            connection.send(line.encode())
        connection.send('----------------------------------------------------------\n'.encode())

    def log_message(self, message):
        historic = open(f'./backups/{self.date_today}.txt', 'a')
        historic.write(message)
        historic.close()

    def broadcast(self, sender, message):
        for user in self.users_list:
            if not user == sender:
                user["connection"].send(message.encode())

if __name__ == '__main__':
    chat = Chat_room()
    chat.start_channel()    
    chat.join()
