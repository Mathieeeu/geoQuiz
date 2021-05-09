import socket

def connexion_client_multi(pseudo,ip):
    global ClientMultiSocket,host,port,message

    ClientMultiSocket = socket.socket()
    
    host = ip
    port = 5050
    serveur_trouver=0

    print('En attente du serveur ...')
    try:
        ClientMultiSocket.connect((host, port))
        serveur_trouver=1
    except socket.error as e:
        print(str(e))

    if serveur_trouver==1:

        res = ClientMultiSocket.recv(1024)

        message = (str(pseudo)+","+str(ip)+",connexion")
        ClientMultiSocket.send(str.encode(message))
        res = ClientMultiSocket.recv(1024)
        if res.decode('utf-8').startswith('pseudo_update,'):
            pseudo=res.decode('utf-8').replace('pseudo_update,','')
            print("votre pseudo est maintenant {}".format(pseudo))

        return "en_attente"

    else:
        print("Il n'y a pas de serveur accessible")
        return "aucun_serveur_accessible"

def boucle_client_multi(pseudo,ip):
    global ClientMultiSocket, hostname, ip_client,ip_client,host,port,message 
    res = ClientMultiSocket.recv(1024)
    message_recu=res.decode('utf-8')
    return message_recu
        

def deconnexion_multi(pseudo,ip):
    global ClientMultiSocket
    message = (str(pseudo)+","+str(ip_client)+",deconnexion")
    ClientMultiSocket.send(str.encode(message))
    ClientMultiSocket.close()

