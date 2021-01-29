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
    #print(record)
    return record

commande = "select nom from pays WHERE "
n=0

def test_question(condition):
    global question,n,commande
    listeQ.pop(n)
    commande_backup=commande
    if type(condition)==list:
        commande=commande.replace(" from pays WHERE","")
        cutcondition = condition[0].split(" ", 2);
        commande += (","+str(cutcondition[0]))
        commande += (" from pays WHERE")
        for i in range(len(condition)):
            cutcondition = condition[i].split(" ", 2);
            commande += (" or "+str(condition[i]))
        commande.replace("WHERE or","WHERE")
    else:
        cutcondition = condition.split(" ", 2);
        commande=commande.replace(" from pays WHERE","")
        commande += (","+str(cutcondition[0])+" from pays WHERE "+str(condition))
    record=AffichezDB(commande)
  
    if (question==1 and len(record)<50) or (question==2 and len(record)<25) or (question==3 and len(record)<12) or (question==4 and len(record)<5) or (question==5 and len(record)!=1):
            n=randint(0,len(listeQ)-1)
            commande=commande_backup
            test_question(listeQ[n])

def random(colonne):
    chiffre=randint(1,199)
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = ("select nom,"+str(colonne)+" from pays where idPays="+str(chiffre))
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    record= record[0][0]
    return record

ecart=randint(2,4)

listealpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
listealphaMAX=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

listeecartcap=[]
bloc1=randint(ecart,len(listealpha)-1-ecart)
for i in range (bloc1,bloc1+ecart*2):
    listeecartcap.append("capitale LIKE '"+str(listealphaMAX[i])+"%'")
    
listeecartpays=[]
bloc1=randint(ecart,len(listealpha)-ecart)
for i in range (bloc1,bloc1+ecart*2):
    listeecartpays.append("pays LIKE '"+str(listealphaMAX[i])+"%'")
listeQ=["frontieres LIKE '"+str(random("nom"))+"'","nom LIKE '"+str(listealphaMAX[randint(0,25)])+"%'",listeecartpays,"nom LIKE '"+str(listealphaMAX[randint(ecart,ecart*3)])+"%'","nom LIKE '%"+str(listealpha[randint(0,25)])+"%'","nom LIKE '%"+str(listealpha[randint(0,25)])+"'",\
"capitale LIKE '"+str(listealphaMAX[randint(0,25)])+"%'",listeecartcap,"capitale LIKE '%"+str(listealpha[randint(0,25)])+"%'","capitale LIKE '"+str(listealpha[randint(0,25)])+"%'"]

#---------------------------------------------------------------------------------------------


for i in range(3):
    n=randint(0,len(listeQ)-1)
    test_question(listeQ[n])
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
