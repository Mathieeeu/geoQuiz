from tkinter import*
from tkinter.ttk import *
import tkinter.font as tkFont
import sqlite3
import time

"""Fonction de connexion permettant de se connecter à la base pokedex
"""
def connexion():
    try:
        #connexion à la bdd
        sqliteConnection = sqlite3.connect('assets/pokedex.db')
        return sqliteConnection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

"""<summary>Fonction de connexion à la bdd</summary>
"""
def deconnexion(sqliteConnection):
   if (sqliteConnection):
       #fermeture de la co
            sqliteConnection.close()
            print("The SQLite connection is closed")



"""<summary>La fonction va chercher la liste des pokemon dans la bdd</summary>
<return>Retourne un tableau contenant la liste des noms de pokemon</return>
"""

def RemplirListeDeroulantePokemon():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
    sqlite_select_Query = "select nom from pokemon;"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #declaration du tableau qui va contenir les données a afficher dans la liste déroulante
    tabPoke = []
    #parcours notre tableau de retour de base de données et ajoute les éléments dans le tableau data
    for row in record:
        tabPoke.append(row[0])

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

    #retourne le tableau
    return tabPoke

def RemplirListeDeroulanteTypes():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
    sqlite_select_Query = "select libelle_type from type;"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #declaration du tableau qui va contenir les données a afficher dans la liste déroulante
    tabTypes = []
    #parcours notre tableau de retour de base de données et ajoute les éléments dans le tableau data
    for row in record:
        tabTypes.append(row[0])

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

    #retourne le tableau
    return tabTypes

"""<summary>Recupére et affiche les informations récupérer par la requéte</summary>

"""
def AffichezPokemon():

    global commande
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = commande #differente commandes
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()

    #la variable record est un tableau à plusieurs dimension, chaque case contient une information

    #on modifie la valeur de la StringVar "value_label_nom" avec une valeur du tableau
    value_label_nom.set(record[0][0])

    #on modifie la valeur de la StringVar "value_label_hp" avec une valeur du tableau
    value_label_hp.set(str(record[0][1]))
    #on modifie la valeur de la StringVar "value_label_attaque" avec une valeur du tableau
    value_label_attaque.set(str(record[0][2]))
    #on modifie la valeur de la StringVar "value_label_defense" avec une valeur du tableau
    value_label_defense.set(str(record[0][3]))
    #on modifie la valeur de la StringVar "value_label_attaque_spe" avec une valeur du tableau
    value_label_attaque_spe.set(str(record[0][4]))
    #on modifie la valeur de la StringVar "value_label_defense_spe" avec une valeur du tableau
    value_label_defense_spe.set(str(record[0][5]))
    #on modifie la valeur de la StringVar "value_label_vitesse" avec une valeur du tableau
    value_label_vitesse.set(str(record[0][6]))
    #on modifie la valeur de la StringVar "value_label_id" avec une valeur du tableau
    value_label_id.set(str(record[0][8]))
    #on modifie la valeur de la StringVar "value_label_dresseur" avec une valeur du tableau 
    value_label_dresseur.set(str(record[0][10]))


    #construction du lien de l'image
    lien_image = "assets/pokemons/" + str(record[0][0]) + ".png"

    #affichage de l'image
    img2 = PhotoImage(file=lien_image)
    image_pokemon.configure(image=img2)
    image_pokemon.image = img2

    #affiche une image des types
    file_type="assets/types/" + str(record[0][9]) + ".png"
    types = PhotoImage(file=file_type)
    image_types.configure(image=types,borderwidth=0)
    image_types.image = types

    print("SQLite Database Version is: ", record)
    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)


#fonctions permettant de changer la commande SQL
    
def AffichezPokemonButton():

    global commande
    commande =  "SELECT pokemon.nom,HP,attaque,defense,attaque_spe,defense_spe,vitesse,url_image,idPokemon, type.libelle_type, dresseur.nom from pokemon INNER JOIN type ON type.idType = pokemon.idType INNER JOIN dresseur ON dresseur.idDresseur = pokemon.pokemon_posseder WHERE pokemon.nom ='" + listeDeroulantePokemon.get() + "';"
    AffichezPokemon()
    
def AffichezPokemonAvant():

    global commande
    commande = "SELECT pokemon.nom,HP,attaque,defense,attaque_spe,defense_spe,vitesse,url_image,idPokemon, type.libelle_type, dresseur.nom from pokemon INNER JOIN type ON type.idType = pokemon.idType INNER JOIN dresseur ON dresseur.idDresseur = pokemon.pokemon_posseder WHERE pokemon.idPokemon ='" + str(int(value_label_id.get())-1) + "';"
    AffichezPokemon()


def AffichezPokemonSuivant():

    global commande
    commande = "SELECT pokemon.nom,HP,attaque,defense,attaque_spe,defense_spe,vitesse,url_image,idPokemon, type.libelle_type, dresseur.nom from pokemon INNER JOIN type ON type.idType = pokemon.idType INNER JOIN dresseur ON dresseur.idDresseur = pokemon.pokemon_posseder WHERE pokemon.idPokemon ='" + str(int(value_label_id.get())+1) + "';"
    AffichezPokemon()

    
"""<summary>Affiche dans le tree la liste des pokemon retourné par la requéte</summary>
"""

def AffichezListePokemon():
    
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requete
    if listeDeroulanteTypes.get() == 'Tous les types':
        sqlite_select_Query = "SELECT idPokemon,nom,HP,libelle_type FROM pokemon INNER JOIN type  ON type.idType = pokemon.idType WHERE nom LIKE '%" + var_texte_recherche.get() + "%';"
    else:
        sqlite_select_Query = "SELECT idPokemon,nom,HP,libelle_type FROM pokemon INNER JOIN type  ON type.idType = pokemon.idType WHERE nom LIKE '%" + var_texte_recherche.get() + "%' AND type.libelle_type ='" + listeDeroulanteTypes.get() + "';"

        
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #vidange du tableau
    tree.delete(*tree.get_children())
    #on parcours le tableau record pour afficher et on insert une nouvelle ligne à chaque row. 
    for row in record:
        tree.insert('', 'end', iid=str(row[0]), text=str(row[1]),values=(str(row[2]),str(row[3])))


    #on ferme le curseur
    cursor.close()
    #deconnexion de la bdd
    deconnexion(sqliteConnection)

#création de la fenetre Tkinter
fenetre=Tk()
fenetre.title('Pokédex Lite')
fontStyle = tkFont.Font(family="Terminal", size=12, weight="bold")

filename = PhotoImage(file = "assets/background/background_info.png")
#permet de modifier la taille de la fenétre
fenetre.geometry("800x800")
background_label = Label(fenetre, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
 
"""
------Partie liste déroulante + Bbouton Recherche-------------
"""
#récupération de la liste des pokemon dans la base de données avec la fonction RemplirListeDeroulantePokemon qui retoune un tableau.
tabPokemon=RemplirListeDeroulantePokemon()
#  Création de la Combobox (liste déroulante) , on la remplie avec le tableau préalablement récupérer
listeDeroulantePokemon = Combobox(fenetre, values=tabPokemon)
# Choisir l'élément qui s'affiche par défaut (ici le premier)
listeDeroulantePokemon.current(0)
#positon de la liste dans la fenetre
listeDeroulantePokemon.place(x=118,y=352,width=120, height=35)


#bouton recherche qui appele la fonction AffichezPokemon
bouton_search=Button(fenetre, text="Rechercher", command=AffichezPokemonButton)
bouton_search.place(x=125,y=395,width=102, height=25)

#bouton qui affiche le pokemon suivant (id+1)
bouton_search_avant=Button(fenetre, text="<", command=AffichezPokemonAvant)
bouton_search_avant.place(x=85,y=354,width=30, height=30)

#bouton qui affiche le pokemon suivant (id-1)
bouton_search_apres=Button(fenetre, text=">", command=AffichezPokemonSuivant)
bouton_search_apres.place(x=241,y=354,width=30, height=30)


"""
------FIN-------------
"""


"""
Partie affichage des informations d'une pokemon
"""

#création d'une variable StringVar value_label_nom
value_label_nom = StringVar()
champ_label=Label(fenetre,textvariable=value_label_nom,font=fontStyle)
champ_label.place(x=630,y=160,width=140, height=30)
champ_label.config(anchor=CENTER)

#création d'une variable StringVar value_label_hp
value_label_hp = StringVar()
champ_label_hp=Label(fenetre,textvariable=value_label_hp,font=fontStyle)
champ_label_hp.place(x=105,y=456,width=45, height=20)
champ_label_hp.config(anchor=CENTER)

#création d'une variable StringVar value_label_attaque
value_label_attaque = StringVar()
champ_label_attaque=Label(fenetre,textvariable=value_label_attaque,font=fontStyle)
champ_label_attaque.place(x=105,y=488,width=45, height=20)
champ_label_attaque.config(anchor=CENTER)

#création d'une variable StringVar value_label_defense
value_label_defense = StringVar()
champ_label_defense=Label(fenetre,textvariable=value_label_defense,font=fontStyle)
champ_label_defense.place(x=105,y=521,width=45, height=20)
champ_label_defense.config(anchor=CENTER)

#création d'une variable StringVar value_label_attaque_spe
value_label_attaque_spe = StringVar()
champ_label_attaque_spe=Label(fenetre,textvariable=value_label_attaque,font=fontStyle)
champ_label_attaque_spe.place(x=105,y=553,width=45, height=20)
champ_label_attaque_spe.config(anchor=CENTER)

#création d'une variable StringVar value_label_defense_spe
value_label_defense_spe = StringVar()
champ_label_defense_spe=Label(fenetre,textvariable=value_label_defense_spe,font=fontStyle)
champ_label_defense_spe.place(x=105,y=584,width=45, height=20)
champ_label_defense_spe.config(anchor=CENTER)

#création d'une variable StringVar value_label_vitesse
value_label_vitesse = StringVar()
champ_label_vitesse=Label(fenetre,textvariable=value_label_vitesse,font=fontStyle)
champ_label_vitesse.place(x=105,y=617,width=45, height=20)
champ_label_vitesse.config(anchor=CENTER)

#création d'une variable StringVar value_label_id
value_label_id = StringVar()
champ_label_id=Label(fenetre,textvariable=value_label_id,font=fontStyle)
champ_label_id.place(x=505,y=160,width=45, height=30)
champ_label_id.config(anchor=CENTER)

#création d'une variable StringVar value_label_dresseur
value_label_dresseur = StringVar()
champ_label_dresseur=Label(fenetre,textvariable=value_label_dresseur,font=fontStyle)
champ_label_dresseur.place(x=480,y=440,width=290, height=30)
champ_label_dresseur.config(anchor=CENTER)

#label de l'image du pokemon
image_pokemon = Label(fenetre, image="")
image_pokemon.place(x=26,y=130,width=296, height=192)

#label de l'image du type
image_types = Label(fenetre, image="",borderwidth=-1, relief=FLAT, border=-1,background='#e74e4e')
image_types.place(x=625,y=195,width=70, height=30)

#label du texte avant dresseur
champ_label_dresseur_text=Label(fenetre,text='Ce pokemon appartient à :',font=fontStyle)
champ_label_dresseur_text.place(x=461,y=397,width=330, height=30)
champ_label_dresseur_text.config(anchor=CENTER)
"""
-------------------FIN---------------------------------------
"""

"""
Partie recherche et affichage du tableau
"""
#création d'une variable StringVar
var_texte_recherche = StringVar()
textBoxRecherche = Entry(fenetre, textvariable=var_texte_recherche, width=20)
textBoxRecherche.place(x=410,y=635,width=100, height=30)
#bouton de recherche
bouton_affichez_pokemon=Button(fenetre, text="Rechercher", command=AffichezListePokemon)
bouton_affichez_pokemon.place(x=640,y=635,width=150, height=30)


#récupération de la liste des types dans la base de données avec la fonction RemplirListeDeroulanteTypes qui retoune un tableau.
tabTypes=RemplirListeDeroulanteTypes()
#  Création de la Combobox (liste déroulante) , on la remplie avec le tableau préalablement récupérer
listeDeroulanteTypes = Combobox(fenetre, values=tabTypes)
# Choisir l'élément qui s'affiche par défaut (ici le premier)
listeDeroulanteTypes.current(0)
#positon de la liste dans la fenetre
listeDeroulanteTypes.place(x=520,y=635,width=110, height=30)


#création de la grille d'affichage (tableau)
tree = Treeview(fenetre, columns=('HP', 'Type'))

 
 # Set the heading (Attribute Names)
tree.heading('#0', text='Pokemon')
tree.heading('#1', text='HP')
tree.heading('#2', text='Type')
# Specify attributes of the columns (We want to stretch it!)
tree.column('#0',width=150, stretch=YES)
tree.column('#1',width=30, stretch=YES)
tree.column('#2',width=70, stretch=YES)

#placement du tableau
tree.place(x=20,y=683,width=760, height=110)
"""-----------------FIN----------------------"""

AffichezPokemonButton()
AffichezListePokemon()

#On démarre la boucle Tkinter qui s'interrompt quand on ferme la fenêtre
fenetre.mainloop()
