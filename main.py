from tkinter import *
import tkinter.font as tkFont
from simplificateur import simp, simp_liste, simp_liste_p2, simp_liste_p3
import creation_questions
from nommer_questions import nommer_questions
import time
import os
import socket
from multi_client import connexion_client_multi,boucle_client_multi, deconnexion_multi
import ast
from random import *

def page1(xx,yy):
    global menu
    reset()
    menu.place(x=0, y=0)

    label_background = Label(menu, image="")
    file_background="images/menu.png"
    background = PhotoImage(file=file_background)
    label_background.configure(image=background)
    label_background.image = background
    label_background.place(x=0,y=0,width=longueur, height=largeur)
    
    
    bouton_jouer = StringVar()
    bouton_jouer=Button(menu, text='Jouer',command=page4, font=police1)
    bouton_jouer.place(x=xx,y=yy,width=200, height=50)


    bouton_quit = StringVar()
    bouton_quit=Button(menu, text='Quitter',command=quitter, font=police1)
    bouton_quit.place(x=(int(longueur)/2)-100,y=550,width=200, height=50)

    
    #print('p1 appelé')

    menu.bind('<Motion>', motion)



def page2():
    global jeu_solo
    global label_r1,label_r2,label_r3,label_r4,label_r5
    global label_q1,label_q2,label_q3,label_q4,label_q5
    
    global temps_0
    
    reset()
    crea_question()
    jeu_solo.place(x=0, y=0)

    temps_0 = time.time()

    is_multi.set(0)
    temps_timer.set(0)

    bouton_retour = StringVar()
    bouton_retour=Button(jeu_solo, text='Retour', command=retour, font=police1)
    bouton_retour.place(x=int(longueur)-210,y=int(largeur)-60,width=200, height=50)

    bouton_abandon = StringVar()
    bouton_abandon=Button(jeu_solo, text='Abandonner', command=abandon, font=police1)
    bouton_abandon.place(x=int(longueur)-420,y=int(largeur)-60,width=200, height=50)

    #print('p2 appelé')

    textBoxReponse = Entry(jeu_solo, textvariable=var_reponse, width=40, font=police1, bg = 'yellow')
    textBoxReponse.place(x=950,y=600,width=250, height=70)

    label_timer = Label(jeu_solo, textvariable=temps_timer, font=police2 , background = 'lightgrey', anchor='center')
    label_timer.place(x=1250,y=600,width=100, height=70)

    label_q1 = Label(jeu_solo, textvariable=question1, font=police2 , background = 'lightgrey', anchor='center')
    label_q1.place(x=100,y=100,width=800, height=70)

    label_q2 = Label(jeu_solo, textvariable=question2, font=police2, background = 'grey', anchor='center')
    label_q2.place(x=100,y=200,width=800, height=70)

    label_q3 = Label(jeu_solo, textvariable=question3, font=police2, background = 'grey', anchor='center')
    label_q3.place(x=100,y=300,width=800, height=70)

    label_q4 = Label(jeu_solo, textvariable=question4, font=police2, background = 'grey', anchor='center')
    label_q4.place(x=100,y=400,width=800, height=70)

    label_q5 = Label(jeu_solo, textvariable=question5, font=police2, background = 'grey', anchor='center')
    label_q5.place(x=100,y=500,width=800, height=70)


    label_r1 = Label(jeu_solo, textvariable=var_reponse, font=police1, background = 'lightgrey', anchor='center')
    label_r1.place(x=950,y=100,width=400, height=70)

    label_r2 = Label(jeu_solo, textvariable=reponse_entree2, font=police1, background = 'grey', anchor='center')
    label_r2.place(x=950,y=200,width=400, height=70)

    label_r3 = Label(jeu_solo, textvariable=reponse_entree3, font=police1, background = 'grey', anchor='center')
    label_r3.place(x=950,y=300,width=400, height=70)

    label_r4 = Label(jeu_solo, textvariable=reponse_entree4, font=police1, background = 'grey', anchor='center')
    label_r4.place(x=950,y=400,width=400, height=70)

    label_r5 = Label(jeu_solo, textvariable=reponse_entree5, font=police1, background = 'grey', anchor='center')
    label_r5.place(x=950,y=500,width=400, height=70)

    update_temps()


def page3():
    global gagne_solo
    global temps_0
    global temps_1

    temps_1 = time.time()
    temps=temps_1-temps_0

    reset()
    gagne_solo.place(x=0, y=0)
    label_q1 = Label(gagne_solo, text='Bien-joué tu as mis : '+str(round(temps))+'s', font=police1 , background = 'grey', anchor='center')
    label_q1.place(x=(int(longueur)/2)-250,y=200,width=500, height=70)


    bouton_rejouer = StringVar()
    bouton_rejouer=Button(gagne_solo, text='Rejouer', command=page2, font=police1)
    bouton_rejouer.place(x=(int(longueur)/2)-100,y=400,width=200, height=50)

    bouton_menu = StringVar()
    bouton_menu=Button(gagne_solo, text='Menu', command=retour, font=police1)
    bouton_menu.place(x=(int(longueur)/2)-100,y=475,width=200, height=50)

    bouton_quitter = StringVar()
    bouton_quitter=Button(gagne_solo, text='Quitter', command=quitter, font=police1)
    bouton_quitter.place(x=(int(longueur)/2)-100,y=550,width=200, height=50)
    

def page4():
    global selec_jeu
    reset()
    selec_jeu.place(x=0, y=0)
    
    bouton_solo = StringVar()
    bouton_solo=Button(selec_jeu, text='Solo',command=page2, font=police1)
    bouton_solo.place(x=(int(longueur)/2)-100,y=450,width=200, height=50)


    bouton_multi = StringVar()
    bouton_multi=Button(selec_jeu, text='Multijoueur',command=page5, font=police1)
    bouton_multi.place(x=(int(longueur)/2)-100,y=550,width=200, height=50)

    bouton_retour = StringVar()
    bouton_retour=Button(selec_jeu, text='Retour',command=retour, font=police1)
    bouton_retour.place(x=(int(longueur)/2)-100,y=650,width=200, height=50)

    
    image_logo = Label(selec_jeu, image="")
    file_logo="logo.png"
    logo = PhotoImage(file=file_logo)
    image_logo.configure(image=logo)
    image_logo.image = logo
    image_logo.place(x=440,y=150,width=624, height=240)

def page5():
    global choix_multi
    reset()
    choix_multi.place(x=0, y=0)

    is_multi.set(1)
    print("multi? : "+str(is_multi.get()))
    
    bouton_solo = StringVar()
    bouton_solo=Button(choix_multi, text='Créer partie',command=lancer_serveur, font=police1)
    bouton_solo.place(x=(int(longueur)/2)-90,y=450,width=220, height=50)


    bouton_multi = StringVar()
    bouton_multi=Button(choix_multi, text='Rejoindre partie',command=page6, font=police1)
    bouton_multi.place(x=(int(longueur)/2)-90,y=550,width=220, height=50)

    bouton_retour = StringVar()
    bouton_retour=Button(choix_multi, text='Retour',command=retour, font=police1)
    bouton_retour.place(x=(int(longueur)/2)-90,y=650,width=220, height=50)

    
    image_logo = Label(choix_multi, image="")
    file_logo="logo.png"
    logo = PhotoImage(file=file_logo)
    image_logo.configure(image=logo)
    image_logo.image = logo
    image_logo.place(x=440,y=150,width=624, height=240)

def page6():
    global recherche_multi

    reset()
    recherche_multi.place(x=0, y=0)

    recherche_pseudo.set("Anonymous")

    textBoxPseudo = Entry(recherche_multi, textvariable=recherche_pseudo, width=40, font=police1, bg = 'yellow')
    textBoxPseudo.place(x=550,y=200,width=250, height=70)
    textBoxIp = Entry(recherche_multi, textvariable=recherche_ip, width=40, font=police1, bg = 'yellow')
    textBoxIp.place(x=550,y=300,width=250, height=70)


    bouton_rechercher = StringVar()
    bouton_rechercher=Button(recherche_multi, text='Rechercher le serveur', command=connexion_serveur, font=police1)
    bouton_rechercher.place(x=850,y=300,width=350, height=50)

    bouton_quit_retour = StringVar()
    bouton_quit_retour=Button(recherche_multi, text='Retour au menu',command=retour, font=police1)
    bouton_quit_retour.place(x=1190,y=735,width=220, height=50)
    

def page7():
    global lobby_multi

    hostname = socket.gethostname()
    local_ip.set(socket.gethostbyname(hostname))
    
    reset()
    lobby_multi.place(x=0, y=0)

    
    image_logo = Label(lobby_multi, image="")
    file_logo="logo.png"
    logo = PhotoImage(file=file_logo)
    image_logo.configure(image=logo)
    image_logo.image = logo
    image_logo.place(x=640,y=450,width=624, height=240)

    label_ip = Label(lobby_multi, textvariable=local_ip, font=police1, background = 'lightgrey', anchor='center')
    label_ip.place(x=860,y=715,width=300, height=70)
    """
    bouton_soloaaa = StringVar()
    bouton_soloaaa=Button(lobby_multi, text='Créer partie',command=new_envent_lobby, font=police1)
    bouton_soloaaa.place(x=1000-90,y=450,width=220, height=50)

    bouton_jouer_multi = StringVar()
    bouton_jouer_multi=Button(lobby_multi, text='Jouer',command=page8, font=police1)
    bouton_jouer_multi.place(x=1000-90,y=350,width=220, height=50)
    """
    bouton_quit_retour = StringVar()
    bouton_quit_retour=Button(lobby_multi, text='Retour au menu',command=quitter_multi, font=police1)
    bouton_quit_retour.place(x=1190,y=735,width=220, height=50)





    #new_event_lobby()


def page8():
    global jeu_multi
    global label_r1,label_r2,label_r3,label_r4,label_r5
    global label_q1,label_q2,label_q3,label_q4,label_q5
    global temps_0
    
    reset()
    crea_question()
    jeu_multi.place(x=0, y=0)

    temps_0 = time.time()

    temps_timer.set(0)
    """
    bouton_abandon = StringVar()
    bouton_abandon=Button(jeu_multi, text='Abandonner (à enlever après)', command=abandon, font=police1)
    bouton_abandon.place(x=int(longueur)-420,y=int(largeur)-60,width=200, height=50)
    """
    #print('p2 appelé')

    label_timer = Label(jeu_multi, textvariable=temps_timer, font=police2 , background = 'lightgrey', anchor='center')
    label_timer.place(x=1250,y=600,width=100, height=70)

    textBoxReponse = Entry(jeu_multi, textvariable=var_reponse, width=40, font=police1, bg = 'yellow')
    textBoxReponse.place(x=950,y=600,width=250, height=70)

    label_q1 = Label(jeu_multi, textvariable=question1, font=police2 , background = 'lightgrey', anchor='center')
    label_q1.place(x=100,y=100,width=800, height=70)

    label_q2 = Label(jeu_multi, textvariable=question2, font=police2, background = 'grey', anchor='center')
    label_q2.place(x=100,y=200,width=800, height=70)

    label_q3 = Label(jeu_multi, textvariable=question3, font=police2, background = 'grey', anchor='center')
    label_q3.place(x=100,y=300,width=800, height=70)

    label_q4 = Label(jeu_multi, textvariable=question4, font=police2, background = 'grey', anchor='center')
    label_q4.place(x=100,y=400,width=800, height=70)

    label_q5 = Label(jeu_multi, textvariable=question5, font=police2, background = 'grey', anchor='center')
    label_q5.place(x=100,y=500,width=800, height=70)


    label_r1 = Label(jeu_multi, textvariable=var_reponse, font=police1, background = 'lightgrey', anchor='center')
    label_r1.place(x=950,y=100,width=400, height=70)

    label_r2 = Label(jeu_multi, textvariable=reponse_entree2, font=police1, background = 'grey', anchor='center')
    label_r2.place(x=950,y=200,width=400, height=70)

    label_r3 = Label(jeu_multi, textvariable=reponse_entree3, font=police1, background = 'grey', anchor='center')
    label_r3.place(x=950,y=300,width=400, height=70)

    label_r4 = Label(jeu_multi, textvariable=reponse_entree4, font=police1, background = 'grey', anchor='center')
    label_r4.place(x=950,y=400,width=400, height=70)

    label_r5 = Label(jeu_multi, textvariable=reponse_entree5, font=police1, background = 'grey', anchor='center')
    label_r5.place(x=950,y=500,width=400, height=70)

    update_temps()


def page9():
    global gagne_multi
    global temps_0
    global temps_1

    temps_1 = time.time()
    temps=temps_1-temps_0

    reset()
    gagne_multi.place(x=0, y=0)
    label_q1 = Label(gagne_multi, text='Bien-joué tu as mis : '+str(round(temps))+'s', font=police1 , background = 'grey', anchor='center')
    label_q1.place(x=(int(longueur)/2)-250,y=200,width=500, height=70)


    bouton_rejouer = StringVar()
    bouton_rejouer=Button(gagne_multi, text='Retour au lobby', command=page7, font=police1)
    bouton_rejouer.place(x=(int(longueur)/2)-100,y=500,width=350, height=50)


def connexion_serveur():
    pseudo=recherche_pseudo.get()
    ip=recherche_ip.get()
    etat_multi.set(connexion_client_multi(pseudo,ip))
    
    if etat_multi.get()=="aucun_serveur_accessible":
        page5()
    else:
        discussion_serveur()
    page7()
    
def discussion_serveur():

    if is_multi.get()==1:

        if "aucun_serveur_accessible" in etat_multi.get():
            page5()
        else :
            pseudo=recherche_pseudo.get()
            ip=recherche_ip.get()
            etat_multi.set(boucle_client_multi(pseudo,ip))
        

        if "lancement_partie" in etat_multi.get() :
            etat_multi.set(str(etat_multi.get()).replace("lancement_partie",""))
            etat_multi.set(str(etat_multi.get()).replace("en_attente",""))
            seed_serveur.set(int(etat_multi.get()))
            page8()


        #print('update toutes les secondes ...')
        fenetre.after(1000,discussion_serveur)


#def lancer_boucle():


def quitter_multi():
    pseudo=recherche_pseudo.get()
    ip=recherche_ip.get()
    deconnexion_multi(pseudo,ip)
    is_multi.set(0)
    retour()


def reset():
    global menu
    global jeu_solo
    global jeu_multi
    global gagne_solo
    global gagne_multi
    global lobby_multi
    global selec_jeu
    global choix_multi
    global recherche_multi
    global connexion_au_serveur
    global label_r1
    global label_r2
    global label_r3
    global label_r4
    global label_r5
    global nombre_personne

    
    menu.destroy()
    jeu_solo.destroy()
    jeu_multi.destroy()
    gagne_solo.destroy()
    gagne_multi.destroy()
    lobby_multi.destroy()
    selec_jeu.destroy()
    choix_multi.destroy()
    recherche_multi.destroy()
    connexion_au_serveur.destroy
    menu = Canvas(fenetre, width=longueur, height=largeur)
    jeu_solo = Canvas(fenetre, width=longueur, height=largeur)
    gagne_solo = Canvas(fenetre, width=longueur, height=largeur)
    selec_jeu = Canvas(fenetre, width=longueur, height=largeur)
    choix_multi = Canvas(fenetre, width=longueur, height=largeur)
    jeu_multi = Canvas(fenetre, width=longueur, height=largeur)
    lobby_multi = Canvas(fenetre, width=longueur, height=largeur)
    gagne_multi = Canvas(fenetre, width=longueur, height=largeur)
    recherche_multi = Canvas(fenetre, width=longueur, height=largeur)
    connexion_au_serveur = Canvas(fenetre,width=longueur, height=largeur)

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
    nb_reponse_juste.set(0)

    nombre_personne=0


def crea_question():

    global liste_attributs, liste_valeurs, liste_reponses, liste_questions



    if is_multi.get()==0:


        liste_attributs, liste_valeurs, liste_reponses = creation_questions.lancer_tirage(randint(1,1000000))

    else :
        print('la seed est :'+seed_serveur.get())
        liste_attributs, liste_valeurs, liste_reponses = creation_questions.lancer_tirage(seed_serveur.get())

    liste_questions=nommer_questions(liste_attributs,liste_valeurs)

    question1.set(liste_questions[0])
    

def quitter():   #fermer la fenetre
    fenetre.destroy()

def callback(key):
    test_reponse()

def recherche():
    print(str(var_entree.get()))

def test_reponse():

    global liste_attributs, liste_valeurs, liste_reponses, liste_questions

    try :
        
        reponse_simp=simp(var_reponse.get())

        nb_reponse_juste_fct=nb_reponse_juste.get()

        liste_reponses_simp=simp_liste_p3(liste_reponses)
        
        for i in range (len(liste_reponses[nb_reponse_juste_fct])):
           
            if str(reponse_simp) == liste_reponses_simp[nb_reponse_juste_fct][i][0]:
                              
                nb_reponse_juste.set(nb_reponse_juste.get()+1)

                if nb_reponse_juste.get() == 1:
                    
                    reponse_entree1.set(liste_reponses[nb_reponse_juste_fct][i][0])
                    label_r1.configure(textvariable=reponse_entree1,background ='lightgreen')
                    label_r2.configure(textvariable=var_reponse,background ='lightgrey')
                    label_q1.configure(background ='lightgreen')
                    label_q2.configure(background ='lightgrey')
                    question2.set(liste_questions[1])
                    var_reponse.set('')
                    
                if nb_reponse_juste.get() == 2:
                    reponse_entree2.set(liste_reponses[nb_reponse_juste_fct][i][0])
                    label_r2.configure(textvariable=reponse_entree2,background ='lightgreen')
                    label_r3.configure(textvariable=var_reponse,background ='lightgrey')
                    label_q2.configure(background ='lightgreen')
                    label_q3.configure(background ='lightgrey')
                    question3.set(liste_questions[2])
                    
                if nb_reponse_juste.get() == 3:
                    reponse_entree3.set(liste_reponses[nb_reponse_juste_fct][i][0])
                    label_r3.configure(textvariable=reponse_entree3,background ='lightgreen')
                    label_r4.configure(textvariable=var_reponse,background ='lightgrey')
                    label_q3.configure(background ='lightgreen')
                    label_q4.configure(background ='lightgrey')
                    question4.set(liste_questions[3])
                    
                if nb_reponse_juste.get() == 4:
                    reponse_entree4.set(liste_reponses[nb_reponse_juste_fct][i][0])
                    label_r4.configure(textvariable=reponse_entree4,background ='lightgreen')
                    label_r5.configure(textvariable=var_reponse,background ='lightgrey')
                    label_q4.configure(background ='lightgreen')
                    label_q5.configure(background ='lightgrey')
                    question5.set(liste_questions[4])
                    
                if nb_reponse_juste.get() == 5:
                    reponse_entree5.set(liste_reponses[nb_reponse_juste_fct][i][0])
                    label_r5.configure(textvariable=reponse_entree5,background ='lightgreen')
                    label_q5.configure(background ='lightgreen')

                    print(is_multi.get())
                    if is_multi.get() == 0 :
                        page3()
                    else :
                        page9()
                    
                var_reponse.set('')
    except:None
            


def echap(key):
    retour()
    
def retour():
    page1(620,450)

def abandon():
    var_reponse.set(str(liste_reponses[4][0][0]))

def f_follow(key):
    if follow.get()!='1':
        follow.set('1')
    else :
        follow.set('0')


def motion(event):
    xx, yy = event.x, event.y
    if follow.get()=='1':
        page1((xx-100),(yy-25))

def meme_reponse(key):
    if nb_reponse_juste.get()> 0:
        var_reponse.set(eval('reponse_entree'+str(nb_reponse_juste.get())).get())
        test_reponse()


def lancer_serveur():
    os.startfile("multi_serveur.py")
    recherche_ip.set("localhost")
    page6()

def new_envent_lobby():
    global nombre_personne
    nombre_personne=nombre_personne+1
    liste_personne=["Léandro","Dionys","Estéban","Mathieu","Kylian"]
    label_personne = Label(lobby_multi, text=liste_personne[nombre_personne-1], font=police2, background = 'grey', anchor='center')
    label_personne.place(x=50,y=50+(80*nombre_personne),width=400, height=70)
    label_score = Label(lobby_multi, text='0', font=police2, background = 'lightgrey', anchor='center')
    label_score.place(x=450,y=50+(80*nombre_personne),width=100, height=70)

def update_temps():
    global temps_0
    global temps_1
    temps_1 = time.time()
    temps_timer.set(round(temps_1-temps_0))
    fenetre.after(1000,update_temps)

    
longueur = '1440'
largeur = '810'

nombre_personne=0
connecte=0

fenetre = Tk()
fenetre.geometry(longueur+'x'+largeur)
fenetre.title('GéoQuiz')
police1=tkFont.Font(family="MV Boli",size=20)
police2=tkFont.Font(family="MV Boli",size=16)

menu = Canvas(fenetre, width=longueur, height=largeur)
jeu_solo = Canvas(fenetre, width=longueur, height=largeur)
gagne_solo = Canvas(fenetre, width=longueur, height=largeur)
selec_jeu = Canvas(fenetre, width=longueur, height=largeur)
choix_multi = Canvas(fenetre, width=longueur, height=largeur)
jeu_multi = Canvas(fenetre, width=longueur, height=largeur)
lobby_multi = Canvas(fenetre, width=longueur, height=largeur)
gagne_multi = Canvas(fenetre, width=longueur, height=largeur)
recherche_multi = Canvas(fenetre, width=longueur, height=largeur)
connexion_au_serveur = Canvas(fenetre,width=longueur, height=largeur)

fenetre.bind('<KeyPress>', callback)
fenetre.bind('<Escape>', retour)
fenetre.bind('<Control-*>', f_follow)
fenetre.bind('<Control_L>', meme_reponse)


var_reponse = StringVar()
nb_reponse_juste = IntVar(0)

follow = StringVar()

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

local_ip=StringVar()

temps_timer=StringVar()

is_multi = IntVar(0)

recherche_ip=StringVar()
recherche_pseudo=StringVar()

etat_multi=StringVar()

seed_serveur=StringVar()


page1(620,450)
menu.mainloop()
