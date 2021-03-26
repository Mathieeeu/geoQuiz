import sqlite3
from random import *
question=1

def Este(final):
    global E
    E=final
    return E

class pays:

    def __init__(self,nom,capitale,population,point_culminant,superficie,acces_mer,nombre_mots_nom,couleurs_drapeau):
        self.nom=nom
        self.capitale=capitale
        self.population=population
        self.point_culminant=point_culminant
        self.superficie=superficie
        self.mer=acces_mer
        self.nombre_mots_nom=nombre_mots_nom
        self.couleurs_drapeau=couleurs_drapeau
        #self.frontieres=frontieres

    def affichageinfos(self):
        infos=[self.nom,self.capitale,self.population,self.point_culminant,self.superficie,self.mer,self.nombre_mots_nom,self.couleurs_drapeau]
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
    pays1 = pays(record[0][1],record[0][2],record[0][3],record[0][4],record[0][5],record[0][12],record[0][16],record[0][13])
    return pays1

def enigme(attribut):
    
    if attribut=="superficie_entre":
        supermin,supermax = question(pays1,"superficie_entre")
        if supermax == 999999999 :
            print("Ce pays fait plus de " + str(supermin) + " km² !")
            return(supermin)
        else :
            print("Ce pays fait entre " + str(supermin) + " et " + str(supermax) + " km² !")
            return [supermin,supermax]

    if attribut=="superficie_sup":
        supermin = question(pays1,"superficie_sup")
        print("Ce pays fait plus de " + str(supermin) + " km² !")
        return supermin

    if attribut=="superficie_inf":
        supermax = question(pays1,"superficie_inf")
        print("Ce pays fait moins de " + str(supermax) + " km² !")
        return supermax

        
    if attribut == "population_entre" :
        popmin,popmax = question(pays1,"population_entre")
        if popmax == 999999999 :
            print("Ce pays compte plus de " + str(popmin) + " habitants !")
            return popmin
        else :
            print("Ce pays compte entre " + str(popmin) + " et " + str(popmax) + " habitants !")
            return [popmin,popmax]

    if attribut=="population_sup":
        supermin = question(pays1,"superficie_sup")
        print("Ce pays compte plus de " + str(supermin) + " habitants !")
        return supermin

    if attribut=="population_inf":
        supermax = question(pays1,"superficie_inf")
        print("Ce pays compte moins de " + str(supermax) + " habitants !")
        return supermax
    
    if attribut == "initiale_nom" :
        initiale_pays=question(pays1,"initiale_nom")
        return("Ce pays commence par un "+str(initiale_pays))
    
    if attribut == "initiale_capitale" :
        initiale_cap=question(pays1,"initiale_capitale")
        return("La capitale de ce pays commence par un "+str(initiale_cap))
        
        #print(AffichezDB(nompays,listeQ[randint(0,len(listeQ)-1)]))
    
    if attribut == "accès_mer" :
        M=question(pays1,"accès_mer")
        if M == "True":
            print("True")
            return("Ce pays a un accès à la mer")
        elif M == "False":
            print("False")
            return("Ce pays n'a pas d'accès à la mer")
        else:
            print("ERROR ACCES MER")
            
    if attribut=="nombre_mots_nom":
        nbr_mots=question(pays1,"nombre_mots_nom")
        return("Le nom du pays contient "+str(nbr_mots)+" mots")

    if attribut=="couleurs_drapeau":
        nbr_couleurs=question(pays1,"couleurs_drapeau")
        return("Le drapeau du pays contient "+str(nbr_couleurs)+" couleurs")

    if attribut=="point_culminant":
        maxi,mini=question(pays1,"point_culminant")
        return("Le point culminant de ce pays est entre "+str(mini)+"km et "+str(maxi)+"km")

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
    if attribut == "accès_mer":
        return pays1.mer
    if attribut == "nombre_mots_nom":
        return pays1.nombre_mots_nom
    if attribut == "couleurs_drapeau":
        return pays1.couleurs_drapeau
    if attribut == "point_culminant":
        hauteur=pays1.point_culminant/1000
        liste=[0,1,2,3,4,5,6,7,8,9]
        mini=0
        maxi=9
        for i in range(len(liste)):
            if liste[i]<hauteur and liste[i]>mini:
                mini=liste[i]
            elif liste[i]>hauteur and liste[i]<maxi:
                maxi=liste[i]
        return maxi,mini



def calcul(valeur,attribut):
    if attribut == "initiale_nom" or attribut == "initiale_capitale":   # POUR LES LETTRE
        attribut=attribut.replace("initiale_","")
        condition = (attribut + " like \'"+valeur+"%'")
    elif attribut == "superficie_entre" or attribut == "population_entre":                                                                                        #POUR LES CHIFFRES MIAM
        attribut=attribut.replace("_entre","")
        condition = (attribut + " > " + str(valeur[0]) + " and " + attribut + " < " + str(valeur[1]))
    elif attribut == "superficie_sup" or attribut == "population_sup":                                                                                          #POUR LES CHIFFRES MIAM
        attribut=attribut.replace("_sup","")
        condition = (attribut + " > " + str(valeur))
    elif attribut == "superficie_inf" or attribut == "population_inf":                                                                                          #POUR LES CHIFFRES MIAM
        attribut=attribut.replace("_inf","")
        condition = (attribut + " < " + str(valeur))
        
    elif attribut == "accès_mer":                                                                                         #POUR LES CHIFFRES MIAM
        attribut=attribut.replace("è","e")
        if valeur=="Ce pays a un accès à la mer":
            valeur="'True'"
        else:
            valeur="'False'"
        condition = ("acces_mer like " + str(valeur))
        
    elif attribut =="nombre_mots_nom":
        valeur=valeur.replace("Le nom du pays contient ","")
        valeur=valeur.replace(" mots","")
        condition=(str(attribut)+"="+str(valeur))

    elif attribut=="couleurs_drapeau":
        valeur=valeur.replace("Le drapeau du pays contient ","")
        valeur=valeur.replace(" couleurs","")
        condition=(str(attribut)+"="+str(valeur))
    elif attribut=="point_culminant":
        valeur=valeur.replace("Le point culminant de ce pays est entre ","")
        valeur=valeur.replace("km et ","")
        valeur=valeur.replace("km","")
        condition= (attribut + " > " + str(valeur[0]) + "000 and " + attribut + " < " + str(valeur[1])+"000")
    else:
        #attribut=attribut.replace("_entre","")
        condition = (attribut + " > " + str(valeur[0]) + " and " + attribut + " < " + str(valeur[1]))
        
        print(condition)
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = ("select nom from pays where "+ condition)
    print(condition)
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    print()
    print()
    final=[]
    for j in range(0,len(record)-1):
        final.append(record[j][0])
    #print(final)
    Este(final)
    return(len(final))


# listealpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tirage=True
nompays=random()
listeQ=["population_entre","population_sup","population_inf","superficie_entre","superficie_sup","superficie_inf","accès_mer","nombre_mots_nom","couleurs_drapeau","point_culminant"]#,"initiale_nom","initiale_capitale",]
if 1==1:
    
    if tirage==True:
        print("______________________________________________________\n"+str(nompays))
        pays1=AffichezDB(nompays)
        tirage=False
        print(pays1.affichageinfos())
        

        print("\n#############################################")
        attribut = listeQ[randint(0,len(listeQ)-1)]
        attribut="point_culminant"
        valeur = enigme(attribut)
        print(valeur)
        
        issues = calcul(valeur,attribut)
        print(issues)
        #issues = 11
        print("\n\n\nIl y a un cetain nombre de possiblites qui est egal au chiffre suivant ------------>        ",issues)
        

        
        if issues < 10:
            tirage = True


    print("############################")
    #test Esteban --------------------------------------------------------------------------------------------------------------------------
    """
    tirage=True
    nompays=random()
    print("______________________________________________________\n"+str(nompays))
    pays1=AffichezDB(nompays)
    tirage=False
    print(pays1.affichageinfos())
    print("\n\n\n\n")
    Q1=0
    Q2=0
    Q3=0
    Q4=0
    Q5=0
    Q6=0
    Q7=0
    Q8=0
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    p5=[]
    p6=[]
    p7=[]
    p8=[]
    more=0
    for i in range(len(listeQ)):
            
        attribut=listeQ[i]
        valeur=enigme(attribut)
        calcul(valeur,attribut)

        if Q1==0:
            Q1=E
        elif Q2==0:
            Q2=E
        elif Q3==0:
            Q3=E
        elif Q4==0:
            Q4=E
        elif Q5==0:
            Q5=E
        elif Q6==0:
            Q6=E
        elif Q7==0:
            Q7=E
        elif Q8==0:
            Q8=E
            
        else:
            print("Ok check it !")
        print()
    print("\n\n\n\nCHECKED\n\n\n")
    print("Voilà le nombre de réponses entre Q1 et Q8 : "+str(len(Q1))+" "+str(len(Q2))+" "+str(len(Q3))+" "+str(len(Q4))+" "+str(len(Q5))+" "+str(len(Q6))+" "+str(len(Q7))+" "+str(len(Q8))+"\n\n\n")
    POSSIBLE=[]
    #Q more
    a=Q1
    print(len(Q1))
    if len(a)<len(Q2):
        a=Q2
        print("Q2 sup")
        print(len(Q2))
    if len(a)<len(Q3):
        a=Q3
        print("Q3 sup")
        print(len(Q3))
    if len(a)<len(Q4):
        a=Q4
        print("Q4 sup")
        print(len(Q4))
    if len(a)<len(Q5):
        a=Q5
        print("Q5 sup")
        print(len(Q5))
    if len(a)<len(Q6):
        a=Q6
        print("Q6 sup")
        print(len(Q6))
    if len(a)<len(Q7):
        a=Q7
        print("Q7 sup")
        print(len(Q7))
    if len(a)<len(Q8):
        a=Q8
        print("Q8 sup")
        print(len(Q8))
    #Then
    more=0
    print(a)
    #print(str(Q1)+"\n\n"+str(Q2)+"\n\n"+str(Q3)+"\n\n"+str(Q4)+"\n\n"+str(Q5)+"\n\n"+str(Q6)+"\n\n"+str(Q7)+"\n\n"+str(Q8)+"\n\n")
    for i in range(len(a)):
        more=0
        qnumb=[]
        for j in range(7):
            if eval("Q"+str(j+1)).count(a[i])==1:
                more=more+1
                qnumb.append(j)
        if more>=5:
            #print("ajout "+str(a[i]))
            POSSIBLE.append(a[i])
            for z in range(7):
                if qnumb.count(z)==1:
                    eval("p"+str(z+1)).append(a[i])
#        else:
#            print("NONE")
    print()
    print(POSSIBLE)
    print()
    print(len(POSSIBLE))
    print(len(p1))
    print(len(p2))
    print(len(p3))
    print(len(p4))
    print(len(p5))
    print(len(p6))
    print(len(p7))
    print(len(p8))
    """        
        










        
