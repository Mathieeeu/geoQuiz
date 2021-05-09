from tkinter import *
import tkinter.font as tkFont
import socket

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




def lancer_partie():
    print('aaa')




            



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
menu.mainloop()




