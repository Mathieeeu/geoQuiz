from tkinter import *
import tkinter.font as tkFont
import socket
import os

#06.01.2022 : pour le raccourci sur le bureau----------------------

geoquiz_location_path = os.getcwd()

if os.path.isfile(geoquiz_location_path+"\main_fix.py"):
    geoquiz_location_path=''
else:
    import sys
    from win32com.client import Dispatch
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut("GéoQuiz.lnk")
    geoquiz_location_path=''.join((shortcut.Targetpath).rsplit('\\', 1)[0])+'\\'
    sys.path.insert(1, geoquiz_location_path)

#------------------------------------------------------------------

from _thread import *
import creation_questions
from random import *

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Initialisation des fonctions serveurs XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

class joueur: # classe qui permet de définir toutes les variables des joueurs
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

def detect_parent(pseudo): # permet de détecter si plusieurs joueurs ont le meme pseudo (car il y a ecrit joueur(2))
    if pseudo[-3]=="(" and pseudo[-1]==")":
        return pseudo[0:-3]
    else:
        return pseudo

liste_joueurs=[]


def message_a_tous(message): # la focntion permet d'envoyer un message à tout les houers (ex : lancement partie)
    #print("le serveur envoie "+message)
    if message=="deco_test":
       for joueurs in liste_joueurs:
            try:
                joueurs.client.sendall(str.encode(message))
            except:
                #ICI : POSSIBILITE DE DELETE UN JOUEUR EN CAS DE DECONNEXION (MARCHE PAS ENCORE)
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



def multi_threaded_client(connection): # la fonction permet de gerer la connexion avec plusieurs client en meme temps
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
                #PAS ENCORE MIS AU POINT
                for joueurs in liste_joueurs:
                    if joueurs.pseudo==data[0]:
                        liste_joueurs.pop(liste_joueurs.index(joueurs))
                        print(data[0]+" s'est déconnecté(e).\n")
                        
                    
        except:
            None
    connection.close()

def ajout_clients(): # permet d'ajouter un nouveau client en ajoutant un nouveau thread
    global client_recu, ServerSideSocket, multi_threaded_client, ThreadCount
    try :
        ServerSideSocket.settimeout(0.1)
        Client, address = ServerSideSocket.accept()
        client_recu=Client
        start_new_thread(multi_threaded_client, (Client, ))
        ThreadCount += 1
    except  : None


def lancer_partie(): # lancement de la partie quand le bouton est cliqué
    print("Lancement de la partie\n")
    message_a_tous(str("lancement_partie "+str(randint(1,1000000)))) #une seed est envoyé pour que tout les clients ait la meme seed et donc les memes questions


def en_attente(): # si aucune action est demandé alors le serveur envoi toute les secondes en attentes aux clients
    message_a_tous("en_attente")
    ajout_clients()
    fenetre.after(1000,en_attente)


def wip(): # Work In Progress
    print("Pas encore ajouté")

    
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Initialisation de l'interface graphique XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  

def page_menu(): # la seule page pour l'instant où le serveur peut lancer la partie (plus tard, le serveur poura choisir le mode de jeu, la duree ...
    global menu
    menu.place(x=0, y=0)

    hostname = socket.gethostname()
    local_ip.set(socket.gethostbyname(hostname))
    
    bouton_lancer = StringVar()
    bouton_lancer=Button(menu, text='Lancer la partie',command=lancer_partie, font=police2, background = 'green', fg='black')
    bouton_lancer.place(x=487,y=660,width=200, height=80)

    label_ip = Label(menu, textvariable=local_ip, font=police2, background = 'lightgrey', anchor='center', fg='black')
    label_ip.place(x=37,y=68,width=232, height=35)

    textBoxTemps = Entry(menu,width=20,bg = 'gray89', fg='black')
    textBoxTemps.place(x=455,y=352,width=50, height=30)

    bouton_mode_geoquiz = StringVar()
    bouton_mode_geoquiz=Button(menu,command=wip, font=police1,relief=FLAT)
    bouton_mode_geoquiz.place(x=768,y=212,width=198, height=148)
    file_bouton_mode_geoquiz=geoquiz_location_path+"images/boutons/bouton_mode_geoquiz.png"
    image_bouton_mode_geoquiz = PhotoImage(file=file_bouton_mode_geoquiz)
    bouton_mode_geoquiz.configure(image=image_bouton_mode_geoquiz)
    bouton_mode_geoquiz.image = image_bouton_mode_geoquiz

    bouton_mode_aveugle = StringVar()
    bouton_mode_aveugle=Button(menu,command=wip, font=police1,relief=FLAT)
    bouton_mode_aveugle.place(x=974,y=212,width=198, height=148)
    file_bouton_mode_aveugle=geoquiz_location_path+"images/boutons/bouton_mode_aveugle.png"
    image_bouton_mode_aveugle = PhotoImage(file=file_bouton_mode_aveugle)
    bouton_mode_aveugle.configure(image=image_bouton_mode_aveugle)
    bouton_mode_aveugle.image = image_bouton_mode_aveugle

    bouton_mode_chrono = StringVar()
    bouton_mode_chrono=Button(menu,command=wip, font=police1,relief=FLAT)
    bouton_mode_chrono.place(x=1180,y=212,width=198, height=148)
    file_bouton_mode_chrono=geoquiz_location_path+"images/boutons/bouton_mode_chrono.png"
    image_bouton_mode_chrono = PhotoImage(file=file_bouton_mode_chrono)
    bouton_mode_chrono.configure(image=image_bouton_mode_chrono)
    bouton_mode_chrono.image = image_bouton_mode_chrono

    bouton_mode_br = StringVar()
    bouton_mode_br=Button(menu,command=wip, font=police1,relief=FLAT)
    bouton_mode_br.place(x=768,y=455,width=198, height=148)
    file_bouton_mode_br=geoquiz_location_path+"images/boutons/bouton_mode_br.png"
    image_bouton_mode_br = PhotoImage(file=file_bouton_mode_br)
    bouton_mode_br.configure(image=image_bouton_mode_br)
    bouton_mode_br.image = image_bouton_mode_br

    bouton_mode_blitz = StringVar()
    bouton_mode_blitz=Button(menu,command=wip, font=police1,relief=FLAT)
    bouton_mode_blitz.place(x=974,y=455,width=198, height=148)
    file_bouton_mode_blitz=geoquiz_location_path+"images/boutons/bouton_mode_blitz.png"
    image_bouton_mode_blitz = PhotoImage(file=file_bouton_mode_blitz)
    bouton_mode_blitz.configure(image=image_bouton_mode_blitz)
    bouton_mode_blitz.image = image_bouton_mode_blitz



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
file_background=geoquiz_location_path+"images/lobby_multi_serveur.png"
background = PhotoImage(file=file_background)
label_background.configure(image=background)
label_background.place(x=0,y=0,width=longueur, height=largeur)

local_ip=StringVar()

page_menu()
en_attente()


menu.mainloop()


ServerSideSocket.close()
