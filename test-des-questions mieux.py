import sqlite3
from random import *
question=1
class pays:

    def __init__(self,nom,capitale,population,point_culminant,superficie):
        self.nom=nom
        self.capitale=capitale
        self.population=population
        self.point_culminant=point_culminant
        self.superficie=superficie

    def affichageinfos(self):
        infos=[self.nom,self.capitale,self.population,self.point_culminant,self.superficie]
        return infos
        



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

def AffichezDB(nom):
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = ("select * from pays where nom=\""+str(nom)+"\"")
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    pays1 = pays(record[0][1],record[0][2],record[0][3],record[0][4],record[0][5])
    return pays1



def question(pays,attribut):
    i1,i2=0,0
    if attribut == "superficie":
        liste=[0,100,1000,5000,25000,50000,100000,200000,500000,1000000,2000000] # 0 100 1k 5k 25k 50k 100k 200k 500k 1M 2M
        for i in range(len(liste)):
            try:
                i1=liste[i+1]
            except:
                i1=999999999
            if liste[i] <= pays.superficie and pays.superficie <= i1 :
                return(liste[i],i1)
    if attribut == "population":
        liste=[0,10000,100000,1000000,5000000,10000000,50000000,100000000] #0 10k 100k 1M 5M 10M 50M 100M
        for i in range(len(liste)):
            try:
                i1=liste[i+1]
            except:
                i1=999999999
            if liste[i] <= pays.population and pays.population <= i1 :
                return(liste[i],i1)
    if attribut == "initiale_pays":
        mot=pays.nom[0]
        mot = mot.lower()
        mot = mot.replace("é","e")
        mot = mot.replace("î","i")
        mot=mot.upper()
        return mot
    if attribut == "initiale_cap":
        mot=pays.capitale[0]
        mot = mot.lower()
        mot = mot.replace("é","e")
        mot = mot.replace("î","i")
        mot=mot.upper()
        return mot

    
listealpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#---------------------------------------------------------------------------------------------
tirage=True
nompays=random()
listeQ=["superficie"]
while 1:
    if tirage==True:
        print("______________________________________________________\n"+str(nompays))
        pays1=AffichezDB(nompays)
        tirage=False
        print(pays1.affichageinfos())
        supermin,supermax = question(pays1,"superficie")
        if supermax == 999999999 :
            print("Ce pays fait plus de " + str(supermin) + " km² !")
        else : print("Ce pays fait entre " + str(supermin) + " et " + str(supermax) + " km² !")
        popmin,popmax = question(pays1,"population")
        if popmax == 999999999 :
            print("Ce pays compte plus de " + str(popmin) + " habitants !")
        else : print("Ce pays compte entre " + str(popmin) + " et " + str(popmax) + " habitants !")
        initiale_pays=question(pays1,"initiale_pays")
        print("Ce pays commence par un "+str(initiale_pays))
        initiale_cap=question(pays1,"initiale_cap")
        print("La capitale de ce pays commence par un "+str(initiale_cap))
        #print(AffichezDB(nompays,listeQ[randint(0,len(listeQ)-1)]))
    if input("")=="":
        nompays=random()
        tirage=True
