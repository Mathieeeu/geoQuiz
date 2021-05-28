import sqlite3
from random import *
question=1

class pays: # définition d'une classe pays pour y attribuer tout les attributs

    def __init__(self,nom,capitale,population,point_culminant,superficie,frontieres,langue,continent,fuseaux,antarctique,tel,acces_mer,couleurs_drapeau,long_frontieres,long_cotes,mots):
        self.nom=nom
        self.capitale=capitale
        self.population=population
        self.point_culminant=point_culminant
        self.superficie=superficie
        self.frontieres=frontieres
        self.langue=langue
        self.continent=continent
        self.fuseaux=fuseaux
        self.antarctique=antarctique
        self.tel=tel#
        self.acces_mer=acces_mer#
        self.couleurs_drapeau=couleurs_drapeau
        self.long_frontieres=long_frontieres#
        self.long_cotes=long_cotes#
        self.perimetre=long_cotes+long_frontieres#
        self.mots=mots

    def affichageinfos(self): # affcihe les informations du pays (PAS ENCORE IMPLEMENTE DANS MAIN)
        infos=[self.nom,self.capitale,self.population,self.point_culminant,self.superficie,self.frontieres,self.langue,self.continent,self.fuseaux]
        return infos



def connexion(): # connexion à la base de données pays
    try:
        #connexion à la bdd
        sqliteConnection = sqlite3.connect('pays.db')
        return sqliteConnection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite : ", error)


def deconnexion(sqliteConnection): # déconnexion à la base de données pays
   if (sqliteConnection):
       #fermeture de la co
            sqliteConnection.close()
            print("The SQLite connection is closed")

def infos():
    return str(pays.affichageinfos())

def random(): # genere un nombre aléatoire et l'associe à une pays
    chiffre=randint(1,199)
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = ("select nom from pays where idPays="+str(chiffre))
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    record= record[0][0]
    return record

def AffichezDB(nom_pays): # donne tous les attributs du pays selectionné
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = ("select * from pays where nom=\""+str(nom_pays)+"\"")
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    pays1 = pays(record[0][1],record[0][2],record[0][3],record[0][4],record[0][5],record[0][6],record[0][7],record[0][8],record[0][9],record[0][10],record[0][11],record[0][12],record[0][13],record[0][14],record[0][15],record[0][16],)
    return pays1


def donne_infos_pays(nom_pays): # permet de renvoyer toutes les informations du pays
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = ("select * from pays where nom=\""+str(nom_pays)+"\"")
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    return record


      
def question(pays,attribut): # donne les valeurs des pays en fonction de l'attribut (ex : si le pays est France et l'attribut est capitale, les valeurs peuvent être O et Q : l'initiale de la capitale de la france est entre O et Q
    global selecteur, mot
    val_min,val_max=0,0 #
    
    if attribut == "superficie_entre":
        liste=[0,100,1000,5000,25000,50000,100000,200000,500000,1000000,2000000] # 0 100 1k 5k 25k 50k 100k 200k 500k 1M 2M
        for i in range(len(liste)):
            try:
                val_min=liste[i+1]
            except:
                val_min=9999999999
            if liste[i] <= pays.superficie and pays.superficie <= val_min :
                return(liste[i],val_min)

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

    elif attribut == "point_culminant":
        liste=[0,500,1500,2500,4000,6000] 
        for i in range(len(liste)):
            try:
                val_min=liste[i+1]
            except:
                val_min=9999
            if liste[i] <= int(pays.point_culminant) and int(pays.point_culminant) <= val_min :
                return(liste[i],val_min)
            
    elif attribut == "population_entre":
        liste=[0,10000,100000,1000000,5000000,10000000,25000000,50000000,100000000] #0 10k 100k 1M 5M 10M 25M 50M 100M
        for i in range(len(liste)):
            try:
                val_min=liste[i+1]
            except:
                val_min=9999999999
            if liste[i] <= pays.population and pays.population <= val_min :
                return(liste[i],val_min)
            
    elif attribut == "population_sup":
        liste=[0,10000,100000,1000000,5000000,10000000,25000000] #0 10k 100k 1M 5M 10M 25M
        random = randint(0,len(liste)-1)
        while liste[random] >= pays.population :
            random = randint(0,len(liste)-1)
        return(liste[random])
        

    elif attribut == "population_inf":
        liste=[100000,1000000,5000000,10000000,50000000,25000000,100000000] #100k 1M 5M 10M 25M 50M 100M
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
        bornes=[]
        bornes.append(listealpha.index(mot[0])-randint(0,5))
        bornes.append(listealpha.index(mot[0])+randint(0,5))
        for i in range(2):
            if bornes[i]>25:
                bornes[i]=25
            if bornes[i]<0:
                bornes[i]=0
        return listealpha[bornes[0]],listealpha[bornes[1]]
        
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
        bornes=[]
        bornes.append(listealpha.index(mot[0])-randint(0,5))
        bornes.append(listealpha.index(mot[0])+randint(0,5))
        for i in range(2):
            if bornes[i]>25:
                bornes[i]=25
            if bornes[i]<0:
                bornes[i]=0
        return listealpha[bornes[0]],listealpha[bornes[1]]
          
        
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
            if attribut == "frontieres_2" and len(frontieres)==1:
                return "None"
            return frontieres
        else:
            return ("None")
        
    elif attribut.startswith("continent_"):
        if attribut == "continent_1":
            liste=[pays.continent]
        else :
            listeContinents=["Afrique","Europe","Amérique","Océanie","Asie"]
            listeContinents.pop(listeContinents.index(pays.continent))
            liste = [pays.continent,listeContinents[randint(0,len(listeContinents)-1)],pays.continent]
            liste.pop(choice([0, 2]))
        return liste
        
    elif attribut == "antarctique" :
        return pays.antarctique

    elif attribut == "fuseaux":
        if pays.fuseaux == 1 :
            return pays.fuseaux
        else :
            liste=[2,3,5,8,10,15]
            for i in range(len(liste)):
                val_min=liste[i+1]
                if liste[i] <= pays.fuseaux and pays.fuseaux <= val_min :
                    return(liste[i],val_min)
            
    elif attribut == "langue":
        return pays.langue

    elif attribut == "mots":
        return pays.mots

    elif attribut == "couleurs_drapeau":
        return pays.couleurs_drapeau




def calcul(valeur,attribut): # fonction qui va ajouter pour chaque questions le nombre de pays qui sont possibles, à la fin il faut qu'il n'y ait que 1 réponse possible
    global commandeSQL

    liste_pays_possible=[]

    # définition d'une condition de recherche dans la base de donnees en focntion de l'attributs
    
    if attribut == "initiale_nom" or attribut == "initiale_capitale" or attribut == "initiale_nom_entre" or attribut == "initiale_capitale_entre" :   # POUR LES LETTRES
        attribut=attribut.replace("initiale_","")
        if attribut.endswith("_entre"):
            attribut=attribut.replace("_entre","")
            condition="("            
            for i in range (int(listealpha.index(valeur[1]))-int(listealpha.index(valeur[0]))+1):
                condition +=(attribut + " like \'"+listealpha[listealpha.index(valeur[0])+i]+"%' or ")
            condition += "nettoyeur)"
            condition = condition.replace(" or nettoyeur","")
        else: condition = (attribut + " like \'"+str(valeur)+"%'")

    elif attribut.startswith("frontieres_"):
        condition = "("
        if not valeur == "None":
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
        
    elif attribut == "superficie_entre" or attribut == "population_entre":
        if attribut.endswith("_entre"):
            attribut=attribut.replace("_entre","")
            condition = (attribut + " > " + str(valeur[0]) + " and " + attribut + " < " + str(valeur[1]))
    
    elif attribut == "antarctique":
        condition = "antarctique = '"+str(valeur)+"'"
        
    elif attribut == "fuseaux":
        if valeur == 1:
            condition = ("fuseaux = "+str(valeur))
        else :
            condition = (attribut + " >= " + str(valeur[0]) + " and " + attribut + " <= " + str(valeur[1]))
        
    elif attribut == "langue":
        condition = "langue = '"+str(valeur)+"'"

    elif attribut == "point_culminant":
        condition = (attribut + " > " + str(valeur[0]) + " and " + attribut + " < " + str(valeur[1]))

    elif attribut == "mots":
        condition = "nombre_mots_nom = "+str(valeur)
        
    elif attribut == "couleurs_drapeau":
        condition = "couleurs_drapeau = "+str(valeur)

    # recherche dans la base de donnees
    
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = ("select nom from pays where "+ condition)
    commandeSQL += (" and "  + sqlite_select_Query.replace("select nom from pays where ",""))

    if commandeSQL.startswith("select nom from pays where  and"):
        commandeSQL=commandeSQL.replace("where  and","where")
    cursor.execute(commandeSQL)
    
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    for row in record :
        liste_pays_possible.append(list(row))
    return(liste_pays_possible)



def lancer_tirage(la_seed): # fonction qui teste si le pays et les attributs forme 5 questions qui marche 
    global commandeSQL ,tirage, nompays, listeQ, pays1, attribut, valeur, issues, listealpha, questions

    seed(la_seed)
    
    listealpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    etape = 5
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    commandeSQL = "select nom from pays where "
    tirage=True

    nompays=random()

    # les attributs possibles pour chaque questions
    listeQ0=["initiale_nom_entre","initiale_capitale_entre","continent_2","continent_1"]
    listeQ1=["initiale_nom","initiale_capitale","population_entre","initiale_nom_entre","initiale_capitale_entre","continent_1","continent_2","point_culminant","couleurs_drapeau"]
    listeQ2=["superficie_entre","initiale_nom","initiale_capitale","population_entre","initiale_nom_entre","initiale_capitale_entre","continent_1","continent_2","fuseaux","point_culminant","mots","couleurs_drapeau"]
    listeQ3=["frontieres_1","superficie_entre","initiale_nom","initiale_capitale","population_entre","initiale_nom_entre","initiale_capitale_entre","antarctique","fuseaux","point_culminant","mots","couleurs_drapeau"]
    listeQ4=["frontieres_1","frontieres_2","superficie_entre","initiale_nom","initiale_capitale","population_entre","initiale_nom_entre","initiale_capitale_entre","antarctique","fuseaux","langue","point_culminant","mots","couleurs_drapeau"]

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
    
    pays1=AffichezDB(nompays)

    for etape_en_cours in range(etape):
        if tirage==True:
            attribut = listeQ[etape_en_cours][randint(0,len(listeQ[etape_en_cours])-1)]
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
            elif attribut == "antarctique":
                for chaqueliste in listeQ:
                    for i in chaqueliste:
                        if i == "antarctique":
                            chaqueliste.pop(chaqueliste.index(i))
            elif attribut == "fuseaux":
                for chaqueliste in listeQ:
                    for i in chaqueliste:
                        if i == "fuseaux":
                            chaqueliste.pop(chaqueliste.index(i))
            elif attribut == "langue":
                for chaqueliste in listeQ:
                    for i in chaqueliste:
                        if i == "langue":
                            chaqueliste.pop(chaqueliste.index(i))
            elif attribut == "point_culminant":
                 for chaqueliste in listeQ:
                    for i in chaqueliste:
                        if i == "point_culminant":
                            chaqueliste.pop(chaqueliste.index(i))
            elif attribut == "mots":
                 for chaqueliste in listeQ:
                    for i in chaqueliste:
                        if i == "mots":
                            chaqueliste.pop(chaqueliste.index(i))
            elif attribut == "couleurs_drapeau":
                 for chaqueliste in listeQ:
                    for i in chaqueliste:
                        if i == "couleurs_drapeau":
                            chaqueliste.pop(chaqueliste.index(i))

                            
            valeur = question(pays1,attribut)
            issues = calcul(valeur,attribut)
            ##print("les issues : " + str(issues))

            liste_attributs.append(attribut)
            liste_valeurs.append(valeur)
            liste_reponses.append(issues)

            # Pour que le tirage soit juste, il faut que à la questions 1 il y ait : - de 30 réponses, pour la q2 : -12 réponses, pour la q3 : -7, pour la q4 : -3 , pour la q5 : exactement 1 réponse sinon le tirage est relancé du début avec un autre pays
            if ((len(issues) <= 30 and etape_en_cours == 0) or (len(issues) <= 12 and etape_en_cours == 1) or (len(issues) <= 7 and etape_en_cours == 2)  or (len(issues) <= 3  and etape_en_cours ==3) or (len(issues)!=1  and etape_en_cours ==4) or valeur== None):                            #recherche manouelle
                tirage=False

            infos_pays=donne_infos_pays(nompays)
            # defini une liste d'info qui va etre affiché lorsque le joueur gagne une partie
            liste_infos=[infos_pays[0][1],infos_pays[0][2],infos_pays[0][8],infos_pays[0][3],infos_pays[0][5],int(int(infos_pays[0][14])+int(infos_pays[0][15])),infos_pays[0][7]]

            # si tout est bon le pays est gardé et les listes sont transmises
            if etape_en_cours == 4 and len(issues) == 1 and valeur != None:
                return liste_attributs, liste_valeurs, liste_reponses, liste_infos


    if tirage==False: # le tirage est relancé
        return lancer_tirage(randint(1,1000000))

