
import tkinter.font as tkFont
from tkinter import *


def page1():
    global menu
    reset()
    menu.place(x=0, y=0)
    
    bouton_jouer = StringVar()
    bouton_jouer=Button(menu, text='Jouer',command=page2, font=police)
    bouton_jouer.place(x=(int(longueur)/2)-100,y=300,width=200, height=50)

    bouton_quit = StringVar()
    bouton_quit=Button(menu, text='Quitter',command=quitter, font=police)
    bouton_quit.place(x=(int(longueur)/2)-100,y=500,width=200, height=50)
    
    print('p1 appelé')

def page2():
    global jeu
    global textBoxEntree1
    global textBoxEntree2
    reset()
    jeu.place(x=0, y=0)

    bouton_retour = StringVar()
    bouton_retour=Button(jeu, text='Retour', command=page1, font=police)
    bouton_retour.place(x=int(longueur)-210,y=int(largeur)-60,width=200, height=50)

    print('p2 appelé')

    textBoxEntree1 = Entry(jeu, textvariable=var_entree1, width=40, font=police)
    textBoxEntree1.place(x=600,y=100,width=200, height=70)

    label_q1 = Label(jeu, text=str(question1), font=police)
    label_q1.place(x=200,y=100,width=400, height=70)

    textBoxEntree2 = Entry(jeu, textvariable=var_entree2, width=40, font=police)
    textBoxEntree2.place(x=600,y=200,width=200, height=70)

    label_q2 = Label(jeu, text=str(question2), font=police)
    label_q2.place(x=200,y=200,width=400, height=70)

    textBoxEntree3 = Entry(jeu, textvariable=var_entree3, width=40, font=police)
    textBoxEntree3.place(x=600,y=300,width=200, height=70)

    label_q3 = Label(jeu, text=str(question3), font=police)
    label_q3.place(x=200,y=300,width=400, height=70)
    
    textBoxEntree4 = Entry(jeu, textvariable=var_entree4, width=40, font=police)
    textBoxEntree4.place(x=600,y=400,width=200, height=70)
    
    label_q4 = Label(jeu, text=str(question4), font=police)
    label_q4.place(x=200,y=400,width=400, height=70)

    textBoxEntree5 = Entry(jeu, textvariable=var_entree5, width=40, font=police)
    textBoxEntree5.place(x=600,y=500,width=200, height=70)

    label_q5 = Label(jeu, text=str(question5), font=police)
    label_q5.place(x=200,y=500,width=400, height=70)




def reset():
    global menu
    global jeu
    menu.destroy()
    jeu.destroy()
    menu = Canvas(fenetre,width=longueur, height=largeur)
    jeu = Canvas(fenetre, width=longueur, height=largeur)

def quitter():   #fermer la fenetre
    fenetre.destroy()

def callback(key):
    verif()


def verif():
    global textBoxEntree1
    global textBoxEntree2
    if str(var_entree1.get()) == 'Paris':
        print('gg')
        label_r1 = Label(jeu, textvariable=var_entree1, font=police)
        label_r1.place(x=600,y=100,width=200, height=70)
        textBoxEntree1.configure(state="disable")
        textBoxEntree2.configure(state="normal")

longueur = '1440'
largeur = '810'

fenetre = Tk()
fenetre.geometry(longueur+'x'+largeur)
fenetre.title('GéoQuiz')
police=tkFont.Font(family="Lobster",size=18)

menu = Canvas(fenetre, width=longueur, height=largeur)
jeu = Canvas(fenetre, width=longueur, height=largeur)

fenetre.bind('<Return>', callback)



question1 = StringVar()
question2 = StringVar()
question3 = StringVar()
question4 = StringVar()
question5 = StringVar()
var_entree1 = StringVar()
var_entree2 = StringVar()
var_entree3 = StringVar()
var_entree4 = StringVar()
var_entree5 = StringVar()

question1='Quel est la capitale de la France ?'
question2='Quel est la capitale de la France ?'
question3='Quel est la capitale de la France ?'
question4='Quel est la capitale de la France ?'
question5='Quel est la capitale de la France ?'

page1()
menu.mainloop()

