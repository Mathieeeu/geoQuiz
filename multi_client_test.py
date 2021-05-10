import socket
from tkinter import *

"""
pseudo=input("\nPseudo : ")
ip=input("IP de l'hôte : ")
if ip == "":
    ip="localhost"
    ip_client="localhost"
elif ip == "dev":
    ip="localhost"
    ip_client=input("IP du client : ")
"""

def connexion_client_multi(pseudo,ip):
    global ClientMultiSocket, hostname, ip_client,ip_client,host,port,message 
    hostname = socket.gethostname()
    ip_client = socket.gethostbyname(hostname)
    print('Ton Adresse IP : {}'.format(ip_client))

    ClientMultiSocket = socket.socket()

    


    print(pseudo,ip)

    host = ip
    port = 2015

    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

    res = ClientMultiSocket.recv(1024)

    message = (str(pseudo)+","+str(ip_client)+",connexion")
    ClientMultiSocket.send(str.encode(message))
    res = ClientMultiSocket.recv(1024)
    if res.decode('utf-8').startswith('pseudo_update,'):
        pseudo=res.decode('utf-8').replace('pseudo_update,','')
        print("votre pseudo est maintenant {}".format(pseudo))
    try:
        score=int(res.decode('utf-8'))
    except:
        score=0
    print("score="+str(score))

def boucle_client_multi(pseudo,ip):
    while True :
        choix="0"
        #print('update')
        res = ClientMultiSocket.recv(1024)
        message_recu=res.decode('utf-8')
        if message_recu == 'lancement':
            print(message_recu)
        #choix=input("demande_lancer_partie")
        choix="recherche_de_partie"
        if choix=="recherche_de_partie":
            message = (str(pseudo)+","+str(ip_client)+",demande_lancer_partie")
            ClientMultiSocket.send(str.encode(message))
        elif choix=="quitter":
            message = (str(pseudo)+","+str(ip_client)+",quitter")
            ClientMultiSocket.send(str.encode(message))
            ClientMultiSocket.close()

            #break

connexion_client_multi("leandro","localhost")
boucle_client_multi("leandro","localhost")
