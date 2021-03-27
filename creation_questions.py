import sqlite3
from random import *
question=1
class pays:

    def __init__(self,nom,capitale,population,point_culminant,superficie,frontieres,langue,continent,fuseaux):
        self.nom=nom
        self.capitale=capitale
        self.population=population
        self.point_culminant=point_culminant
        self.superficie=superficie
        self.frontieres=frontieres
        self.langue=langue
        self.continent=continent
        self.fuseaux=fuseaux
        #antarctique
        #tel
        #acces_mer

    def affichageinfos(self):
        infos=[self.nom,self.capitale,self.population,self.point_culminant,self.superficie,self.frontieres,self.langue,self.continent,self.fuseaux]
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
    pays1 = pays(record[0][1],record[0][2],record[0][3],record[0][4],record[0][5],record[0][6],record[0][7],record[0][8],record[0][9])
    return pays1


      
def question(pays,attribut):
    global selecteur, mot
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

    elif attribut == "superficie_sup":
        liste=[0,100,1000,5000,25000,50000,100000,200000,500000] # 0 100 1k 5k 25k 50k 100k 200k 500k
        random = randint(0,len(liste)-1)
        while liste[random] >= pays.superficie :
            random = randint(0,len(liste)-1)
        return(liste[random])

    elif attribut == "superficie_inf":
        liste=[50000,100000,200000,500000,1000000,2000000] # 5k 25k 50k 100k 200k 500k 1M 2M
        random = randint(0,len(liste)-1)
        while liste[random] <= pays.superficie :
            random = randint(0,len(liste)-1)
        return(liste[random])
            
    elif attribut == "population_entre":
        liste=[0,10000,100000,1000000,5000000,10000000,50000000,100000000] #0 10k 100k 1M 5M 10M 50M 100M
        for i in range(len(liste)):
            try:
                i1=liste[i+1]
            except:
                i1=9999999999
            if liste[i] <= pays.population and pays.population <= i1 :
                return(liste[i],i1)
            
    elif attribut == "population_sup":
        liste=[0,10000,100000,1000000,5000000,10000000] #0 10k 100k 1M 5M 10M
        random = randint(0,len(liste)-1)
        while liste[random] >= pays.population :
            random = randint(0,len(liste)-1)
        return(liste[random])
        

    elif attribut == "population_inf":
        liste=[100000,1000000,5000000,10000000,50000000,100000000] #100k 1M 5M 10M 50M 100MM
        random = randint(0,len(liste)-1)
        while liste[random] <= pays.population :
            random = randint(0,len(liste)-1)
        return(liste[random])
            
    elif attribut == "initiale_nom" : 
        mot=pays.nom[0]
        mot = mot.lower()
        mot = mot.replace("é","e")
        mot = mot.replace("î","i")
        mot=mot.upper()
        return mot

    elif attribut == "initiale_nom_entre":
        mot=pays.nom[0]
        mot = mot.lower()
        mot = mot.replace("é","e")
        mot = mot.replace("î","i")
        mot=mot.upper()
        if (listealpha.index(mot[0]) > 6) and (listealpha.index(mot[0]) < 17 ):
            selecteur=randint((listealpha.index(mot[0])-7),listealpha.index(mot[0]))
        elif (listealpha.index(mot[0]) <= 6) :
            selecteur=randint(0,listealpha.index(mot[0]))
        elif (listealpha.index(mot[0]) >= 16):
            selecteur=17
        return listealpha[selecteur],listealpha[selecteur+8]
        
    elif attribut == "initiale_capitale":
        mot=pays.capitale[0]
        mot = mot.lower()
        mot = mot.replace("é","e")
        mot = mot.replace("î","i")
        mot=mot.upper()
        return mot

    elif attribut == "initiale_capitale_entre":
        mot=pays.capitale[0]
        mot = mot.lower()
        mot = mot.replace("é","e")
        mot = mot.replace("î","i")
        mot=mot.upper()
        if (listealpha.index(mot[0]) > 6) and (listealpha.index(mot[0]) < 17 ):
            selecteur=randint((listealpha.index(mot[0])-7),listealpha.index(mot[0]))
        elif (listealpha.index(mot[0]) <= 6) :
            selecteur=randint(0,listealpha.index(mot[0]))
        elif (listealpha.index(mot[0]) >= 16):
            selecteur=17
        return listealpha[selecteur],listealpha[selecteur+8]
          
        
    elif attribut == "frontieres_1" or attribut =="frontieres_2":
        if pays.frontieres!="None":
            listefrontieres=pays.frontieres.split(',')
            frontieres=[]
            for i in range (int(attribut[-1])):
                try:
                    nb=randint(0,len(listefrontieres)-1)
                    frontieres.append(listefrontieres[nb])
                    listefrontieres.pop(nb)
                except:
                    attribut == "frontieres_1"
                    break
            return frontieres
        else:
            return None
        
    elif attribut.startswith("continent_"):
        if attribut == "continent_1":
            liste=[pays.continent]
        else :
            listeContinents=["Afrique","Europe","Amérique","Océanie","Asie"]
            listeContinents.pop(listeContinents.index(pays.continent))
            liste = [pays.continent,listeContinents[randint(0,len(listeContinents)-1)],pays.continent]
            liste.pop(choice([0, 2]))
        return liste
        
   
        
        
    

def calcul(valeur,attribut):
    global commandeSQL

    #print("attribut recherché : "+str(attribut))
    
    if attribut == "initiale_nom" or attribut == "initiale_capitale" or attribut == "initiale_nom_entre" or attribut == "initiale_capitale_entre" :   # POUR LES LETTRE
        attribut=attribut.replace("initiale_","")
        if attribut.endswith("_entre"):
            attribut=attribut.replace("_entre","")
            condition="("
            for i in range (9):
                condition +=(attribut + " like \'"+listealpha[listealpha.index(valeur[0])+i]+"%' or ")
            condition += "nettoyeur)"
            condition = condition.replace(" or nettoyeur","")
        else: condition = (attribut + " like \'"+str(valeur)+"%'")

    elif attribut.startswith("frontieres_"):
        condition = "("
        if not valeur is None:
            for i in valeur:
                condition += ("frontieres like '%" + i + "%' and ")
            condition+="netoyyeru)"
            condition=condition. replace(" and netoyyeru","")
        else: condition = "frontieres = 'None'"

    elif attribut.startswith("continent_"):
        if len(valeur)==1:
            condition = "continent ='"+valeur[0]+"'"
        else :
            condition = "(continent ='"+valeur[0]+"' or continent ='"+valeur[1]+"')"
        
    else :
        if attribut == "superficie_entre" or attribut == "population_entre":
            if attribut.endswith("_entre"):
                attribut=attribut.replace("_entre","")
        ##print("c\'est un else, la valeur est : "+str(valeur[1]))
        condition = (attribut + " > " + str(valeur[0]) + " and " + attribut + " < " + str(valeur[1]))


    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = ("select nom from pays where "+ condition)
    commandeSQL += (" and "  + sqlite_select_Query.replace("select nom from pays where ",""))

    if commandeSQL.startswith("select nom from pays where  and"):
        commandeSQL=commandeSQL.replace("where  and","where")
    ##print("\n\nla commande f'est "+commandeSQL+"\n\n")
    #execution de la requéte
    cursor.execute(commandeSQL)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    print(record)
    return(record)



def lancer_tirage():
    global commandeSQL ,tirage, nompays, listeQ, pays1, attribut, valeur, issues, listealpha, questions
    
    
    listealpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    etape = 5
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    commandeSQL = "select nom from pays where "
    tirage=True

    nompays=random()
    listeQ0=["initiale_nom_entre","initiale_capitale_entre","continent_2"]
    listeQ1=["initiale_nom","initiale_capitale","population_entre","initiale_nom_entre","initiale_capitale_entre","continent_1","continent_2"]
    listeQ2=["superficie_entre","initiale_nom","initiale_capitale","population_entre","initiale_nom_entre","initiale_capitale_entre","continent_1","continent_2"]
    listeQ3=["frontieres_1","superficie_entre","initiale_nom","initiale_capitale","population_entre","initiale_nom_entre","initiale_capitale_entre"]
    listeQ4=["frontieres_1","frontieres_2","superficie_entre","initiale_nom","initiale_capitale","population_entre","initiale_nom_entre","initiale_capitale_entre"]

    listeQbackup=[]
    listeQbackup.append(listeQ0)
    listeQbackup.append(listeQ1)
    listeQbackup.append(listeQ2)
    listeQbackup.append(listeQ3)
    listeQbackup.append(listeQ4)

    listeQ=listeQbackup.copy()


    liste_attributs =[]
    liste_valeurs=[]
    liste_reponses=[]
    

    #print("______________________________________________________\n Le pays : "+str(nompays))
    pays1=AffichezDB(nompays)

    
    #print("les infos du pays : "+str(pays1.affichageinfos()))


    #print("\n#############################################")


    for j in range(etape):
        if tirage==True:
            attribut = listeQ[j][randint(0,len(listeQ[j])-1)]
            for chaqueliste in listeQ:
                for i in chaqueliste:
                    try:
                            chaqueliste.pop(chaqueliste.index(attribut))
                    except: None
            if attribut.endswith("_2"):
                for chaqueliste in listeQ:
                    for i in chaqueliste:
                        try:
                            chaqueliste.pop(chaqueliste.index(attribut.replace("_2","_1")))
                        except: None
            if attribut.endswith("_1"):
                for chaqueliste in listeQ:
                    for i in chaqueliste:
                        try:
                            chaqueliste.pop(chaqueliste.index(attribut.replace("_1","_2")))
                        except: None


                                        
            elif attribut.startswith("superficie"):
                for chaqueliste in listeQ:
                    for i in chaqueliste:
                        if i.startswith("superficie"):
                            chaqueliste.pop(chaqueliste.index(i))
            elif attribut.startswith("population"):
                for chaqueliste in listeQ:
                     for i in chaqueliste:
                        if i.startswith("population"):
                            chaqueliste.pop(chaqueliste.index(i))
            elif attribut.startswith("initiale_nom"):
                for chaqueliste in listeQ:
                    for i in chaqueliste:
                        if i.startswith("initiale_nom"):
                            chaqueliste.pop(chaqueliste.index(i))
            elif attribut.startswith("initiale_capitale"):
                for chaqueliste in listeQ:
                    for i in chaqueliste:
                        if i.startswith("initiale_capitale"):
                            chaqueliste.pop(chaqueliste.index(i))

                            
            valeur = question(pays1,attribut)
            issues = calcul(valeur,attribut)
            ##print("les issues : " + str(issues))

            liste_attributs.append(attribut)
            liste_valeurs.append(valeur)
            liste_reponses.append(issues)

            
            if ((len(issues) <= 30 and j == 0) or (len(issues) <= 12 and j == 1) or (len(issues) <= 7 and j == 2)  or (len(issues) <= 3  and j ==3) or (len(issues)!=1  and j ==4)):                            #recherche manouelle
                tirage=False
                    
            #print("étape :"+str(j+1))
            if j == 4 and len(issues) == 1:
                #print("le résultat final est : attributs : "+str(liste_attributs) +" valeurs : " + str(liste_valeurs) + " reponses :" + str(liste_reponses))
                #return [liste_attributs],[liste_valeurs],[liste_reponses]
                #print(liste_attributs)
                return liste_reponses


    if tirage==False:
        return lancer_tirage()



        
    
#lancer_tirage()
