import sqlite3
from random import *
#question=1
class pays:

    def __init__(self,nom,capitale,population,point_culminant,superficie):
        self.nom=nom
        self.capitale=capitale
        self.population=population
        self.point_culminant=point_culminant
        self.superficie=superficie
        #self.frontieres=frontieres

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
    
    if attribut=="superficie_entre":
        supermin,supermax = question(pays1,"superficie_entre")
        if supermax == 999999999 :
            la_question =("Ce pays fait plus de " + str(supermin) + " km² !")
            return [la_question,supermin]
        else :
            la_question =("Ce pays fait entre " + str(supermin) + " et " + str(supermax) + " km² !")
            return [la_question,supermin,supermax]

    if attribut=="superficie_sup":
        supermin = question(pays1,"superficie_sup")
        la_question =("Ce pays fait plus de " + str(supermin) + " km² !")
        return [la_question,supermin]

    if attribut=="superficie_inf":
        supermax = question(pays1,"superficie_inf")
        la_question =("Ce pays fait moins de " + str(supermax) + " km² !")
        return [la_question,supermax]

        
    if attribut == "population_entre" :
        popmin,popmax = question(pays1,"population_entre")
        if popmax == 999999999 :
            la_question =("Ce pays compte plus de " + str(popmin) + " habitants !")
            return [la_question,popmin]
        else :
            la_question =("Ce pays compte entre " + str(popmin) + " et " + str(popmax) + " habitants !")
            return [la_question,popmin,popmax]

    if attribut=="population_sup":
        supermin = question(pays1,"superficie_sup")
        la_question =("Ce pays compte plus de " + str(supermin) + " habitants !")
        return [la_question,supermin]

    if attribut=="population_inf":
        supermax = question(pays1,"superficie_inf")
        la_question =("Ce pays compte moins de " + str(supermax) + " habitants !")
        return [la_question,supermax]


    
        
    if attribut == "initiale_nom" :
        initiale_pays=question(pays1,"initiale_nom")
        la_question =("Ce pays commence par un "+str(initiale_pays))
        return [la_question,initiale_pays]
    
    if attribut == "initiale_capitale" :
        initiale_cap=question(pays1,"initiale_capitale")
        la_question =("La capitale de ce pays commence par un "+str(initiale_cap))
        return [la_question,initiale_cap]

        
        #print(AffichezDB(nompays,listeQ[randint(0,len(listeQ)-1)]))

def question(pays,attribut):
    i1,i2=0,0
    if attribut == "superficie_entre":
        liste=[0,100,1000,5000,25000,50000,100000,200000,500000,1000000,2000000] # 0 100 1k 5k 25k 50k 100k 200k 500k 1M 2M
        for i in range(len(liste)):
            try:
                i1=liste[i+1]
            except:
                i1=9999999999
            if liste[i] <= pays.superficie and pays.superficie <= i1 :
                return(liste[i],i1)



    if attribut == "superficie_sup":
        liste=[0,100,1000,5000,25000,50000,100000,200000,500000] # 0 100 1k 5k 25k 50k 100k 200k 500k
        random = randint(0,len(liste)-1)
        while liste[random] >= pays.superficie :
            random = randint(0,len(liste)-1)
        return(liste[random])
        

    if attribut == "superficie_inf":
        liste=[50000,100000,200000,500000,1000000,2000000] # 5k 25k 50k 100k 200k 500k 1M 2M
        random = randint(0,len(liste)-1)
        while liste[random] <= pays.superficie :
            random = randint(0,len(liste)-1)
        return(liste[random])



            
    if attribut == "population_entre":
        liste=[0,10000,100000,1000000,5000000,10000000,50000000,100000000] #0 10k 100k 1M 5M 10M 50M 100M
        for i in range(len(liste)):
            try:
                i1=liste[i+1]
            except:
                i1=9999999999
            if liste[i] <= pays.population and pays.population <= i1 :
                return(liste[i],i1)

    if attribut == "population_sup":
        liste=[0,10000,100000,1000000,5000000,10000000] #0 10k 100k 1M 5M 10M
        random = randint(0,len(liste)-1)
        while liste[random] >= pays.population :
            random = randint(0,len(liste)-1)
        return(liste[random])
        

    if attribut == "population_inf":
        liste=[100000,1000000,5000000,10000000,50000000,100000000] #100k 1M 5M 10M 50M 100MM
        random = randint(0,len(liste)-1)
        while liste[random] <= pays.population :
            random = randint(0,len(liste)-1)
        return(liste[random])
            
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
    if attribut == "initiale_nom" or attribut == "initiale_capitale":   # POUR LES LETTRE
        attribut=attribut.replace("initiale_","")
        condition = (attribut + " like \'"+"E"+"%'")
    elif attribut == "superficie_entre" or attribut == "population_entre":                                                                                        #POUR LES CHIFFRES MIAM
        attribut=attribut.replace("_entre","")
        condition = (attribut + " > " + str(valeur[1]) + " and " + attribut + " < " + str(valeur[2]))
    elif attribut == "superficie_sup" or attribut == "population_sup":                                                                                          #POUR LES CHIFFRES MIAM
        attribut=attribut.replace("_sup","")
        condition = (attribut + " > " + str(valeur[1]))
    elif attribut == "superficie_inf" or attribut == "population_inf":                                                                                          #POUR LES CHIFFRES MIAM
        attribut=attribut.replace("_inf","")
        condition = (attribut + " < " + str(valeur[1]))
    else:
        #attribut=attribut.replace("_entre","")
        condition = (attribut + " > " + str(valeur[1]) + " and " + attribut + " < " + str(valeur[2]))
        
        #print(condition)
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = ("select nom from pays where "+ condition)
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    print()
    print()
    final=[]
    for j in range(0,len(record)):
        final.append(record[j][0])
    #print(final)
    return(final)



# listealpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def lancer_tirage():
    global tirage, nompays, listeQ, pays1, attribut, valeur, issues
    tirage=True
    nompays=random()
    listeQ=["initiale_nom"]#,"initiale_capitale","population_entre","population_sup","population_inf","superficie_entre","superficie_sup","superficie_inf"]

    if tirage==True:
        print("______________________________________________________\n"+str(nompays))
        pays1=AffichezDB(nompays)
        tirage=False
        print(pays1.affichageinfos())
        

        print("\n#############################################")
        attribut = listeQ[randint(0,len(listeQ)-1)]
        #attribut = "superficie_entre"
        print(attribut)
        valeur = enigme(attribut)
        print(valeur[0])
        issues = calcul(valeur,attribut)
        print(issues)
        #issues = 11
        #print("\n\n\nIl y a un cetain combre de possiblites qui est egal au chiffre suviant ------------>        ",len(issues))
        return valeur[0],issues
        
        #if issues < 10:
           # tirage = True
        if input("")=="":
            nompays=random()
            tirage=True
    
        
