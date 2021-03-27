import sqlite3
from random import *
question=1

"""Fonction de connexion permettant de se connecter à la base
"""
def connexion():
    try:
        #connexion à la bdd
        sqliteConnection = sqlite3.connect('pays.db')
        return sqliteConnection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite : ", error)

"""<summary>Fonction de connexion à la bdd</summary>
"""
def deconnexion(sqliteConnection):
   if (sqliteConnection):
       #fermeture de la co
            sqliteConnection.close()
            print("The SQLite connection is closed")

def AffichezDB(commande):

    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = commande
    #execution de la requéte
    print (commande)
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()

    return record

commande = "select * from pays WHERE "
n=1

def test_question(condition):
    global question,n,commande
    commande_backup=commande
    commande += str(condition)
    record=AffichezDB(commande)
  
    if question==1 and len(record)<40:
            commande=commande_backup
            test_question(listeQ1[n+1])
            
    if question==2 and len(record)<25:
            commande=commande_backup
            test_question(listeQ2[n+1])
            
    if question==3 and len(record)<12:
            commande=commande_backup
            test_question(listeQ3[n+1])
            
    if question==4 and len(record)<5:
            commande=commande_backup
            test_question(listeQ4[n+1])
            
    if question==5 and len(record)!=1:
            commande=commande_backup
            test_question(listeQ5[n+1])

def random(colonne):
    chiffre=randint(1,199)
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = ("select nom,"+str(colonne)"+ from pays where "+str(colonne)+"="+str(chiffre))
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    record= record[0][0]
    return record

listeQ=[4,"frontieres LIKE '"+str(random("nom"))+"'","capitale LIKE " ]

test_question(listeQ1[n])
