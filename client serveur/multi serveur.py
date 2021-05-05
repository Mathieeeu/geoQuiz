import socket
import os
from _thread import *

class joueur:
    def __init__(self,pseudo,ip):
        self.pseudo=pseudo
        self.ip=ip
        self.score=0
    
    def point(score):
        self.score=score

ServerSideSocket = socket.socket()
host = ''
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

liste_joueurs=[]

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        print(data.decode('utf-8'))
        data=(data.decode('utf-8')).split(",")
        print("le joueur "+str(data[0])+" a "+str(data[2])+" points")
        if data[-1]=="connexion":
            joueur1=joueur(data[0],data[1])
            liste_joueurs.append(joueur1)
            print(liste_joueurs)
        response = 'Server message: ' + str(",".join(data))
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
