from tkinter import *
import tkinter.font as tkFont
from simplificateur import simp, simp_liste, simp_liste_p2, simp_liste_p3
import creation_questions
from nommer_questions import nommer_questions
import time

def page1(xx,yy):
    global menu
    reset()
    menu.place(x=0, y=0)
    
    bouton_jouer = StringVar()
    bouton_jouer=Button(menu, text='Jouer',command=page2, font=police1)
    bouton_jouer.place(x=xx,y=yy,width=200, height=50)


    bouton_quit = StringVar()
    bouton_quit=Button(menu, text='Quitter',command=quitter, font=police1)
    bouton_quit.place(x=(int(longueur)/2)-100,y=550,width=200, height=50)

    image_logo = Label(menu, image="")
    file_logo="logo.png"
    logo = PhotoImage(file=file_logo)
    image_logo.configure(image=logo)
    image_logo.image = logo
    image_logo.place(x=440,y=150,width=624, height=240)
    
    #print('p1 appelé')

    menu.bind('<Motion>', motion)



def page2():
    global jeu
    global label_r1,label_r2,label_r3,label_r4,label_r5
    global label_q1,label_q2,label_q3,label_q4,label_q5
    
    global t0
    
    reset()
    crea_question()
    jeu.place(x=0, y=0)

    t0 = time.time()

    bouton_retour = StringVar()
    bouton_retour=Button(jeu, text='Retour', command=retour, font=police1)
    bouton_retour.place(x=int(longueur)-210,y=int(largeur)-60,width=200, height=50)

    bouton_abandon = StringVar()
    bouton_abandon=Button(jeu, text='Abandonner', command=abandon, font=police1)
    bouton_abandon.place(x=int(longueur)-420,y=int(largeur)-60,width=200, height=50)

    #print('p2 appelé')

    textBoxReponse = Entry(jeu, textvariable=var_reponse, width=40, font=police1, bg = 'yellow')
    textBoxReponse.place(x=1050,y=600,width=200, height=70)

    label_q1 = Label(jeu, textvariable=question1, font=police2 , background = 'lightgrey', anchor='center')
    label_q1.place(x=100,y=100,width=800, height=70)

    label_q2 = Label(jeu, textvariable=question2, font=police2, background = 'grey', anchor='center')
    label_q2.place(x=100,y=200,width=800, height=70)

    label_q3 = Label(jeu, textvariable=question3, font=police2, background = 'grey', anchor='center')
    label_q3.place(x=100,y=300,width=800, height=70)

    label_q4 = Label(jeu, textvariable=question4, font=police2, background = 'grey', anchor='center')
    label_q4.place(x=100,y=400,width=800, height=70)

    label_q5 = Label(jeu, textvariable=question5, font=police2, background = 'grey', anchor='center')
    label_q5.place(x=100,y=500,width=800, height=70)


    label_r1 = Label(jeu, textvariable=var_reponse, font=police1, background = 'lightgrey', anchor='center')
    label_r1.place(x=950,y=100,width=400, height=70)

    label_r2 = Label(jeu, textvariable=reponse_entree2, font=police1, background = 'grey', anchor='center')
    label_r2.place(x=950,y=200,width=400, height=70)

    label_r3 = Label(jeu, textvariable=reponse_entree3, font=police1, background = 'grey', anchor='center')
    label_r3.place(x=950,y=300,width=400, height=70)

    label_r4 = Label(jeu, textvariable=reponse_entree4, font=police1, background = 'grey', anchor='center')
    label_r4.place(x=950,y=400,width=400, height=70)

    label_r5 = Label(jeu, textvariable=reponse_entree5, font=police1, background = 'grey', anchor='center')
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
    label_q1.place(x=(int(longueur)/2)-250,y=200,width=500, height=70)


    bouton_rejouer = StringVar()
    bouton_rejouer=Button(gagne, text='Rejouer', command=page2, font=police1)
    bouton_rejouer.place(x=(int(longueur)/2)-100,y=400,width=200, height=50)

    bouton_menu = StringVar()
    bouton_menu=Button(gagne, text='Menu', command=retour, font=police1)
    bouton_menu.place(x=(int(longueur)/2)-100,y=475,width=200, height=50)

    bouton_quitter = StringVar()
    bouton_quitter=Button(gagne, text='Quitter', command=quitter, font=police1)
    bouton_quitter.place(x=(int(longueur)/2)-100,y=550,width=200, height=50)
    

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


def crea_question():

    global liste_attributs, liste_valeurs, liste_reponses, liste_questions

    liste_attributs, liste_valeurs, liste_reponses = creation_questions.lancer_tirage()
    print('Pssssst : '+ str(liste_reponses[4]))

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
                page3()
                
            var_reponse.set('')
            


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




longueur = '1440'
largeur = '810'

fenetre = Tk()
fenetre.geometry(longueur+'x'+largeur)
fenetre.title('GéoQuiz')
police1=tkFont.Font(family="MV Boli",size=20)
police2=tkFont.Font(family="MV Boli",size=16)

menu = Canvas(fenetre, width=longueur, height=largeur)
jeu = Canvas(fenetre, width=longueur, height=largeur)
gagne = Canvas(fenetre, width=longueur, height=largeur)


fenetre.bind('<KeyPress>', callback)
fenetre.bind('<Escape>', retour)
fenetre.bind('<Control-*>', f_follow)


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


page1(620,450)
menu.mainloop()
