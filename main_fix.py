from tkinter import *
import tkinter.font as tkFont
from simplificateur import simp, simp_liste, simp_liste_p2, simp_liste_p3
import creation_questions
from nommer_questions import nommer_questions,espace_zero
from multi_client import connexion_client_multi,boucle_client_multi, deconnexion_multi
from random import *
import time
import os
import socket
import ast

#06.01.2022 : ajout de la création d'un shortcut sur le bureau lorsqu'on lance le jeu pour la première fois
def check_installed(pkg):
    try:
        __import__(pkg)
        return(True)
    except ModuleNotFoundError:
        return(False)

def install(package):
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if not check_installed('winshell'):
    install('winshell')
import winshell

from win32com.client import Dispatch

desktop = winshell.desktop()
path=os.path.join(desktop, "GéoQuiz.lnk")
target=os.path.join(os.path.dirname(os.path.abspath(__file__)), "main_fix.py")
wDir = desktop
icon=os.path.join(os.path.dirname(os.path.abspath(__file__)), "geoquiz.ico")
shell=Dispatch('WScript.shell')

shortcut=shell.CreateShortCut(path)
shortcut.Targetpath=target
shortcut.WorkingDirectory=wDir
shortcut.IconLocation=icon
shortcut.save()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Initialisation des pages XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


def page1(): # la page menu où l'on peut cliquer sur jouer, regle ou quitter
    global menu
    reset() #permet de supprimer tout ce qu'il y avait dans l'ancienne page pour recrer une nouvelle page
    menu.place(x=0, y=0)

    label_background = Label(menu, image="")
    file_background="images/menu.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)
    
    bouton_jouer = StringVar()
    bouton_jouer=Button(menu,command=page6, font=police1,relief=FLAT)
    bouton_jouer.place(x=505,y=289,width=429, height=97)
    file_bouton_jouer="images/boutons/bouton_jouer.png"
    image_bouton_jouer = PhotoImage(file=file_bouton_jouer)
    bouton_jouer.configure(image=image_bouton_jouer)
    bouton_jouer.image = image_bouton_jouer

    bouton_regles = StringVar()
    bouton_regles=Button(menu,command=page2, font=police1,relief=FLAT)
    bouton_regles.place(x=506,y=422,width=429, height=97)
    file_bouton_regles="images/boutons/bouton_regles.png"
    image_bouton_regles = PhotoImage(file=file_bouton_regles)
    bouton_regles.configure(image=image_bouton_regles)
    bouton_regles.image = image_bouton_regles

    bouton_quitter = StringVar()
    bouton_quitter=Button(menu,command=quitter, font=police1,relief=FLAT)
    bouton_quitter.place(x=506,y=548,width=429, height=97)
    file_bouton_quitter="images/boutons/bouton_quitter.png"
    image_bouton_quitter = PhotoImage(file=file_bouton_quitter)
    bouton_quitter.configure(image=image_bouton_quitter)
    bouton_quitter.image = image_bouton_quitter



def page2(): #page des regles
    global menu_regle
    reset()
    menu_regle.place(x=0, y=0)
    
    label_background = Label(menu_regle, image="")
    file_background="images/regles.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)
    
    bouton_retour = StringVar()
    bouton_retour=Button(menu_regle, text='Retour', command=retour, font=police1 ,bg = 'gray89')
    bouton_retour.place(x=1215,y=740,width=200, height=50)



def page3(): #la page de jeu en solo
    global jeu_solo
    global label_r1,label_r2,label_r3,label_r4,label_r5 #les labels des réponses
    global label_q1,label_q2,label_q3,label_q4,label_q5 #les labels des questions
    global temps_0,temps_1 #pour calculer le temps 
    
    reset()
    crea_question()
    jeu_solo.place(x=0, y=0)

    label_background = Label(jeu_solo, image="")
    file_background="images/fond_jeu.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)
    
    temps_0 = time.time()

    is_multi.set(0) #variable qui défini si le joueur joue en multijoueur (0=solo, 1=multi)
    temps_timer.set(0)

    bouton_abandon = StringVar()
    bouton_abandon=Button(jeu_solo, text='Abandonner', command=page5, font=police1 ,bg = 'gray89', fg = 'black')
    bouton_abandon.place(x=1204,y=740,width=200, height=50)

    textBoxReponse = Entry(jeu_solo, textvariable=var_reponse, width=40, font=police1, bg = 'gray89', fg = 'black')
    textBoxReponse.place(x=924,y=590,width=250, height=70)

    label_timer = Label(jeu_solo, textvariable=temps_timer, font=police2 , background = 'lightgrey', anchor='center', fg = 'black')
    label_timer.place(x=1224,y=590,width=100, height=70)

    label_q1 = Label(jeu_solo, textvariable=question1, font=police2 , background = 'lightgrey', anchor='center', fg = 'black')
    label_q1.place(x=74,y=90,width=800, height=70)

    label_q2 = Label(jeu_solo, textvariable=question2, font=police2, background = 'grey', anchor='center', fg = 'black')
    label_q2.place(x=74,y=190,width=800, height=70)

    label_q3 = Label(jeu_solo, textvariable=question3, font=police2, background = 'grey', anchor='center', fg = 'black')
    label_q3.place(x=74,y=290,width=800, height=70)

    label_q4 = Label(jeu_solo, textvariable=question4, font=police2, background = 'grey', anchor='center', fg = 'black')
    label_q4.place(x=74,y=390,width=800, height=70)

    label_q5 = Label(jeu_solo, textvariable=question5, font=police2, background = 'grey', anchor='center', fg = 'black')
    label_q5.place(x=74,y=490,width=800, height=70)


    label_r1 = Label(jeu_solo, textvariable=var_reponse, font=police1, background = 'lightgrey', anchor='center', fg = 'black')
    label_r1.place(x=924,y=90,width=400, height=70)

    label_r2 = Label(jeu_solo, textvariable=reponse_entree2, font=police1, background = 'grey', anchor='center')
    label_r2.place(x=924,y=190,width=400, height=70)

    label_r3 = Label(jeu_solo, textvariable=reponse_entree3, font=police1, background = 'grey', anchor='center')
    label_r3.place(x=924,y=290,width=400, height=70)

    label_r4 = Label(jeu_solo, textvariable=reponse_entree4, font=police1, background = 'grey', anchor='center')
    label_r4.place(x=924,y=390,width=400, height=70)

    label_r5 = Label(jeu_solo, textvariable=reponse_entree5, font=police1, background = 'grey', anchor='center')
    label_r5.place(x=924,y=490,width=400, height=70)

    update_temps() #lance le timer qui va se mettre a jour ensuite toutes les secondes



def page4(): # la page qui s'ouvre lorsque une partie est gagné en solo
    global gagne_solo
    global temps_0,temps_1

    temps_1 = time.time()
    temps=temps_1-temps_0 #calcul du temps mis par le joueur

    reset()

    label_background = Label(gagne_solo, image="")
    file_background="images/fin_solo_victoire.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)
    
    gagne_solo.place(x=0, y=0)
    label_q1 = Label(gagne_solo, text=str(round(temps))+'s', font=police1 , background = '#BBBBBB', anchor='w', fg = 'black')
    label_q1.place(x=730,y=117,width=100, height=40)

    bouton_rejouer = StringVar()
    bouton_rejouer=Button(gagne_solo, text='Rejouer', command=page3, font=police1 ,bg = 'gray89', fg = 'black')
    bouton_rejouer.place(x=1200,y=400,width=200, height=50)

    bouton_menu = StringVar()
    bouton_menu=Button(gagne_solo, text='Menu', command=retour, font=police1 ,bg = 'gray89', fg = 'black')
    bouton_menu.place(x=1200,y=475,width=200, height=50)

    bouton_quitter = StringVar()
    bouton_quitter=Button(gagne_solo, text='Quitter', command=quitter, font=police1 ,bg = 'gray89', fg = 'black')
    bouton_quitter.place(x=1200,y=550,width=200, height=50)


    champ_label_nom=Label(gagne_solo,textvariable=value_label_nom,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_nom.place(x=626,y=194,width=392, height=57)

    champ_label_capitale=Label(gagne_solo,textvariable=value_label_capitale,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_capitale.place(x=626,y=254,width=392, height=57)

    champ_label_continent=Label(gagne_solo,textvariable=value_label_continent,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_continent.place(x=626,y=315,width=392, height=57)

    champ_label_population=Label(gagne_solo,textvariable=value_label_population,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_population.place(x=626,y=385,width=392, height=57)

    champ_label_superficie=Label(gagne_solo,textvariable=value_label_superficie,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_superficie.place(x=626,y=445,width=392, height=57)

    champ_label_perimetre=Label(gagne_solo,textvariable=value_label_perimetre,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_perimetre.place(x=626,y=506,width=392, height=57)

    champ_label_langue=Label(gagne_solo,textvariable=value_label_langue,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_langue.place(x=626,y=566,width=392, height=57)
    

def page5(): # page qui s'affiche lorsqu'une personne abandonne en solo
    global perd_solo
    global temps_0, temps_1

    temps_1 = time.time()
    temps=temps_1-temps_0

    reset()
    perd_solo.place(x=0, y=0)

    label_background = Label(perd_solo, image="")
    file_background="images/fin_solo_abandon.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)

    label_temps = Label(perd_solo, text=str(round(temps))+'s', font=police1 , background = '#BBBBBB', anchor='w', fg = 'black')
    label_temps.place(x=730,y=117,width=100, height=40)

    bouton_rejouer = StringVar()
    bouton_rejouer=Button(perd_solo, text='Rejouer', command=page3, font=police1 ,bg = 'gray89', fg = 'black')
    bouton_rejouer.place(x=1200,y=400,width=200, height=50)

    bouton_menu = StringVar()
    bouton_menu=Button(perd_solo, text='Menu', command=retour, font=police1 ,bg = 'gray89', fg = 'black')
    bouton_menu.place(x=1200,y=475,width=200, height=50)

    bouton_quitter = StringVar()
    bouton_quitter=Button(perd_solo, text='Quitter', command=quitter, font=police1 ,bg = 'gray89', fg = 'black')
    bouton_quitter.place(x=1200,y=550,width=200, height=50)
    
    
    champ_label_nom=Label(perd_solo,textvariable=value_label_nom,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_nom.place(x=626,y=194,width=392, height=57)

    champ_label_capitale=Label(perd_solo,textvariable=value_label_capitale,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_capitale.place(x=626,y=254,width=392, height=57)

    champ_label_continent=Label(perd_solo,textvariable=value_label_continent,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_continent.place(x=626,y=315,width=392, height=57)

    champ_label_population=Label(perd_solo,textvariable=value_label_population,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_population.place(x=626,y=385,width=392, height=57)

    champ_label_superficie=Label(perd_solo,textvariable=value_label_superficie,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_superficie.place(x=626,y=445,width=392, height=57)

    champ_label_perimetre=Label(perd_solo,textvariable=value_label_perimetre,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_perimetre.place(x=626,y=506,width=392, height=57)

    champ_label_langue=Label(perd_solo,textvariable=value_label_langue,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_langue.place(x=626,y=566,width=392, height=57)


    
def page6(): # la page de séléction entre le jeu solo et le jeu multi
    global selec_jeu
    reset()
    selec_jeu.place(x=0, y=0)

    label_background = Label(selec_jeu, image="")
    file_background="images/menu_jouer.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)

    bouton_solo = StringVar()
    bouton_solo=Button(selec_jeu,command=page3, font=police1,relief=FLAT, fg = 'black')
    bouton_solo.place(x=506,y=360,width=429, height=97)
    file_bouton_solo="images/boutons/bouton_un_joueur.png"
    image_bouton_solo = PhotoImage(file=file_bouton_solo)
    bouton_solo.configure(image=image_bouton_solo)
    bouton_solo.image = image_bouton_solo

    bouton_multi = StringVar()
    bouton_multi=Button(selec_jeu,command=page8, font=police1,relief=FLAT, fg = 'black')
    bouton_multi.place(x=506,y=491,width=429, height=97)
    file_bouton_multi="images/boutons/bouton_multi.png"
    image_bouton_multi = PhotoImage(file=file_bouton_multi)
    bouton_multi.configure(image=image_bouton_multi)
    bouton_multi.image = image_bouton_multi

    bouton_retour = StringVar()
    bouton_retour=Button(selec_jeu,command=retour, font=police1,relief=FLAT, fg = 'black')
    bouton_retour.place(x=507,y=619,width=429, height=97)
    file_bouton_retour="images/boutons/bouton_retour.png"
    image_bouton_retour = PhotoImage(file=file_bouton_retour)
    bouton_retour.configure(image=image_bouton_retour)
    bouton_retour.image = image_bouton_retour



def page7(): # la page qui permet de rejoindre un serveur multi
    global recherche_multi

    reset()
    recherche_multi.place(x=0, y=0)

    label_background = Label(recherche_multi, image="")
    file_background="images/menu_jouer_multi_rejoindre.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)

    recherche_pseudo.set("Anonymous")

    textBoxPseudo = Entry(recherche_multi, textvariable=recherche_pseudo, width=40, font=police1, bg = 'gray89', fg = 'black')
    textBoxPseudo.place(x=525,y=397,width=396, height=60)
    
    textBoxIp = Entry(recherche_multi, textvariable=recherche_ip, width=40, font=police1, bg = 'gray89', fg = 'black')
    textBoxIp.place(x=525,y=522,width=396, height=60)

    bouton_quit_retour = StringVar()
    bouton_quit_retour=Button(recherche_multi, text='Retour au menu',command=retour, font=police1 ,bg = 'gray89', fg = 'black')
    bouton_quit_retour.place(x=1190,y=735,width=220, height=50)

    bouton_rejoindre = StringVar()
    bouton_rejoindre=Button(recherche_multi,command=connexion_serveur, font=police1,relief=FLAT, fg = 'black')
    bouton_rejoindre.place(x=507,y=619,width=429, height=97)
    file_bouton_rejoindre="images/boutons/bouton_rejoindre.png"
    image_bouton_rejoindre = PhotoImage(file=file_bouton_rejoindre)
    bouton_rejoindre.configure(image=image_bouton_rejoindre)
    bouton_rejoindre.image = image_bouton_rejoindre

    
  
def page8(): #la page de choix entre héberger et rejoindre une parti en multi
    global choix_multi
    reset()
    choix_multi.place(x=0, y=0)
    
    is_multi.set(1) # défini que le joueur est en multi

    label_background = Label(choix_multi, image="")
    file_background="images/menu_jouer_multi.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)

    bouton_solo = StringVar()
    bouton_solo=Button(choix_multi,command=lancer_serveur, font=police1,relief=FLAT, fg = 'black')
    bouton_solo.place(x=506,y=360,width=429, height=97)
    file_bouton_solo="images/boutons/bouton_heberger.png"
    image_bouton_solo = PhotoImage(file=file_bouton_solo)
    bouton_solo.configure(image=image_bouton_solo)
    bouton_solo.image = image_bouton_solo

    bouton_multi = StringVar()
    bouton_multi=Button(choix_multi,command=page7, font=police1,relief=FLAT, fg = 'black')
    bouton_multi.place(x=506,y=492,width=429, height=97)
    file_bouton_multi="images/boutons/bouton_rejoindre.png"
    image_bouton_multi = PhotoImage(file=file_bouton_multi)
    bouton_multi.configure(image=image_bouton_multi)
    bouton_multi.image = image_bouton_multi

    bouton_retour = StringVar()
    bouton_retour=Button(choix_multi,command=retour, font=police1,relief=FLAT, fg = 'black')
    bouton_retour.place(x=507,y=619,width=429, height=97)
    file_bouton_retour="images/boutons/bouton_retour.png"
    image_bouton_retour = PhotoImage(file=file_bouton_retour)
    bouton_retour.configure(image=image_bouton_retour)
    bouton_retour.image = image_bouton_retour


    
def page9(): # page qui s'affiche lorsqu'on est connecté au serveur en attendant que le serveur lance la partie
    global lobby_multi  
    reset()
    lobby_multi.place(x=0, y=0)

    hostname = socket.gethostname()
    local_ip.set(socket.gethostbyname(hostname)) #permet d'afficher son ip

    label_background = Label(lobby_multi, image="")
    file_background="images/lobby_multi_client.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)

    label_ip = Label(lobby_multi, textvariable=local_ip, font=police1, background = 'lightgrey', anchor='center', fg = 'black')
    label_ip.place(x=860,y=715,width=300, height=70)
  
    bouton_quit_retour = StringVar()
    bouton_quit_retour=Button(lobby_multi, text='Retour au menu',command=quitter_multi, font=police1, fg = 'black')
    bouton_quit_retour.place(x=1190,y=735,width=220, height=50)



def page10(): #page du jeu en mode multijoueur
    global jeu_multi
    global label_r1,label_r2,label_r3,label_r4,label_r5
    global label_q1,label_q2,label_q3,label_q4,label_q5
    global temps_0,temps_1
    
    reset()
    crea_question()
    jeu_multi.place(x=0, y=0)

    temps_0 = time.time()
    temps_timer.set(0)

    label_background = Label(jeu_multi, image="")
    file_background="images/fond_jeu.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)

    bouton_abandon = StringVar()
    bouton_abandon=Button(jeu_multi, text='Abandonner', command=abandon, font=police1 ,bg = 'gray89', fg = 'black')
    bouton_abandon.place(x=1204,y=740,width=200, height=50)

    textBoxReponse = Entry(jeu_multi, textvariable=var_reponse, width=40, font=police1, bg = 'yellow', fg = 'black')
    textBoxReponse.place(x=924,y=590,width=250, height=70)

    label_timer = Label(jeu_multi, textvariable=temps_timer, font=police2 , background = 'lightgrey', anchor='center', fg = 'black')
    label_timer.place(x=1224,y=590,width=100, height=70)

    label_q1 = Label(jeu_multi, textvariable=question1, font=police2 , background = 'lightgrey', anchor='center', fg = 'black')
    label_q1.place(x=74,y=90,width=800, height=70)

    label_q2 = Label(jeu_multi, textvariable=question2, font=police2, background = 'grey', anchor='center', fg = 'black')
    label_q2.place(x=74,y=190,width=800, height=70)

    label_q3 = Label(jeu_multi, textvariable=question3, font=police2, background = 'grey', anchor='center', fg = 'black')
    label_q3.place(x=74,y=290,width=800, height=70)

    label_q4 = Label(jeu_multi, textvariable=question4, font=police2, background = 'grey', anchor='center', fg = 'black')
    label_q4.place(x=74,y=390,width=800, height=70)

    label_q5 = Label(jeu_multi, textvariable=question5, font=police2, background = 'grey', anchor='center', fg = 'black')
    label_q5.place(x=74,y=490,width=800, height=70)


    label_r1 = Label(jeu_multi, textvariable=var_reponse, font=police1, background = 'lightgrey', anchor='center', fg = 'black')
    label_r1.place(x=924,y=90,width=400, height=70)

    label_r2 = Label(jeu_multi, textvariable=reponse_entree2, font=police1, background = 'grey', anchor='center', fg = 'black')
    label_r2.place(x=924,y=190,width=400, height=70)

    label_r3 = Label(jeu_multi, textvariable=reponse_entree3, font=police1, background = 'grey', anchor='center', fg = 'black')
    label_r3.place(x=924,y=290,width=400, height=70)

    label_r4 = Label(jeu_multi, textvariable=reponse_entree4, font=police1, background = 'grey', anchor='center', fg = 'black')
    label_r4.place(x=924,y=390,width=400, height=70)

    label_r5 = Label(jeu_multi, textvariable=reponse_entree5, font=police1, background = 'grey', anchor='center', fg = 'black')
    label_r5.place(x=924,y=490,width=400, height=70)

    update_temps()


def page11(): # page qui s'affiche lorsqu'une personne gagne en multijoueur
    global gagne_multi
    global temps_0, temps_1

    temps_1 = time.time()
    temps=temps_1-temps_0

    reset()
    gagne_multi.place(x=0, y=0)

    label_background = Label(gagne_multi, image="")
    file_background="images/fin_multi.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)

    label_q1 = Label(gagne_multi, text='Bravo vous avez mis '+str(round(temps))+'s', font=police1 , background = 'grey', anchor='center', fg = 'black')
    label_q1.place(x=670,y=650,width=500, height=70)

    bouton_retour = StringVar()
    bouton_retour=Button(gagne_multi, text='Retour au lobby', command=page9, font=police1, fg = 'black')
    bouton_retour.place(x=740,y=730,width=350, height=50)

    champ_label_nom=Label(gagne_multi,textvariable=value_label_nom,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_nom.place(x=835,y=204,width=392, height=57)

    champ_label_capitale=Label(gagne_multi,textvariable=value_label_capitale,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_capitale.place(x=835,y=264,width=392, height=57)

    champ_label_continent=Label(gagne_multi,textvariable=value_label_continent,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_continent.place(x=835,y=325,width=392, height=57)

    champ_label_population=Label(gagne_multi,textvariable=value_label_population,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_population.place(x=835,y=392,width=392, height=57)

    champ_label_superficie=Label(gagne_multi,textvariable=value_label_superficie,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_superficie.place(x=835,y=453,width=392, height=57)

    champ_label_perimetre=Label(gagne_multi,textvariable=value_label_perimetre,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_perimetre.place(x=835,y=514,width=392, height=57)

    champ_label_langue=Label(gagne_multi,textvariable=value_label_langue,bg="#BBBBBB", font=police1, fg = 'black')
    champ_label_langue.place(x=835,y=575,width=392, height=57)


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Initialisation des fonctions qui servent pour la création du jeu XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


def crea_question():

    global liste_attributs, liste_valeurs, liste_reponses, liste_questions, liste_infos # récupère les listes des questions et réponses à générer

    if is_multi.get()==0: # si la personne joue en solo, la seed est générer maintenant
        liste_attributs, liste_valeurs, liste_reponses,liste_infos = creation_questions.lancer_tirage(randint(1,1000000)) #envoi de la seed au programme creations_questions qui va ensuite lui renvoyer la liste des questions (themes + valeurs) et la liste des réponses 

    else : # si la personne joue en multi, récupere la seed envoyé par le serveur
        #print('la seed est :'+seed_serveur.get())
        liste_attributs, liste_valeurs, liste_reponses, liste_infos = creation_questions.lancer_tirage(seed_serveur.get())

    liste_questions=nommer_questions(liste_attributs,liste_valeurs) #permet de nommer les questions (ex: La capitale est Paris) avec la liste des attributs (ex: capitale) et la liste des valeurs (ex : Paris)

    question1.set(liste_questions[0]) # defini le premiere question

    # défini les infos du pays gagnant
    value_label_nom.set(liste_infos[0])
    value_label_capitale.set(liste_infos[1])
    value_label_continent.set(liste_infos[2])
    value_label_population.set(str(espace_zero(liste_infos[3]))+' hab')
    value_label_superficie.set(str(espace_zero(liste_infos[4]))+' m²')
    value_label_perimetre.set(str(espace_zero(liste_infos[5]))+' m')
    value_label_langue.set(liste_infos[6])



def test_reponse(): # teste si la réponse entré est juste (à chaque touche du clavier appuyé), cela permet de ne pas avoir à appuyer sur un bouton pour valider sa réponse

    global liste_attributs, liste_valeurs, liste_reponses, liste_questions

    try :
        
        reponse_simp=simp(var_reponse.get()) # simplifie la reponse
        nb_reponse_juste_fct=nb_reponse_juste.get() #recupere le nombre de réponses deja justes
        liste_reponses_simp=simp_liste_p3(liste_reponses) # siplifie la liste des reponses
        
        for i in range (len(liste_reponses[nb_reponse_juste_fct])): # test si la reponse entrée est la meme qu'une dans la liste des reponses justes
           
            if str(reponse_simp) == liste_reponses_simp[nb_reponse_juste_fct][i][0]: # si la reponses est justes
                              
                nb_reponse_juste.set(nb_reponse_juste.get()+1)

                # changement des couleurs des labels en fonctions du nombres de réponses justes
                if nb_reponse_juste.get() == 1:
                    reponse_entree1.set(liste_reponses[nb_reponse_juste_fct][i][0])
                    label_r1.configure(textvariable=reponse_entree1,background ='lightgreen', fg = 'black')
                    label_r2.configure(textvariable=var_reponse,background ='lightgrey', fg = 'black')
                    label_q1.configure(background ='lightgreen', fg = 'black')
                    label_q2.configure(background ='lightgrey', fg = 'black')
                    question2.set(liste_questions[1])
                    var_reponse.set('')
                    
                if nb_reponse_juste.get() == 2:
                    reponse_entree2.set(liste_reponses[nb_reponse_juste_fct][i][0])
                    label_r2.configure(textvariable=reponse_entree2,background ='lightgreen', fg = 'black')
                    label_r3.configure(textvariable=var_reponse,background ='lightgrey', fg = 'black')
                    label_q2.configure(background ='lightgreen', fg = 'black')
                    label_q3.configure(background ='lightgrey', fg = 'black')
                    question3.set(liste_questions[2])
                    
                if nb_reponse_juste.get() == 3:
                    reponse_entree3.set(liste_reponses[nb_reponse_juste_fct][i][0])
                    label_r3.configure(textvariable=reponse_entree3,background ='lightgreen', fg = 'black')
                    label_r4.configure(textvariable=var_reponse,background ='lightgrey', fg = 'black')
                    label_q3.configure(background ='lightgreen', fg = 'black')
                    label_q4.configure(background ='lightgrey', fg = 'black')
                    question4.set(liste_questions[3])
                    
                if nb_reponse_juste.get() == 4:
                    reponse_entree4.set(liste_reponses[nb_reponse_juste_fct][i][0])
                    label_r4.configure(textvariable=reponse_entree4,background ='lightgreen', fg = 'black')
                    label_r5.configure(textvariable=var_reponse,background ='lightgrey', fg = 'black')
                    label_q4.configure(background ='lightgreen', fg = 'black')
                    label_q5.configure(background ='lightgrey', fg = 'black')
                    question5.set(liste_questions[4])
                    
                if nb_reponse_juste.get() == 5: #gagné
                    reponse_entree5.set(liste_reponses[nb_reponse_juste_fct][i][0])
                    label_r5.configure(textvariable=reponse_entree5,background ='lightgreen', fg = 'black')
                    label_q5.configure(background ='lightgreen', fg = 'black')

                    if is_multi.get() == 0 : #si le joueur joue en solo, envoi vers l'écran de victoire solo
                        page4()
                    else : # si en multi, envoi vers l'écran de victoire multi
                        page11()
                    
                var_reponse.set('')
    except:None



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Initialisation des fonctions qui servent pour le jeu XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

     
def abandon(): # affiche la reponse dans la textbox reponse en solo lorsque le bouton abandon est cliqué (plus tard la fonction revoira à une page d'abandon)
    var_reponse.set(str(liste_reponses[4][0][0]))


def update_temps(): # met à jour le timer toutes les secondes
    global temps_0, temps_1
    temps_1 = time.time()
    temps_timer.set(round(temps_1-temps_0))
    fenetre.after(1000,update_temps)
    



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Initialisation des fonctions qui servent pour le client/serveur XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


def lancer_serveur(): #lorsque que le bouton hebergé est cliqué, le programme serveur est lancé et la page rejoindre serveur en localhost aussi
    os.startfile("multi_serveur.py")
    recherche_ip.set("localhost")
    page7()

def connexion_serveur(): #fonction qui essaye de connecter le client au serveur en en voyant l'ip et le pseudo au serveur, si il existe
    pseudo=recherche_pseudo.get()
    ip=recherche_ip.get()
    etat_multi.set(connexion_client_multi(pseudo,ip)) # la variable etat multi contient l'esnsemble des donnees transmises par/pour le serveur
    
    if etat_multi.get()=="aucun_serveur_accessible":
        page8()
    else:
        discussion_serveur()
    page9()
    

def discussion_serveur(): # fonction répété chaque seconde pour essayer de connecter le client au serveur et de détecter les ordres comme le lancement de la partie ...

    if is_multi.get()==1: # si le joueur est en multi
        if "aucun_serveur_accessible" in etat_multi.get(): # si il n'y a pas de serveur
            page8()
        else :
            pseudo=recherche_pseudo.get()
            ip=recherche_ip.get()
            etat_multi.set(boucle_client_multi(pseudo,ip))

        if "lancement_partie" in etat_multi.get() : #si le serveur envoi l'ordre de lancer la partie
            etat_multi.set(str(etat_multi.get()).replace("lancement_partie",""))
            etat_multi.set(str(etat_multi.get()).replace("en_attente",""))
            seed_serveur.set(int(etat_multi.get())) #récupere la seed apres avoir enlevé les ordres dans la variables
            page10() #lance la page de jeu multi

        #print('update toutes les secondes ...')
        fenetre.after(1000,discussion_serveur)


def quitter_multi(): # fonction qui permet de quitter proprement le multijoueur en envoyant un message au serveur pour qu'il ne crash pas 
    pseudo=recherche_pseudo.get()
    ip=recherche_ip.get()
    deconnexion_multi(pseudo,ip)
    is_multi.set(0)
    retour()





#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Initialisation des fonctions qui servent pour l'infrastructure XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


def reset(): # permet de supprimer tout ce qu'il y a dans la fenetre tkinter afin de créer une nouvelle page
    global menu,jeu_solo,jeu_multi,gagne_solo,gagne_multi,lobby_multi,selec_jeu,choix_multi,recherche_multi,menu_regle,perd_solo # appel global de chaque page
    global label_r1,label_r2,label_r3,label_r4,label_r5 # appel global des labels réponses
    global nombre_personne

    # destruction de toute les pages
    menu.destroy()
    menu_regle.destroy()
    jeu_solo.destroy()
    gagne_solo.destroy()
    perd_solo.destroy()
    selec_jeu.destroy()
    recherche_multi.destroy()
    choix_multi.destroy()
    lobby_multi.destroy()
    jeu_multi.destroy()
    gagne_multi.destroy()


    
    
    # definition de toutes les pages (au cas ou)
    menu = Canvas(fenetre, width=longueur, height=largeur)
    menu_regle = Canvas(fenetre,width=longueur, height=largeur)
    jeu_solo = Canvas(fenetre, width=longueur, height=largeur)
    gagne_solo = Canvas(fenetre, width=longueur, height=largeur)
    perd_solo = Canvas(fenetre, width=longueur, height=largeur)
    selec_jeu = Canvas(fenetre, width=longueur, height=largeur)
    recherche_multi = Canvas(fenetre, width=longueur, height=largeur)
    choix_multi = Canvas(fenetre, width=longueur, height=largeur)
    lobby_multi = Canvas(fenetre, width=longueur, height=largeur)
    jeu_multi = Canvas(fenetre, width=longueur, height=largeur)
    gagne_multi = Canvas(fenetre, width=longueur, height=largeur)



    #reset de chaque valeur entree
    reponse_entree1.set('')
    reponse_entree2.set('')
    reponse_entree3.set('')
    reponse_entree4.set('')
    reponse_entree5.set('')
    var_reponse.set('')
    question2.set('')
    question3.set('')
    question4.set('')
    question5.set('')
    nb_reponse_juste.set(0) #remet le compteur de reponses justes à 0

    nombre_personne=0 #remet le compteur de personne connecté en multi à 0


def new_envent_lobby(): # PAS ENCORE IMPLEMENTE (permettra d'avoir la liste des joueurs connecté en multi sur le lobby et leur nombre de points)
    global nombre_personne
    nombre_personne=nombre_personne+1
    liste_personne=[]
    label_personne = Label(lobby_multi, text=liste_personne[nombre_personne-1], font=police2, background = 'grey', anchor='center', fg = 'black')
    label_personne.place(x=50,y=50+(80*nombre_personne),width=400, height=70)
    label_score = Label(lobby_multi, text='0', font=police2, background = 'lightgrey', anchor='center', fg = 'black')
    label_score.place(x=450,y=50+(80*nombre_personne),width=100, height=70)


def callback(key): # lorsqu'une touche est appuyé, appel la focntion qui va tester si la reponse entré est juste
    test_reponse()

def echap(key): # lorsque le touche echap est appuyé, cela fait revenir au menu principal
    retour()
    
def retour(): # revient à la page 1, (plus tard cela fera revenir juste à la page précédante grace à une pile)
    page1()

def meme_reponse(key): # lorsque la touche control est appuyé, remet la derniere reponse juste dans la textbox et test si c'est encore juste
    if nb_reponse_juste.get()> 0:
        var_reponse.set(eval('reponse_entree'+str(nb_reponse_juste.get())).get())
        test_reponse()

def quitter():   #fermer proprement la fenetre geoquizz
    fenetre.destroy()



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Création de la fenetre tkinter XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

longueur = '1440'
largeur = '810'

fenetre = Tk()
fenetre.geometry(longueur+'x'+largeur)
fenetre.title('GéoQuiz')
police1=tkFont.Font(family="MV Boli",size=20)
police2=tkFont.Font(family="MV Boli",size=16)

menu = Canvas(fenetre, width=longueur, height=largeur)
menu_regle = Canvas(fenetre,width=longueur, height=largeur)
jeu_solo = Canvas(fenetre, width=longueur, height=largeur)
gagne_solo = Canvas(fenetre, width=longueur, height=largeur)
perd_solo = Canvas(fenetre, width=longueur, height=largeur)
selec_jeu = Canvas(fenetre, width=longueur, height=largeur)
recherche_multi = Canvas(fenetre, width=longueur, height=largeur)
choix_multi = Canvas(fenetre, width=longueur, height=largeur)
lobby_multi = Canvas(fenetre, width=longueur, height=largeur)
jeu_multi = Canvas(fenetre, width=longueur, height=largeur)
gagne_multi = Canvas(fenetre, width=longueur, height=largeur)


# permet d'associer la touche d'une touche du clavier à une fonction :

fenetre.bind('<KeyPress>', callback)
fenetre.bind('<Escape>', echap)
fenetre.bind('<Control_L>', meme_reponse)

nombre_personne=0 # ne sert pas encore



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Définition de toutes les variables StringVar (permet d'éviter de mettre des globals) XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

var_reponse = StringVar()
nb_reponse_juste = IntVar()

reponse_entree1=StringVar()
reponse_entree2=StringVar()
reponse_entree3=StringVar()
reponse_entree4=StringVar()
reponse_entree5=StringVar()

reponse_entree1_simp=StringVar()
reponse_entree2_simp=StringVar()
reponse_entree3_simp=StringVar()
reponse_entree4_simp=StringVar()
reponse_entree5_simp=StringVar()

question1=StringVar()
question2=StringVar()
question3=StringVar()
question4=StringVar()
question5=StringVar()

value_label_nom = StringVar()
value_label_capitale = StringVar()
value_label_continent = StringVar()
value_label_population = StringVar()
value_label_superficie = StringVar()
value_label_perimetre = StringVar()
value_label_langue = StringVar()

local_ip=StringVar()

temps_timer=StringVar()

is_multi = IntVar()

recherche_ip=StringVar()
recherche_pseudo=StringVar()

etat_multi=StringVar() # La variable contient les données transmises par le serveur, il peut y avoir la seed, le lancement de la partie, une personne qui se déconnecte/connecte ...

seed_serveur=StringVar()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Lancement du jeu (ENFIN !) XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

page1()
menu.mainloop()
