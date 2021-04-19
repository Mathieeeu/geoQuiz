from tkinter import*
from tkinter.ttk import *
import tkinter.font as tkFont
import sqlite3
import random
import time
from math import *
from tkinter import messagebox as mb



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Fonctions universelles XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


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

def reset():  #remettre à zéro chaque page pour pouvoir changer de page
    global info
    global selection
    global area
    info.destroy()
    selection.destroy()
    area.destroy()
    info = Canvas(fenetre, width=800, height=800)
    selection = Canvas(fenetre, width=800, height=800)
    area = Canvas(fenetre, width=800, height=800)
    

def Quit():   #fermer la fenetre
    fenetre.destroy()



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Fonctions pour la page info XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


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
    global image_pokemon
    global image_pokemon_dresseur
    global zone
    
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

    #on modifie les valeurs des stats avec les valeurs du tableau
    value_label_hp.set(str(record[0][1]))
    value_label_attaque.set(str(record[0][2]))
    value_label_defense.set(str(record[0][3]))
    value_label_attaque_spe.set(str(record[0][4]))
    value_label_defense_spe.set(str(record[0][5]))
    value_label_vitesse.set(str(record[0][6]))
    value_label_id.set(str(record[0][8]))
    value_label_dresseur.set(str(record[0][10]))



    #construction du lien de l'image
    lien_image = "assets/pokemons/" + str(record[0][0]) + ".png"

    #affichage de l'image
    img2 = PhotoImage(file=lien_image)
    image_pokemon.configure(image=img2)
    image_pokemon.image = img2

    print("SQLite Database Version is: ", record)
    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

    if zone == 1 :  #si c'est dans le pokédex
        
        #affiche une image des types
        file_type="assets/types/" + str(record[0][9]) + ".png"
        types = PhotoImage(file=file_type)
        image_types.configure(image=types,borderwidth=0)
        image_types.image = types



    if zone == 3 :  #si on est dans area pour pouvoir afficher le pokemon du dresseur

        sqliteConnection = connexion()
        cursor = sqliteConnection.cursor()
        #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
        sqlite_select_Query = "SELECT pokemon.nom,HP,attaque,defense,attaque_spe,defense_spe,vitesse,url_image,idPokemon, type.libelle_type, dresseur.nom, pokemon_posseder from pokemon INNER JOIN type ON type.idType = pokemon.idType INNER JOIN dresseur ON dresseur.idDresseur = pokemon.pokemon_posseder WHERE pokemon.nom ='" + pokemon_dresseur + "';"
        #execution de la requéte
        cursor.execute(sqlite_select_Query)
        #on place tout les enregistrements dans une variable record
        record = cursor.fetchall()

        #la variable record est un tableau à plusieurs dimension, chaque case contient une information

        #on modifie la valeur de la StringVar "value_label_nom" avec une valeur du tableau
        value_label_nom_dresseur.set(record[0][0])

        #on modifie les valeurs des stats avec les valeurs du tableau
        value_label_hp_dresseur.set(str(record[0][1]))
        value_label_attaque_dresseur.set(str(record[0][2]))
        value_label_defense_dresseur.set(str(record[0][3]))
        value_label_attaque_spe_dresseur.set(str(record[0][4]))
        value_label_defense_spe_dresseur.set(str(record[0][5]))
        value_label_vitesse_dresseur.set(str(record[0][6]))
        value_label_pokemon_posseder.set(str(record[0][11]))

        #construction du lien de l'image
        lien_image = "assets/pokemons/" + str(record[0][0]) + ".png"

        #affichage de l'image
        img2 = PhotoImage(file=lien_image)
        image_pokemon_dresseur.configure(image=img2)
        image_pokemon_dresseur.image = img2

        print("SQLite Database Version is: ", record)
        #on ferme le curseur
        cursor.close()
        deconnexion(sqliteConnection)

        value_label_hp_restant.set(value_label_hp.get())
        value_label_hp_restant_dresseur.set(value_label_hp_dresseur.get())


#fonctions permettant de changer la commande SQL

def AffichezPokemonButton():

    global commande
    commande =  "SELECT pokemon.nom,HP,attaque,defense,attaque_spe,defense_spe,vitesse,url_image,idPokemon, type.libelle_type, dresseur.nom, pokemon_posseder from pokemon INNER JOIN type ON type.idType = pokemon.idType INNER JOIN dresseur ON dresseur.idDresseur = pokemon.pokemon_posseder WHERE pokemon.nom ='" + listeDeroulantePokemon.get() + "';"
    AffichezPokemon()
    
def AffichezPokemonAvant():

    global commande
    commande = "SELECT pokemon.nom,HP,attaque,defense,attaque_spe,defense_spe,vitesse,url_image,idPokemon, type.libelle_type, dresseur.nom, pokemon_posseder from pokemon INNER JOIN type ON type.idType = pokemon.idType INNER JOIN dresseur ON dresseur.idDresseur = pokemon.pokemon_posseder WHERE pokemon.idPokemon ='" + str(int(value_label_id.get())-1) + "';"
    AffichezPokemon()


def AffichezPokemonSuivant():

    global commande
    commande = "SELECT pokemon.nom,HP,attaque,defense,attaque_spe,defense_spe,vitesse,url_image,idPokemon, type.libelle_type, dresseur.nom, pokemon_posseder from pokemon INNER JOIN type ON type.idType = pokemon.idType INNER JOIN dresseur ON dresseur.idDresseur = pokemon.pokemon_posseder WHERE pokemon.idPokemon ='" + str(int(value_label_id.get())+1) + "';"
    AffichezPokemon()

    
"""<summary>Affiche dans le tree la liste des pokemon retourné par la requéte</summary>
"""


def AffichezListePokemon():
    
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
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



#XXXXXXXXXXXXXXXXXXXXXXXXXXX Fonctions pour la page selection XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


def RemplirListeDeroulanteDresseur():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
    sqlite_select_Query = "select nom from dresseur;"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #declaration du tableau qui va contenir les données a afficher dans la liste déroulante
    tabDresseur = []
    #parcours notre tableau de retour de base de données et ajoute les éléments dans le tableau data
    #tabDresseur.append('--- Sélectionner votre dresseur ---')
    for row in record:
        tabDresseur.append(row[0])
    tabDresseur.pop(0)
    

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

    #retourne le tableau
    return tabDresseur


def RemplirListeDeroulantePokemonDresseur():
    global listeDeroulanteDresseur
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
    sqlite_select_Query = "SELECT pokemon.nom FROM pokemon INNER JOIN dresseur  ON dresseur.idDresseur = pokemon.pokemon_posseder WHERE dresseur.nom = '" + listeDeroulanteDresseur.get() + "';"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #declaration du tableau qui va contenir les données a afficher dans la liste déroulante
    tabPokemon = []
    #parcours notre tableau de retour de base de données et ajoute les éléments dans le tableau data
    for row in record:
        tabPokemon.append(row[0])

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

    #retourne le tableau
    return tabPokemon

def Actualiser(): #actualiser les pokemons des dresseurs
    global listeDeroulanteDresseur
    global listeDeroulantePokemon
    #récupération de la liste des pokemons dans la base de données avec la fonction RemplirListeDeroulantePokemonDresseur qui retoune un tableau.
    tabPokemon=RemplirListeDeroulantePokemonDresseur()
    #Création de la Combobox (liste déroulante) , on la remplie avec le tableau préalablement récupérer
    listeDeroulantePokemon = Combobox(selection, values=tabPokemon)
    # Choisir l'élément qui s'affiche par défaut (ici le premier)
    listeDeroulantePokemon.current(0)

    #positon de la liste dans la fenetre
    listeDeroulantePokemon.place(x=487,y=230,width=200, height=30)

    
def ajouter_dresseur(): #ajouter un dresseur à la base SQL

    global listeDeroulanteDresseur
    
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    sql = "INSERT INTO dresseur (idDresseur, nom) VALUES (?,?)"
    value=(len(listeDeroulanteDresseur['values'])+1,var_texte_ajouter_dresseur.get())
    count = cursor.execute(sql,value)
    sqliteConnection.commit()
    print("Enregistrement inséré avec succès dans la table dresseur")

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    sql = "UPDATE pokemon SET pokemon_posseder = ? WHERE idPokemon == ?"
    value=(len(listeDeroulanteDresseur['values'])+1,random.randint(1,151))
    count = cursor.execute(sql,value)
    sqliteConnection.commit()
    print("Enregistrement inséré avec succès dans la table dresseur")

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

    #récupération de la liste des dresseurs dans la base de données avec la fonction RemplirListeDeroulanteDresseur qui retoune un tableau.
    tabDresseur=RemplirListeDeroulanteDresseur()
    #  Création de la Combobox (liste déroulante) , on la remplie avec le tableau préalablement récupérer
    listeDeroulanteDresseur = Combobox(selection, values=tabDresseur)
    # Choisir l'élément qui s'affiche par défaut (ici le premier)
    listeDeroulanteDresseur.current(0)
    #positon de la liste dans la fenetre
    listeDeroulanteDresseur.place(x=140,y=230,width=200, height=30)


def valider():
    global listeDeroulantePokemon
    global pokemon_dresseur

    #Actualiser()
    pokemon_dresseur=listeDeroulantePokemon.get()
    print(pokemon_dresseur)

    page_area()



        
#XXXXXXXXXXXXXXXXXXXXXXXXXXX Fonctions pour la page area XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


def rencontre():
    global commande
    commande =  "SELECT pokemon.nom,HP,attaque,defense,attaque_spe,defense_spe,vitesse,url_image,idPokemon, type.libelle_type, dresseur.nom, pokemon_posseder from pokemon INNER JOIN type ON type.idType = pokemon.idType INNER JOIN dresseur ON dresseur.idDresseur = pokemon.pokemon_posseder WHERE pokemon.idPokemon ='" + str(random.randint(1,151)) + "';"
    print(commande)
    value_label_texte_area.set('Que voulez vous faire ?')
    AffichezPokemon()


def attaquer():

    global bouton_attaque_phy
    global bouton_attaque_spe
    global type_attaque
    
    value_label_texte_area.set('Attaquer corps à corps ou \n \nAttaquer à distance ?')

    type_attaque=''
        
    bouton_attaque_phy=Button(area, text="Attaque Physique", command=attaque_phy)
    bouton_attaque_phy.place(x=390,y=685,width=105, height=35)

    bouton_attaque_spe=Button(area, text="Attaque Spéciale", command=attaque_spe)
    bouton_attaque_spe.place(x=390,y=730,width=105, height=35)


def attaque_phy():

    global bouton_attaque_phy
    global bouton_attaque_spe
    global type_attaque
    
    bouton_attaque_phy.destroy()
    bouton_attaque_spe.destroy()

    value_label_texte_area.set(str(value_label_nom_dresseur.get())+ ' attaque ...')

    if int(value_label_vitesse.get()) < int(value_label_vitesse_dresseur.get()) or type_attaque == '2eme' :
        
        value_label_hp_restant.set(round(int(value_label_hp_restant.get()) -(((int(value_label_attaque_dresseur.get()) / 3) / int(value_label_defense.get())) * int(value_label_attaque_dresseur.get()))))
        print(str(value_label_hp_restant.get()))

        if int(value_label_hp_restant.get()) < 0 :
            value_label_hp_restant.set(0)
            value_label_texte_area.set('Dommage, ' +str(value_label_nom.get())+ ' est K.O. !')
            fenetre.after(3000,mort)

        else :
            
            if type_attaque !='2eme':
                fenetre.after(1000,attaque_poke_sauvage)

        actu_pv()
        fenetre.after(2000,que_faire)
 
    else :
        type_attaque = 'phy'
        attaque_poke_sauvage()



def attaque_spe():

    global bouton_attaque_phy
    global bouton_attaque_spe
    global type_attaque
    
    bouton_attaque_phy.destroy()
    bouton_attaque_spe.destroy()


    if int(value_label_vitesse.get()) < int(value_label_vitesse_dresseur.get()) or type_attaque == '2eme' :

        value_label_texte_area.set(str(value_label_nom_dresseur.get())+ ' attaque ...')
    
        value_label_hp_restant.set(round(int(value_label_hp_restant.get()) -(((int(value_label_attaque_spe_dresseur.get()) / 3) / int(value_label_defense_spe.get())) * int(value_label_attaque_spe_dresseur.get()))))
        print(str(value_label_hp_restant.get()))

        if int(value_label_hp_restant.get()) < 0 :
            value_label_hp_restant.set(0)
            value_label_texte_area.set(str(value_label_nom.get())+ ' est K.O. !')
            fenetre.after(3000,mort)

        else :
            if type_attaque !='2eme':
                fenetre.after(1000,attaque_poke_sauvage)

        actu_pv()
        fenetre.after(2000,que_faire)
        
    else :
        type_attaque = 'spe'
        attaque_poke_sauvage()


def attaque_poke_sauvage():  #attaque du pokemon sauvage apres que le joueur a joué

    global type_attaque

    if int(value_label_attaque.get()) > int(value_label_attaque_spe.get()) :
        value_label_hp_restant_dresseur.set(round(int(value_label_hp_restant_dresseur.get()) -(((int(value_label_attaque.get()) / 3) / int(value_label_defense_dresseur.get())) * int(value_label_attaque.get()))))

    else :
        value_label_hp_restant_dresseur.set(round(int(value_label_hp_restant_dresseur.get()) -(((int(value_label_attaque_spe.get()) / 3) / int(value_label_defense_spe_dresseur.get())) * int(value_label_attaque_spe.get()))))
            
    print(str(value_label_hp_restant_dresseur.get()))
    value_label_texte_area.set(str(value_label_nom.get())+ ' attaque ...')

    if int(value_label_hp_restant_dresseur.get()) < 0 :
        value_label_hp_restant_dresseur.set(0)
        value_label_texte_area.set(str(value_label_nom_dresseur.get())+ ' est K.O. !')
        fenetre.after(3000,mort)


    elif int(value_label_vitesse.get()) >= int(value_label_vitesse_dresseur.get()) and type_attaque !='capture_loupe':

        if type_attaque == 'phy':
            type_attaque = '2eme'
            fenetre.after(1000,attaque_phy)
        else :
            type_attaque = '2eme'
            fenetre.after(1000,attaque_spe)

    else :
        fenetre.after(2000,que_faire)

    actu_pv()
    

        
def actu_pv():  #change la taille et la couleur de la barre des pv

    champ_label_hp_dresseur=Label(area,text=value_label_hp_restant_dresseur.get() +'/'+ value_label_hp_dresseur.get(),font=fontStyle)
    champ_label_hp_dresseur.place(x=490,y=556,width=100, height=20)
    champ_label_hp_dresseur.config(anchor=CENTER)

    champ_label_hp=Label(area,text=value_label_hp_restant.get() +'/'+ value_label_hp.get(),font=fontStyle)
    champ_label_hp.place(x=30,y=212,width=100, height=20)
    champ_label_hp.config(anchor=CENTER)


    champ_label_barre_pv_dresseur=Label(area,background='white')
    champ_label_barre_pv_dresseur.place(x=629,y=558,width=148, height=14)
    
    if int(value_label_hp_restant_dresseur.get())/int(value_label_hp_dresseur.get()) < 0.2:
        champ_label_barre_pv_dresseur=Label(area,background='red')
    elif int(value_label_hp_restant_dresseur.get())/int(value_label_hp_dresseur.get()) < 0.5:
        champ_label_barre_pv_dresseur=Label(area,background='yellow')
    else :
        champ_label_barre_pv_dresseur=Label(area,background='green')
        
    champ_label_barre_pv_dresseur.place(x=629,y=558,width=round(148*(int(value_label_hp_restant_dresseur.get())/int(value_label_hp_dresseur.get()))), height=14)



    champ_label_barre_pv=Label(area,background='white')
    champ_label_barre_pv.place(x=181,y=212,width=186, height=18)
    
    if int(value_label_hp_restant.get())/int(value_label_hp.get()) < 0.2:
        champ_label_barre_pv=Label(area,background='red')
    elif int(value_label_hp_restant.get())/int(value_label_hp.get()) < 0.5:
        champ_label_barre_pv=Label(area,background='yellow')
    else :
        champ_label_barre_pv=Label(area,background='green')
        
    champ_label_barre_pv.place(x=181,y=212,width=round(186*(int(value_label_hp_restant.get())/int(value_label_hp.get()))), height=18)

def mort(): #revient au pokedex

    page_info()
    
def capturer():

    global bouton_attaque_phy
    global bouton_attaque_spe
    global image_pokeball
    global count
    global canvas
    global test_capture
    global type_attaque
    
    bouton_attaque_phy.destroy()
    bouton_attaque_spe.destroy()

    #le canvas permet d'animer la pokeball avec les sprites
    canvas = Canvas(area, width=128, height=128,bg='#fbf9ff')
    canvas.place(x=300,y=300)

    image_pokeball = Label(canvas, image="", anchor = SE)
    
    #affichage de l'image
    img2 = PhotoImage(file='assets/pokeball/sprite_pokeball.png')
    image_pokeball.configure(image=img2)
    image_pokeball.image = img2

    count = 0
    test_capture = random.randint(1,ceil(int(value_label_hp_restant.get())/5))
    print(test_capture)
    type_attaque =''
    update()


def update(): #permet de faire animer la pokeball en deplacant le sprite tout les 100ms
    global count
    global image_pokeball
    global canvas
    global test_capture
    global image_pokemon
    global type_attaque
    global liste_capture

    #chaque nombre fait descendre le canvas ce qui fait une animation
    
    if type_attaque !='capture_loupe':
        if test_capture > 4 :
            liste_capture = [0,1,2,3,2,1,0,1,2,3,2,1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,18,17,17,17,17,21,22,23,24,25,26] #loupé, 1
            type_attaque = 'capture_loupe'
            #fenetre.after(5000,attaque_poke_sauvage)
        if test_capture == 3 or 4 :
            liste_capture = [0,1,2,3,2,1,0,1,2,3,2,1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,18,17,17,17,17,16,15,16,17,18,19,18,17,17,17,17,21,22,23,24,25,26] # loupé 2
            type_attaque = 'capture_loupe'
            #fenetre.after(5000,attaque_poke_sauvage)
        if test_capture == 2 :
            liste_capture = [0,1,2,3,2,1,0,1,2,3,2,1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,18,17,17,17,17,16,15,16,17,18,19,18,17,17,17,17,16,15,16,17,18,19,18,17,17,17,17,21,22,23,24,25,26] #loupé 3
            type_attaque = 'capture_loupe'
            #fenetre.after(5000,attaque_poke_sauvage)
        if test_capture == 1 :
            liste_capture = [0,1,2,3,2,1,0,1,2,3,2,1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,18,17,17,17,17,16,15,16,17,18,19,18,17,17,17,17,16,15,16,17,18,19,18,17,17,17,17,28,29,30,31,32] #gagné
        
                
    if count < len(liste_capture) - 1 : #lancement pokeball

        if count < 17 :
                canvas.place(x=100+27*count,y=600-20*count)

        else :
            image_pokemon.destroy()
                
        image_pokeball.place(x=-1,y=(-128)*liste_capture[count],width=128, height=4096)
        
        count=count+1
        image_pokeball.after(100,update)

    else: #reaffiche le poke sauvage

        if test_capture == 1 :
            pokemon_capture()
            value_label_texte_area.set('Bravo, vous avez capturé ' +str(value_label_nom.get())+ ' !')
            fenetre.after(3000,page_info)

        else :
            image_pokemon = Label(area, image='')
            image_pokemon.place(x=450,y=230,width=296, height=192)
            lien_image = "assets/pokemons/" + value_label_nom.get() + ".png"
            img2 = PhotoImage(file=lien_image)
            image_pokemon.configure(image=img2)
            image_pokemon.image = img2
            value_label_texte_area.set('Dommage, ' +str(value_label_nom.get())+ ' s\'est echapper !')
            fenetre.after(2000,attaque_poke_sauvage)
            
            

def pokemon_capture(): #lorsque le pokemon est capturé, cela l'ajoute à la base SQL

    global pokemon_dresseur
    
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    print(value_label_pokemon_posseder.get())
    print(value_label_nom.get())
    sql = "UPDATE pokemon SET pokemon_posseder = '" +value_label_pokemon_posseder.get()+"'  WHERE nom = '" + value_label_nom.get() +"';"
    count = cursor.execute(sql)
    sqliteConnection.commit()
    print("Enregistrement inséré avec succès dans la table dresseur")

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

def que_faire():
    value_label_texte_area.set('Que voulez vous faire ?')

    
def stats(): #bouton qui affiche les stats

    global bouton_attaque_phy
    global bouton_attaque_spe
    
    bouton_attaque_phy.destroy()
    bouton_attaque_spe.destroy()
    
    value_label_texte_area.set(str(value_label_nom.get()) +' - PV:'+ str(value_label_hp.get()) +' - Atk:'+str(value_label_attaque.get()) +' - Def:'+str(value_label_defense.get()) +'\n Atk Spe:'+str(value_label_attaque_spe.get()) +' - Def Spe:'+str(value_label_defense_spe.get()) +' - Vit:'+str(value_label_vitesse.get()) +'\n \n' + str(value_label_nom_dresseur.get()) +' - PV:'+ str(value_label_hp_dresseur.get()) +' - Atk:'+str(value_label_attaque_dresseur.get()) +' - Def:'+str(value_label_defense_dresseur.get()) +'\n Atk Spe:'+str(value_label_attaque_spe_dresseur.get()) +' - Def Spe:'+str(value_label_defense_spe_dresseur.get()) +' - Vit:'+str(value_label_vitesse_dresseur.get()))




#XXXXXXXXXXXXXXX Fonctions définissant les objets de chacunes des 3 pages XXXXXXXXXXXXXXXXXXXXXXXXXXX


def page_info():

    global listeDeroulantePokemon
    global image_pokemon
    global image_types
    global listeDeroulanteTypes
    global tree
    global zone

    zone = 1

    reset()

    info.place(x=0, y=0)

    background_label = Label(info, image="")
    background_label.place(x=0, y=0, width=800, height=800)
    """
    ------Partie liste déroulante + Bbouton Recherche-------------
    """
    #récupération de la liste des pokemon dans la base de données avec la fonction RemplirListeDeroulantePokemon qui retoune un tableau.
    tabPokemon=RemplirListeDeroulantePokemon()
    #  Création de la Combobox (liste déroulante) , on la remplie avec le tableau préalablement récupérer
    listeDeroulantePokemon = Combobox(info, values=tabPokemon)
    # Choisir l'élément qui s'affiche par défaut (ici le premier)
    listeDeroulantePokemon.current(0)
    #positon de la liste dans la info
    listeDeroulantePokemon.place(x=118,y=352,width=120, height=35)


    #boutons qui appellent des fonctions :
    
    bouton_search=Button(info, text="Rechercher", command=AffichezPokemonButton)
    bouton_search.place(x=125,y=395,width=102, height=25)

    bouton_search_avant=Button(info, text="<", command=AffichezPokemonAvant)
    bouton_search_avant.place(x=85,y=354,width=30, height=30)

    bouton_search_apres=Button(info, text=">", command=AffichezPokemonSuivant)
    bouton_search_apres.place(x=241,y=354,width=30, height=30)

    bouton_info=Button(info, image="", command=page_info)
    bouton_info.place(x=55,y=6,width=178, height=55)

    bouton_area=Button(info, image="", command=page_selection)
    bouton_area.place(x=252,y=6,width=178, height=55)

    bouton_quitter=Button(info, image="", command=Quit)
    bouton_quitter.place(x=590,y=6,width=178, height=55)


    """
    ------FIN-------------
    """


    """
    Partie affichage des informations d'une pokemon
    """

    
    #label nom
    champ_label_nom=Label(info,textvariable=value_label_nom,font=fontStyle)
    champ_label_nom.place(x=630,y=160,width=140, height=30)
    champ_label_nom.config(anchor=CENTER)

    #label pv
    champ_label_hp=Label(info,textvariable=value_label_hp,font=fontStyle)
    champ_label_hp.place(x=105,y=456,width=45, height=20)
    champ_label_hp.config(anchor=CENTER)

    #label attaque
    champ_label_attaque=Label(info,textvariable=value_label_attaque,font=fontStyle)
    champ_label_attaque.place(x=105,y=488,width=45, height=20)
    champ_label_attaque.config(anchor=CENTER)

    #defense
    champ_label_defense=Label(info,textvariable=value_label_defense,font=fontStyle)
    champ_label_defense.place(x=105,y=521,width=45, height=20)
    champ_label_defense.config(anchor=CENTER)

    #label attaque spé
    champ_label_attaque_spe=Label(info,textvariable=value_label_attaque,font=fontStyle)
    champ_label_attaque_spe.place(x=105,y=553,width=45, height=20)
    champ_label_attaque_spe.config(anchor=CENTER)

    #label défense spé
    champ_label_defense_spe=Label(info,textvariable=value_label_defense_spe,font=fontStyle)
    champ_label_defense_spe.place(x=105,y=584,width=45, height=20)
    champ_label_defense_spe.config(anchor=CENTER)

    #label vitesse
    champ_label_vitesse=Label(info,textvariable=value_label_vitesse,font=fontStyle)
    champ_label_vitesse.place(x=105,y=617,width=45, height=20)
    champ_label_vitesse.config(anchor=CENTER)

    #label id
    champ_label_id=Label(info,textvariable=value_label_id,font=fontStyle)
    champ_label_id.place(x=505,y=160,width=45, height=30)
    champ_label_id.config(anchor=CENTER)

    #label texte avant dresseur
    champ_label_dresseur_text=Label(info,text='Ce pokemon appartient à :',font=fontStyle)
    champ_label_dresseur_text.place(x=461,y=397,width=330, height=30)
    champ_label_dresseur_text.config(anchor=CENTER)

    #label nom dresseur
    champ_label_dresseur=Label(info,textvariable=value_label_dresseur,font=fontStyle)
    champ_label_dresseur.place(x=480,y=440,width=290, height=30)
    champ_label_dresseur.config(anchor=CENTER)

    #label image pokemon
    image_pokemon = Label(info, image="")
    image_pokemon.place(x=26,y=130,width=296, height=192)

    #label image type
    image_types = Label(info, image="",borderwidth=-1, relief=FLAT, border=-1,background='#e74e4e')
    image_types.place(x=625,y=195,width=70, height=30)


    """
    -------------------FIN---------------------------------------
    """


    """
    Partie recherche et affichage du tableau
    """
    #création d'une variable StringVar
    textBoxRecherche = Entry(info, textvariable=var_texte_recherche, width=20)
    textBoxRecherche.place(x=410,y=635,width=100, height=30)
    #bouton de recherche
    bouton_affichez_pokemon=Button(info, text="Rechercher", command=AffichezListePokemon)
    bouton_affichez_pokemon.place(x=640,y=635,width=150, height=30)


    #récupération de la liste des types dans la base de données avec la fonction RemplirListeDeroulanteTypes qui retoune un tableau.
    tabTypes=RemplirListeDeroulanteTypes()
    #  Création de la Combobox (liste déroulante) , on la remplie avec le tableau préalablement récupérer
    listeDeroulanteTypes = Combobox(info, values=tabTypes)
    # Choisir l'élément qui s'affiche par défaut (ici le premier)
    listeDeroulanteTypes.current(0)
    #positon de la liste dans la fenetre
    listeDeroulanteTypes.place(x=520,y=635,width=110, height=30)


    # Chargement des images :
 
    file_quitter="assets/boutons/back_button.png"
    image_quitter = PhotoImage(file=file_quitter)
    bouton_quitter.configure(image=image_quitter)
    bouton_quitter.image = image_quitter

    file_info_click="assets/boutons/info_click_button.png"
    image_info_click = PhotoImage(file=file_info_click)
    bouton_info.configure(image=image_info_click)
    bouton_info.image = image_info_click

    file_area="assets/boutons/area_button.png"
    image_area = PhotoImage(file=file_area)
    bouton_area.configure(image=image_area)
    bouton_area.image = image_area

    file_background="assets/background/background_info.png"
    image_background = PhotoImage(file=file_background)
    background_label.configure(image=image_background)
    background_label.image = image_background

    
    #création de la grille d'affichage (tableau)
    tree = Treeview(info, columns=('HP', 'Type'))

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



def page_selection():

    global listeDeroulanteDresseur
    global listeDeroulantePokemon
    global var_texte_ajouter_dresseur
    global zone


    zone = 2

    reset()

    selection.place(x=0, y=0)


    background_label = Label(selection, image="")
    background_label.place(x=0, y=0, width=800, height=800)


    #label selection nom dresseur
    champ_label_dresseur=Label(selection,text='Votre nom :',font=fontStyle)
    champ_label_dresseur.place(x=170,y=170,width=145, height=30)
    champ_label_dresseur.config(anchor=CENTER)

    #label selection nom pokemon
    champ_label_pokemon=Label(selection,text='Votre pokemon :',font=fontStyle)
    champ_label_pokemon.place(x=487,y=170,width=200, height=30)
    champ_label_pokemon.config(anchor=CENTER)

    #label selection ajouter dresseur
    champ_label_ajouter_dresseur=Label(selection,text='Ajouter un autre dresseur :',font=fontStyle)
    champ_label_ajouter_dresseur.place(x=60,y=550,width=350, height=30)
    champ_label_ajouter_dresseur.config(anchor=CENTER)

    
    #boutons qui appellent des fonctions :

    bouton_info=Button(selection, image="", command=page_info)
    bouton_info.place(x=55,y=6,width=178, height=55)

    bouton_area=Button(selection, image="", command=page_selection)
    bouton_area.place(x=252,y=6,width=178, height=55)

    bouton_quitter=Button(selection, image="", command=Quit)
    bouton_quitter.place(x=590,y=6,width=178, height=55)

    bouton_valider=Button(selection, text="Valider", command=valider)
    bouton_valider.place(x=487,y=575,width=200, height=30)

    bouton_ajouter_dresseur=Button(selection, text="Ajouter", command=ajouter_dresseur)
    bouton_ajouter_dresseur.place(x=275,y=600,width=50, height=30)



    textBox_ajouter_dresseur = Entry(selection, textvariable=var_texte_ajouter_dresseur, width=20)
    textBox_ajouter_dresseur.place(x=115,y=600,width=150, height=30)



    #récupération de la liste des dresseurs dans la base de données avec la fonction RemplirListeDeroulanteDresseur qui retoune un tableau.
    tabDresseur=RemplirListeDeroulanteDresseur()
    #  Création de la Combobox (liste déroulante) , on la remplie avec le tableau préalablement récupérer
    listeDeroulanteDresseur = Combobox(selection, values=tabDresseur)
    # Choisir l'élément qui s'affiche par défaut (ici le premier)
    listeDeroulanteDresseur.current(0)
    #positon de la liste dans la fenetre
    listeDeroulanteDresseur.place(x=140,y=230,width=200, height=30)


    #récupération de la liste des dresseurs dans la base de données avec la fonction RemplirListeDeroulanteDresseur qui retoune un tableau.
    tabPokemon=RemplirListeDeroulantePokemonDresseur()
    #Création de la Combobox (liste déroulante) , on la remplie avec le tableau préalablement récupérer
    listeDeroulantePokemon = Combobox(selection, values=tabPokemon)
    # Choisir l'élément qui s'affiche par défaut (ici le premier)
    listeDeroulantePokemon.current(0)
    #positon de la liste dans la fenetre
    listeDeroulantePokemon.place(x=487,y=230,width=200, height=30)

    bouton_actualiser=Button(selection, text="Actualiser", command=Actualiser)
    bouton_actualiser.place(x=364,y=230,width=100, height=30)


    # Chargement des images :
 
    file_quitter="assets/boutons/back_button.png"
    image_quitter = PhotoImage(file=file_quitter)
    bouton_quitter.configure(image=image_quitter)
    bouton_quitter.image = image_quitter

    file_info="assets/boutons/info_button.png"
    image_info = PhotoImage(file=file_info)
    bouton_info.configure(image=image_info)
    bouton_info.image = image_info

    file_area_click="assets/boutons/area_click_button.png"
    image_area_click = PhotoImage(file=file_area_click)
    bouton_area.configure(image=image_area_click)
    bouton_area.image = image_area_click

    file_background="assets/background/background_selection.png"
    image_background = PhotoImage(file=file_background)
    background_label.configure(image=image_background)
    background_label.image = image_background



def page_area():

    global image_pokemon
    global image_pokemon_dresseur
    global zone

    zone = 3
    
    reset()

    area.place(x=0, y=0)

    background_label = Label(area, image="")
    background_label.place(x=0, y=0, width=800, height=800)


    #boutons qui appellent des fonctions :


    bouton_info=Button(area, image="", command=page_info)
    bouton_info.place(x=55,y=6,width=178, height=55)

    bouton_area=Button(area, image="", command=page_selection)
    bouton_area.place(x=252,y=6,width=178, height=55)

    bouton_quitter=Button(area, image="", command=Quit)
    bouton_quitter.place(x=590,y=6,width=178, height=55)

    bouton_attaquer=Button(area, text="Attaquer", command=attaquer)
    bouton_attaquer.place(x=505,y=685,width=105, height=35)

    bouton_capturer=Button(area, text="Capturer", command=capturer)
    bouton_capturer.place(x=620,y=685,width=105, height=35)

    bouton_stats=Button(area, text="Stats", command=stats)
    bouton_stats.place(x=505,y=730,width=105, height=35)

    bouton_fuir=Button(area, text="Fuir", command=page_info)
    bouton_fuir.place(x=620,y=730,width=105, height=35)

    #label image pokemon du dresseur
    image_pokemon_dresseur = Label(area, image="")
    image_pokemon_dresseur.place(x=0,y=461,width=296, height=192)
    
    #label image pokemon
    image_pokemon = Label(area, image="")
    image_pokemon.place(x=450,y=230,width=296, height=192)

    
    # Chargement des images :
 
    file_quitter="assets/boutons/back_button.png"
    image_quitter = PhotoImage(file=file_quitter)
    bouton_quitter.configure(image=image_quitter)
    bouton_quitter.image = image_quitter

    file_info="assets/boutons/info_button.png"
    image_info = PhotoImage(file=file_info)
    bouton_info.configure(image=image_info)
    bouton_info.image = image_info

    file_area_click="assets/boutons/area_click_button.png"
    image_area_click = PhotoImage(file=file_area_click)
    bouton_area.configure(image=image_area_click)
    bouton_area.image = image_area_click

    file_background="assets/background/background_area.png"
    image_background = PhotoImage(file=file_background)
    background_label.configure(image=image_background)
    background_label.image = image_background

    rencontre()
    actu_pv()

    
    #label nom dresseur
    champ_label_nom_dresseur=Label(area,textvariable=value_label_nom_dresseur,font=fontStyle)
    champ_label_nom_dresseur.place(x=645,y=520,width=140, height=30)
    champ_label_nom_dresseur.config(anchor=CENTER)

    #label nom sauvage
    champ_label_nom=Label(area,textvariable=value_label_nom,font=fontStyle)
    champ_label_nom.place(x=30,y=165,width=140, height=30)
    champ_label_nom.config(anchor=CENTER)

    #label texte_area
    champ_label_texte_area=Label(area,textvariable=value_label_texte_area,font=fontStyle2)
    champ_label_texte_area.place(x=45,y=680,width=450, height=90)
    champ_label_texte_area.config(anchor=W)

    value_label_texte_area.set('Que voulez vous faire ?')


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Programme XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


#création de la fenetre Tkinter
fenetre=Tk()
fenetre.geometry("800x800")
fenetre.title('Pokédex BONUS')

fontStyle = tkFont.Font(family="Terminal", size=12, weight="bold")
fontStyle2 = tkFont.Font(family="Terminal", size=12)

info = Canvas(fenetre, width=800, height=800)
selection = Canvas(fenetre, width=800, height=800)
area = Canvas(fenetre, width=800, height=800)


#On crée un label(lignedetexte) souhaitant labienvenue
#Note:lepremier paramètre passé au constructeur de Label est notre fenétre

value_label_nom = StringVar()
value_label_hp = StringVar()
value_label_attaque = StringVar()
value_label_defense = StringVar()
value_label_attaque_spe = StringVar()
value_label_defense_spe = StringVar()
value_label_vitesse = StringVar()
value_label_id = StringVar()
value_label_dresseur = StringVar()
var_texte_recherche = StringVar()
var_texte_ajouter_dresseur = StringVar()

value_label_nom_dresseur = StringVar()
value_label_hp_dresseur = StringVar()
value_label_attaque_dresseur = StringVar()
value_label_defense_dresseur = StringVar()
value_label_attaque_spe_dresseur = StringVar()
value_label_defense_spe_dresseur = StringVar()
value_label_vitesse_dresseur = StringVar()
value_label_texte_area = StringVar()

value_label_pokemon_posseder = StringVar()
value_label_hp_restant = StringVar()
value_label_hp_restant_dresseur = StringVar()


page_info()

mb.showinfo('Infos','Ceci est la version bonus : \n Il y a 3 boutons en haut de la fenêtre : \n INFO pour le afficher le pokedex, AREA pour combattre et capturer des pokemons et BACK pour quitter :)')

#On démarre la boucle Tkinter qui s'interrompt quand on ferme la fenêtre

info.mainloop()
