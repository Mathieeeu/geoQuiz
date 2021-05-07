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
port = 2003
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

def detect_parent(pseudo):
    if pseudo[-3]=="(" and pseudo[-1]==")":
        return pseudo[0:-3]
    else:
        return pseudo

liste_joueurs=[]
def message_a_tous(message):
    if message=="deco_test":
       for clients in liste_client:
            try:
                clients.sendall(str.encode(message))
            except:
                if input("le joueur "+str(liste_joueurs[liste_client.index(clients)].pseudo)+" s'est déconnecté.\n\
supprimer le joueur ? ")=="oui":
                    liste_joueurs.pop(liste_client.index(clients))
                    liste_client.pop(liste_client.index(clients))
                    print("joueur supprimé.")
    else:
        for clients in liste_client:
            try:
                clients.sendall(str.encode(message))
            except: None


def multi_threaded_client(connection):
    
    connection.send(str.encode('Server is working:'))
    while True:
        try:
            data = connection.recv(2048)
            data=(data.decode('utf-8')).split(",")
            if data[-1]=="connexion":
                reco=False
                for joueurs in liste_joueurs:
                    if detect_parent(joueurs.pseudo)==detect_parent(data[0]):
                        if joueurs.ip==data[1]:
                            connection.sendall(str.encode(str(joueurs.score)))
                            reco=True
                        else:
                            if joueurs.pseudo[-3]=="(" and joueurs.pseudo[-1]==")":
                                print(data[0]+" avant")
                                data[0]=detect_parent(data[0])+"("+str(int(joueurs.pseudo[-2])+1)+")"
                                print(data[0]+" après")
                            else:
                                data[0]+="(1)"
                if reco==False:
                    joueur1=joueur(data[0],data[1])
                    liste_joueurs.append(joueur1)
                    connection.sendall(str.encode(str("pseudo_update,"+data[0])))
                    print("\n"+str(data[0])+" s'est connecté(e).\n")
                    message_a_tous("\n"+str(data[0])+" s'est connecté(e).\n")
                else:
                    print("\n"+str(data[0])+" s'est reconnecté(e).\n")
                    message_a_tous("\n"+str(data[0])+" s'est reconnecté(e).\n")
                print("joueurs connectés :")
                for joueurs in liste_joueurs:
                    print(str(joueurs.pseudo)+" - "+str(joueurs.score)+" pts - "+str(joueurs.ip))
            else: 
                print("le joueur "+str(data[0])+" a "+str(data[2])+" points")
                for joueurs in liste_joueurs:
                    if joueurs.pseudo==data[0]:
                        joueurs.score=data[2]
            response = 'Server message: ' + str(",".join(data))
            if not data:
                break
            connection.sendall(str.encode(response))
        except:
            message_a_tous("deco_test")
            break
    connection.close()

liste_client=[]
while True:
    reco=False
    Client, address = ServerSideSocket.accept()
    for clients in liste_client:
        if clients == Client:
            reco=True
    if reco==False:
        liste_client.append(Client)
    #print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    #print('Thread Number: ' + str(ThreadCount) + '\n')
ServerSideSocket.close()
