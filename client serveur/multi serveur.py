import socket
import os
from _thread import *

class joueur:
    def __init__(self,pseudo,ip):
        self.pseudo=pseudo
        self.ip=ip
        self.score=0

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
        #print(data.decode('utf-8'))
        data=(data.decode('utf-8')).split(",")
        if data[-1]=="connexion":
            reco=False
            for joueurs in liste_joueurs:
                print("joueur: "+str(joueurs.pseudo)+"/"+str(data[0]))
                if joueurs.pseudo==data[0]:
                    if joueurs.ip==data[1]:
                        connection.sendall(str.encode(str(joueurs.score)))
                        print(str(joueurs.pseudo),str(joueurs.score))
                        reco=True
                    else:
                        if data[0][-3]=="(" and data[0][-1]==")":
                            try:
                                data[0]+="("+int(data[0][-2])+")"
                            except : None
                        else:
                            data[0]+="(1)"
                            print(data[0])
            if reco==False:
                joueur1=joueur(data[0],data[1])
                liste_joueurs.append(joueur1)
            print(str(data[0])+" s'est connecté(e).\n")
            print("joueurs connectés :")
            for joueurs in liste_joueurs:
                print(str(joueurs.pseudo)+" - "+str(joueurs.ip))
        else: 
            print("le joueur "+str(data[0])+" a "+str(data[2])+" points")
            for joueurs in liste_joueurs:
                if joueurs.pseudo==data[0]:
                    joueurs.score=data[2]
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
    print('Thread Number: ' + str(ThreadCount) + '\n')
ServerSideSocket.close()
