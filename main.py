from tkinter import *


def page1():
    global menu
    reset()
    menu.place(x=0, y=0)
    
    bouton_jouer = StringVar()
    bouton_jouer=Button(menu, text='Jouer',command=page2)
    bouton_jouer.place(x=(int(longueur)/2)-100,y=300,width=200, height=50)

    bouton_quit = StringVar()
    bouton_quit=Button(menu, text='Quitter',command=quitter)
    bouton_quit.place(x=(int(longueur)/2)-100,y=500,width=200, height=50)
    
    print('p1 appelé')

def page2():
    global jeu
    reset()
    jeu.place(x=0, y=0)

    bouton_retour = StringVar()
    bouton_retour=Button(jeu, text='Retour', command=page1)
    bouton_retour.place(x=int(longueur)-210,y=int(largeur)-60,width=200, height=50)

    print('p2 appelé')

    textBoxEntree = Entry(jeu, textvariable=var_entree, width=40)
    textBoxEntree.place(x=410,y=635,width=200, height=70)

    label_q1 = Label(jeu, text=str(question), police=...)
    label_q1.place(x=200,y=235,width=200, height=70)




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
    recherche()

def recherche():
    print(str(var_entree.get()))



longueur = '1440'
largeur = '810'

fenetre = Tk()
fenetre.geometry(longueur+'x'+largeur)
fenetre.title('GéoQuiz')
Police=fenetre.font.Font(family="Calibri",size=120)

menu = Canvas(fenetre, width=longueur, height=largeur)
jeu = Canvas(fenetre, width=longueur, height=largeur)

fenetre.bind('<Return>', callback)

question='Quel est la capitale de la France ?'

var_entree = StringVar()

page1()
menu.mainloop()
