import sqlite3
from random import *

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
    #print (commande)
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()

    return record


#///////////////////////////////////////////////////

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]

#Pays Select
r=randint(1,199)
commande="SELECT * FROM pays WHERE idPays='"+str(r)+"'"

rec=AffichezDB(commande)
print(rec)
print()

#Questions
memory=[-1]
def NewQuest(memory):
    questions=["Le pays commence par une lettre entre ","q2","ok"]
    numéro=randint(0,len(questions)-1)
    if numéro not in memory:
        memory.append(numéro)
        choose(questions[numéro])
        return memory
    else :
        print("fail")

def choose(ASK):
    if ASK=="Le pays commence par une lettre entre ":
        Ques1(ASK)
    elif ASK=="ok":
        print("fuck")
     
def Ques1(question):
    print(rec[0][1])

    z=rec[0][1][0]
    z=z.lower()
    mean=alpha.index(z)

    mini=randint(0,4)
    mini=mean-mini
    minimum=alpha[mini]

    maxi=randint(0,4)
    maxi=mean+maxi
    maximum=alpha[maxi]


    print(str(question)+str(minimum)+" et "+str(maximum))
    print()
    print()
    final=[]
    for i in range(mini,maxi+1):

        other="SELECT nom FROM pays WHERE nom LIKE '"+str(alpha[i])+"%'"

        fin=AffichezDB(other)
        for j in range(0,len(fin)-1):
            final.append(fin[j][0])
    print(final)



def Ques2(question):
    
    
#/////////////////////////////////////////////////////////////////////////
NewQuest(memory)
NewQuest(memory)
NewQuest(memory)
print(memory)





