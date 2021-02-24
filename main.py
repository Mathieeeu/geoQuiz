from tkinter import *
import tkinter.font as tkFont
import simp
import time

def page1():
    global menu
    reset()
    menu.place(x=0, y=0)
    
    bouton_jouer = StringVar()
    bouton_jouer=Button(menu, text='Jouer',command=page2, font=police1)
    bouton_jouer.place(x=(int(longueur)/2)-100,y=350,width=200, height=50)

    bouton_quit = StringVar()
    bouton_quit=Button(menu, text='Quitter',command=quitter, font=police1)
    bouton_quit.place(x=(int(longueur)/2)-100,y=450,width=200, height=50)
    
    print('p1 appelé')

def page2():
    global jeu
    global label_r1
    global label_r2
    global label_r3
    global label_r4
    global label_r5
    global t0
    
    reset()
    jeu.place(x=0, y=0)

    t0 = time.time()

    bouton_retour = StringVar()
    bouton_retour=Button(jeu, text='Retour', command=page1, font=police1)
    bouton_retour.place(x=int(longueur)-210,y=int(largeur)-60,width=200, height=50)

    print('p2 appelé')

    textBoxReponse = Entry(jeu, textvariable=var_reponse, width=40, font=police1, bg = 'yellow')
    textBoxReponse.place(x=1050,y=600,width=200, height=70)

    label_q1 = Label(jeu, textvariable=question1, font=police1 , background = 'grey', anchor='center')
    label_q1.place(x=100,y=100,width=800, height=70)

    label_q2 = Label(jeu, textvariable=question2, font=police1, background = 'grey', anchor='center')
    label_q2.place(x=100,y=200,width=800, height=70)

    label_q3 = Label(jeu, textvariable=question3, font=police1, background = 'grey', anchor='center')
    label_q3.place(x=100,y=300,width=800, height=70)

    label_q4 = Label(jeu, textvariable=question4, font=police1, background = 'grey', anchor='center')
    label_q4.place(x=100,y=400,width=800, height=70)

    label_q5 = Label(jeu, textvariable=question5, font=police1, background = 'grey', anchor='center')
    label_q5.place(x=100,y=500,width=800, height=70)


    label_r1 = Label(jeu, textvariable=var_reponse, font=police1, background = 'light grey', anchor='center')
    label_r1.place(x=950,y=100,width=400, height=70)

    label_r2 = Label(jeu, textvariable=reponse_entree2, font=police1, background = 'light grey', anchor='center')
    label_r2.place(x=950,y=200,width=400, height=70)

    label_r3 = Label(jeu, textvariable=reponse_entree3, font=police1, background = 'light grey', anchor='center')
    label_r3.place(x=950,y=300,width=400, height=70)

    label_r4 = Label(jeu, textvariable=reponse_entree4, font=police1, background = 'light grey', anchor='center')
    label_r4.place(x=950,y=400,width=400, height=70)

    label_r5 = Label(jeu, textvariable=reponse_entree5, font=police1, background = 'light grey', anchor='center')
    label_r5.place(x=950,y=500,width=400, height=70)


def page3():
    global gagne
    global t0
    global t1

    t1 = time.time()
    temps=t1-t0

    reset()
    gagne.place(x=0, y=0)
    label_q1 = Label(gagne, text='Bien-joué tu as mis : '+str(round(temps))+'s', font=police1 , background = 'grey', anchor='center')
    label_q1.place(x=100,y=100,width=800, height=70)

    bouton_retour = StringVar()
    bouton_retour=Button(gagne, text='Retour', command=page1, font=police1)
    bouton_retour.place(x=int(longueur)-210,y=int(largeur)-60,width=200, height=50)

def reset():
    global menu
    global jeu
    global gagne
    global label_r1
    global label_r2
    global label_r3
    global label_r4
    global label_r5
    
    menu.destroy()
    jeu.destroy()
    gagne.destroy()
    menu = Canvas(fenetre,width=longueur, height=largeur)
    jeu = Canvas(fenetre, width=longueur, height=largeur)
    gagne = Canvas(fenetre, width=longueur, height=largeur)

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
    

def quitter():   #fermer la fenetre
    fenetre.destroy()

def callback(key):
    test_reponse()

def recherche():
    print(str(var_entree.get()))

def test_reponse():

    reponse_simp=simp.simp(var_reponse.get())
    
    if str(reponse_simp) in eval('reponse'+str(nb_reponse_juste.get()+1)) :

        nb_reponse_juste.set(nb_reponse_juste.get()+1)

            #print(nb_reponse_juste.get())
            #print(eval('reponse'+str(nb_reponse_juste.get()+1)))
            

        if nb_reponse_juste.get() == 1:
            reponse_entree1.set(var_reponse.get())
            label_r1.configure(textvariable=reponse_entree1)
            label_r2.configure(textvariable=var_reponse)
            question2.set('Pays européen')
            
        if nb_reponse_juste.get() == 2:
            reponse_entree2.set(var_reponse.get())
            label_r2.configure(textvariable=reponse_entree2)
            label_r3.configure(textvariable=var_reponse)
            question3.set('Pays qui ne parle pas anglais')
            
        if nb_reponse_juste.get() == 3:
            reponse_entree3.set(var_reponse.get())
            label_r3.configure(textvariable=reponse_entree3)
            label_r4.configure(textvariable=var_reponse)
            question4.set('Pays possédant une partie de l\'Antartique')
            
        if nb_reponse_juste.get() == 4:
            reponse_entree4.set(var_reponse.get())
            label_r4.configure(textvariable=reponse_entree4)
            label_r5.configure(textvariable=var_reponse)
            question5.set('Pays dont la capitale est Paris')
            
        if nb_reponse_juste.get() == 5:
            reponse_entree5.set(var_reponse.get())
            label_r5.configure(textvariable=reponse_entree5)
            LabelEntry = Label(jeu, text='Gagné!!!', width=40, font=police1, bg = 'yellow')
            LabelEntry.place(x=1050,y=600,width=200, height=70)
            page3()
            
        var_reponse.set('')

def retour(key):
    page1()



longueur = '1440'
largeur = '810'

fenetre = Tk()
fenetre.geometry(longueur+'x'+largeur)
fenetre.title('GéoQuiz')
police1=tkFont.Font(family="MV Boli",size=20)

menu = Canvas(fenetre, width=longueur, height=largeur)
jeu = Canvas(fenetre, width=longueur, height=largeur)
gagne = Canvas(fenetre, width=longueur, height=largeur)


fenetre.bind('<KeyPress>', callback)
fenetre.bind('<Escape>', retour)


reponse1=['algerie','allemagne','france','norvege','royaume uni']
reponse2=['allemagne','france','norvege','royaume uni']
reponse3=['allemagne','france','norvege']
reponse4=['france','norvege']
reponse5=['france']

var_reponse = StringVar()
nb_reponse_juste = IntVar(0)
reponse_entree1=StringVar()

reponse_entree2=StringVar()
reponse_entree3=StringVar()
reponse_entree4=StringVar()
reponse_entree5=StringVar()

question1=StringVar()
question2=StringVar()
question3=StringVar()
question4=StringVar()
question5=StringVar()

question1.set('Pays avec un drapeau à 3 couleurs')


page1()
menu.mainloop()
