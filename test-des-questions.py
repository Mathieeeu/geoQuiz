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

TROUVE=False

def AffichezDB(commande):
    global TROUVE,question
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = commande
    #execution de la requéte
    print ("\n\n\n\n\n\n\n\ncommande = " +commande+ "\n\n\n\n\n\n\n\n\n\n")
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    print("LES PAYS SONT : ")
    print(record)
    print("solution = "+str(len(record))+ " question ="+str(question))
    if len(record)==1 and question == 5:
        print("gtrouvez")
        TROUVE=True
    return record

commande = "select * from pays WHERE "
n=0

def test_question(condition):
    global question,n,commande,listeQ
    print("\n\n\n\n\n\n\n\n\n\n\n\ncondition = "+str(condition)+"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    listeQ.pop(n)
    commande_backup=commande
    print("commande backup = "+str(commande_backup))
    if type(condition)==list:
        commande += (" and (")
        for i in range(len(condition)-1):
            commande += (str(condition[i])+" or ")
            dernier=i
        commande += (str(condition[dernier+1])+")")
    else:
        commande += (" and "+str(condition))
    commande=commande.replace("WHERE  and","WHERE")
    commande=commande.replace("or  and","and")
    record=AffichezDB(commande)
  
    if (question==1 and len(record)<50) or (question==2 and len(record)<25) or (question==3 and len(record)<12) or (question==4 and len(record)<5) or (question==5 and len(record)!=1):
            print("CA MARCHE PAS")
            print(len(listeQ)-1)
            if (len(listeQ)-1)==(-1):
                listeQ=backup()
                print("jai backup")
                print(len(listeQ)-1)
            n=randint(0,len(listeQ)-1)
            commande=commande_backup
            test_question(listeQ[n])

def random():
    chiffre=randint(1,199)
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = ("select nom from pays where idPays="+str(chiffre))
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    record= record[0][0]
    return record

def backup():
    listeQbackup=["nom LIKE '"+str(listealpha[randint(0,25)])+"%'",listeecartpays,"nom LIKE '"+str(listealpha[randint(ecart,ecart*3)])+"%'","nom LIKE '%"+str(listealpha[randint(0,25)])+"'",\
"capitale LIKE '"+str(listealpha[randint(0,25)])+"%'",listeecartcap,"capitale LIKE '"+str(listealpha[randint(0,25)])+"%'"]
    return listeQbackup

#"nom LIKE '%"+str(listealpha[randint(0,25)])+"%'",
#"capitale LIKE '%"+str(listealpha[randint(0,25)])+"%'",
ecart=randint(2,4)

listealpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

listeecartcap=[]
bloc1=randint(0,(25-ecart*2))
for i in range (bloc1,bloc1+ecart*2):
    listeecartcap.append("capitale LIKE '"+str(listealpha[i])+"%'")
    
listeecartpays=[]
bloc1=randint(0,(25-ecart*2))
for i in range (bloc1,bloc1+ecart*2):
    listeecartpays.append("nom LIKE '"+str(listealpha[i])+"%'")

listeQ=["nom LIKE '"+str(listealpha[randint(0,25)])+"%'",listeecartpays,"nom LIKE '"+str(listealpha[randint(ecart,ecart*3)])+"%'","nom LIKE '%"+str(listealpha[randint(0,25)])+"'",\
"capitale LIKE '"+str(listealpha[randint(0,25)])+"%'",listeecartcap,"capitale LIKE '"+str(listealpha[randint(0,25)])+"%'"]
#---------------------------------------------------------------------------------------------
#"frontieres LIKE '"+str(random())+"'",

while TROUVE==False:
    print("LISTEQ EGALE "+str(listeQ))
    if (len(listeQ))==0:
        listeQ=backup()
        print("jai backup")
    n=randint(0,len(listeQ)-1)
    test_question(listeQ[n])
    question+=1
    print("\n\n\n\n\n\n\n\n\n\n_____________________________________________________________________________________\n\n\n\n\n\n\n\n\n\n\n")
