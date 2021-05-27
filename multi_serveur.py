from tkinter import *
import tkinter.font as tkFont
import socket
import os
from _thread import *
import creation_questions
from random import *


class joueur:
    def __init__(self,pseudo,ip,client):
        self.pseudo=pseudo
        self.ip=ip
        self.score=0
        self.client=client

ServerSideSocket = socket.socket()
host = ''
port = 5051
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Recherche de clients ... \n')
ServerSideSocket.listen(5)

def detect_parent(pseudo):
    if pseudo[-3]=="(" and pseudo[-1]==")":
        return pseudo[0:-3]
    else:
        return pseudo

liste_joueurs=[]
def message_a_tous(message):
    #print("le serveur envoie "+message)
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
            joueurs.client.sendall(str.encode(message))



def multi_threaded_client(connection):
    connection.send(str.encode('Le serveur fonctionne !'))
    while True:
        global client_recu
        try:
            data = connection.recv(2048)
            data=(data.decode('utf-8')).split(",")
            
            if data[2]=="connexion":
                for joueurs in liste_joueurs:
                    if detect_parent(joueurs.pseudo)==detect_parent(data[0]):
                        if joueurs.ip==data[1]:
                            connection.sendall(str.encode(str(joueurs.score)))
                        else:
                            if joueurs.pseudo[-3]=="(" and joueurs.pseudo[-1]==")":
                                print(data[0]+" avant")
                                data[0]=detect_parent(data[0])+"("+str(int(joueurs.pseudo[-2])+1)+")"
                                print(data[0]+" après")
                            else:
                                data[0]+="(1)"
                                
                joueur1=joueur(data[0],data[1],client_recu)
                liste_joueurs.append(joueur1)
                connection.sendall(str.encode(str("pseudo_update,"+data[0])))
                print(str(data[0])+" s'est connecté(e).\n")
                #message_a_tous("\n"+str(data[0])+" s'est connecté(e).\n")

                for joueurs in liste_joueurs:
                    print(str(joueurs.pseudo)+" - "+str(joueurs.score)+" pts - "+str(joueurs.ip+"\n"))

            elif data[2]=="deconnexion":
                #mettre le code ici pour prendre en compte qu'une personne s'est deco
                for joueurs in liste_joueurs:
                    if joueurs.pseudo==data[0]:
                        liste_joueurs.pop(liste_joueurs.index(joueurs))
                        print(data[0]+" s'est déconnecté(e).\n")
                        
                    
        except:
            None
    connection.close()

def ajout_clients():
    global client_recu, ServerSideSocket, multi_threaded_client, ThreadCount
    try :
        ServerSideSocket.settimeout(0.1)
        Client, address = ServerSideSocket.accept()
        client_recu=Client
        start_new_thread(multi_threaded_client, (Client, ))
        ThreadCount += 1
    except  : None


def lancer_partie():
    print("Lancement de la partie\n")
    message_a_tous(str("lancement_partie "+str(randint(1,1000000))))
    

  

def page_menu():
    global menu
    menu.place(x=0, y=0)

    hostname = socket.gethostname()
    local_ip.set(socket.gethostbyname(hostname))
    
    bouton_lancer = StringVar()
    bouton_lancer=Button(menu, text='Lancer la partie',command=lancer_partie, font=police2, background = 'green')
    bouton_lancer.place(x=487,y=660,width=200, height=80)

    label_ip = Label(menu, textvariable=local_ip, font=police2, background = 'lightgrey', anchor='center')
    label_ip.place(x=37,y=68,width=232, height=35)

    textBoxTemps = Entry(menu,width=20,bg = 'gray89')
    textBoxTemps.place(x=455,y=352,width=50, height=30)

    bouton_mode_geoquiz = StringVar()
    bouton_mode_geoquiz=Button(menu,command=wip, font=police1)
    bouton_mode_geoquiz.place(x=768,y=212,width=198, height=148)
    file_bouton_mode_geoquiz="images/boutons/bouton_mode_geoquiz.png"
    image_bouton_mode_geoquiz = PhotoImage(file=file_bouton_mode_geoquiz)
    bouton_mode_geoquiz.configure(image=image_bouton_mode_geoquiz)
    bouton_mode_geoquiz.image = image_bouton_mode_geoquiz

    bouton_mode_aveugle = StringVar()
    bouton_mode_aveugle=Button(menu,command=wip, font=police1)
    bouton_mode_aveugle.place(x=974,y=212,width=198, height=148)
    file_bouton_mode_aveugle="images/boutons/bouton_mode_aveugle.png"
    image_bouton_mode_aveugle = PhotoImage(file=file_bouton_mode_aveugle)
    bouton_mode_aveugle.configure(image=image_bouton_mode_aveugle)
    bouton_mode_aveugle.image = image_bouton_mode_aveugle

    bouton_mode_chrono = StringVar()
    bouton_mode_chrono=Button(menu,command=wip, font=police1)
    bouton_mode_chrono.place(x=1180,y=212,width=198, height=148)
    file_bouton_mode_chrono="images/boutons/bouton_mode_chrono.png"
    image_bouton_mode_chrono = PhotoImage(file=file_bouton_mode_chrono)
    bouton_mode_chrono.configure(image=image_bouton_mode_chrono)
    bouton_mode_chrono.image = image_bouton_mode_chrono

    bouton_mode_br = StringVar()
    bouton_mode_br=Button(menu,command=wip, font=police1)
    bouton_mode_br.place(x=768,y=455,width=198, height=148)
    file_bouton_mode_br="images/boutons/bouton_mode_br.png"
    image_bouton_mode_br = PhotoImage(file=file_bouton_mode_br)
    bouton_mode_br.configure(image=image_bouton_mode_br)
    bouton_mode_br.image = image_bouton_mode_br

    bouton_mode_blitz = StringVar()
    bouton_mode_blitz=Button(menu,command=wip, font=police1)
    bouton_mode_blitz.place(x=974,y=455,width=198, height=148)
    file_bouton_mode_blitz="images/boutons/bouton_mode_blitz.png"
    image_bouton_mode_blitz = PhotoImage(file=file_bouton_mode_blitz)
    bouton_mode_blitz.configure(image=image_bouton_mode_blitz)
    bouton_mode_blitz.image = image_bouton_mode_blitz
    

    
    # Toutes les secondes la page menu est rafraichi ce qui envoi en attente au client
    #Si le client ne recoit rien tt les secondes il freeze

def en_attente():
    message_a_tous("en_attente")
    ajout_clients()
    fenetre.after(1000,en_attente)

def wip():
    print("Pas encore ajouté")

longueur = '1440'
largeur = '810'

chargement=0

fenetre = Tk()
fenetre.geometry(longueur+'x'+largeur)
fenetre.title('GéoQuiz : Serveur')
police1=tkFont.Font(family="MV Boli",size=20)
police2=tkFont.Font(family="MV Boli",size=16)

menu = Canvas(fenetre, width=longueur, height=largeur)

label_background = Label(menu, image="")
file_background="images/lobby_multi_serveur.png"
background = PhotoImage(file=file_background)
label_background.configure(image=background)
label_background.place(x=0,y=0,width=longueur, height=largeur)
local_ip=StringVar()

page_menu()
en_attente()


menu.mainloop()


ServerSideSocket.close()

#lancer_partie-->creation question--> les questions --> message a tous renvoi au client

