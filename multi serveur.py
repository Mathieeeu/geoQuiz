from tkinter import *
import tkinter.font as tkFont
import socket
import os
from _thread import *

class joueur:
    def __init__(self,pseudo,ip,client):
        self.pseudo=pseudo
        self.ip=ip
        self.score=0
        self.client=client

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
    print(message)
    if message=="deco_test":
       for joueurs in liste_joueurs:
            try:
                joueurs.client.sendall(str.encode(message))
            except:
                #ICI : POSSIBILITE DE DELETE UN JOUEUR EN CAS DE DECONNEXION
                """
                if input("le joueur "+str(joueurs.pseudo)+" s'est déconnecté.\n\
supprimer le joueur ? ")=="oui":
                    liste_joueurs.pop(liste_joueurs.index(joueurs))
                    print("joueur supprimé.")
                """
                None
    else:
        for joueurs in liste_joueurs:
            try:
               joueurs.client.sendall(str.encode(message))
            except: None


def multi_threaded_client(connection):
    global lancement_partie
    print(connection)
    connection.send(str.encode('Server is working:'))
    while True:
        global client_recu
        try:
            data = connection.recv(2048)
            data=(data.decode('utf-8')).split(",")
            if data[2]=="connexion":
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
                    joueur1=joueur(data[0],data[1],client_recu)
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
            elif data[2]=="quitter":
                for joueurs in liste_joueurs:
                    if joueurs.pseudo==data[0]:
                        liste_joueurs.pop(liste_joueurs.index(joueurs))
                        print(data[0]+" a quitté la partie.")

            elif data[2]=="demande_lancer_partie":
                if lancement_partie == 1 :
                    lancement_partie = 0
                    valeure = 'stp marche'
                else :
                    valeure = 'non'

                message_a_tous(valeure)
                
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
            None
    connection.close()



def page1():
    global menu
    menu.place(x=0, y=0)

    hostname = socket.gethostname()
    local_ip.set(socket.gethostbyname(hostname))
    
    bouton_jouer = StringVar()
    bouton_jouer=Button(menu, text='Lancer la partie',command=lancer_partie, font=police1)
    bouton_jouer.place(x=20,y=300,width=300, height=50)

    label_ip = Label(menu, textvariable=local_ip, font=police1, background = 'lightgrey', anchor='center')
    label_ip.place(x=0,y=100,width=400, height=70)

def boucle():
    global client_recu, ServerSideSocket, multi_threaded_client, ThreadCount
    print('aaa')
    Client, address = ServerSideSocket.accept()
    client_recu=Client
    #print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    #print('Thread Number: ' + str(ThreadCount) + '\n')



def lancer_partie():
    #global lancement_partie
    #lancement_partie = 1
    message_a_tous("ljdslfj")

longueur = '450'
largeur = '640'

fenetre = Tk()
fenetre.geometry(longueur+'x'+largeur)
fenetre.title('GéoQuiz : Serveur')
police1=tkFont.Font(family="MV Boli",size=20)
police2=tkFont.Font(family="MV Boli",size=16)

menu = Canvas(fenetre, width=longueur, height=largeur)

local_ip=StringVar()

page1()
boucle()


menu.mainloop()

ServerSideSocket.close()
