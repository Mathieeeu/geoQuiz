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

def enigme(attribut):
    if attribut=="superficie":
        supermin,supermax = question(pays1,"superficie")
        if supermax == 999999999 :
            return("Ce pays fait plus de " + str(supermin) + " km² !")
        else : return("Ce pays fait entre " + str(supermin) + " et " + str(supermax) + " km² !")
    if attribut == "population" :
        popmin,popmax = question(pays1,"population")
        if popmax == 999999999 :
            return("Ce pays compte plus de " + str(popmin) + " habitants !")
        else : return("Ce pays compte entre " + str(popmin) + " et " + str(popmax) + " habitants !")
    if attribut == "initiale_nom" :
        initiale_pays=question(pays1,"initiale_nom")
        return("Ce pays commence par un "+str(initiale_pays))
    if attribut == "initiale_capitale" :
        initiale_cap=question(pays1,"initiale_capitale")
        return("La capitale de ce pays commence par un "+str(initiale_cap))
        
        #print(AffichezDB(nompays,listeQ[randint(0,len(listeQ)-1)]))

def question(pays,attribut):
    i1,i2=0,0
    if attribut == "superficie":
        liste=[0,100,1000,5000,25000,50000,100000,200000,500000,1000000,2000000] # 0 100 1k 5k 25k 50k 100k 200k 500k 1M 2M
        for i in range(len(liste)):
            try:
                i1=liste[i+1]
            except:
                i1=9999999999
            if liste[i] <= pays.superficie and pays.superficie <= i1 :
                return(liste[i],i1)
    if attribut == "population":
        liste=[0,10000,100000,1000000,5000000,10000000,50000000,100000000] #0 10k 100k 1M 5M 10M 50M 100M
        for i in range(len(liste)):
            try:
                i1=liste[i+1]
            except:
                i1=9999999999
            if liste[i] <= pays.population and pays.population <= i1 :
                return(liste[i],i1)
    if attribut == "initiale_nom":
        mot=pays.nom[0]
        mot = mot.lower()
        mot = mot.replace("é","e")
        mot = mot.replace("î","i")
        mot=mot.upper()
        return mot
    if attribut == "initiale_capitale":
        mot=pays.capitale[0]
        mot = mot.lower()
        mot = mot.replace("é","e")
        mot = mot.replace("î","i")
        mot=mot.upper()
        return mot

def calcul(valeur,attribut):
    global commandeSQL
    if attribut == "initiale_nom" or attribut == "initiale_capitale":   # POUR LES LETTRE
        attribut=attribut.replace("initiale_","")
        condition = (attribut + " like \'"+valeur+"%'")
    else :                                                                                          #POUR LES CHIFFRES MIAM
        condition = (attribut + " > " + str(valeur[0]) + " and " + attribut + " < " + str(valeur[1]))
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = ("select nom from pays where "+ condition)
    commandeSQL += (" and "  + sqlite_select_Query.replace("select nom from pays where ",""))
    if commandeSQL.startswith("select nom from pays where  and"):
        commandeSQL=commandeSQL.replace("where  and","where")
    print("\n\nla commande c'est "+commandeSQL+"\n\n")
    #execution de la requéte
    cursor.execute(commandeSQL)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    print(record)
    return(len(record))


# listealpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
etape = 4
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
commandeSQL = "select nom from pays where "
tirage=True
nompays=random()
listeQ=["superficie","initiale_nom","initiale_capitale","population"]
while 1:
    if tirage==True:
        print("______________________________________________________\n"+str(nompays))
        pays1=AffichezDB(nompays)
        tirage=False
        
        print(pays1.affichageinfos())


        print("\n#############################################")
        for i in range(etape):
            attribut = listeQ[randint(0,len(listeQ)-1)]
            listeQ.pop(listeQ.index(attribut))
            print(listeQ)
            valeur = question(pays1,attribut)
            issues = calcul(valeur,attribut)
            print("\n\n\nIl y a un cetain combre de possiblites qui est egal au chiffre suviant ------------>        ",issues)
        
            print("\n\nla condititon était    --------->",enigme(attribut))
        
            if (issues < 20 and i == 0) or (issues < 10 and i == 1) or (issues < 5 and i == 2)  or (issues!= 1  and i ==3):
                tirage = True
                listeQ=["superficie","initiale_nom","initiale_capitale","population"]
                commandeSQL = "select nom from pays where "
                print("a")
                break
            """
            elif input("")=="":
                nompays=random()
                listeQ=["superficie","initiale_nom","initiale_capitale","population"]
                tirage=True
            """
        
