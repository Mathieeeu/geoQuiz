def nommer_questions(liste_attributs,liste_valeurs):

    liste_questions=[]

    for i in range(len(liste_attributs)):

        if liste_attributs[i]=="superficie_entre":
            nb1,nb2=espace_zero(int(liste_valeurs[i][0])),espace_zero(int(liste_valeurs[i][1]))
            liste_questions.append("Ce pays fait entre " + str(nb1) + " et " + str(nb2) + " km²")

        elif liste_attributs[i]=="superficie_sup":
            nb1=espace_zero(int(liste_valeurs[i][0]))
            liste_questions.append("Ce pays fait plus de " + str(nb1) + " km²")

        elif liste_attributs[i]=="superficie_inf":
            nb1=espace_zero(int(liste_valeurs[i][0]))
            liste_questions.append("Ce pays fait moins de " + str(nb1) + " km²")

        elif liste_attributs[i]=="population_entre":
            nb1,nb2=espace_zero(int(liste_valeurs[i][0])),espace_zero(int(liste_valeurs[i][1]))
            liste_questions.append("Ce pays possède entre " + str(nb1) + " et " + str(nb2) + " d'habitants")

        elif liste_attributs[i]=="population_sup":
            nb1=espace_zero(int(liste_valeurs[i][0]))
            liste_questions.append("Ce pays possède plus de " + str(nb1) + " habitants")

        elif liste_attributs[i]=="population_inf":
            nb1=espace_zero(int(liste_valeurs[i][0]))
            liste_questions.append("Ce pays possède moins de " + str(nb1) + " habitants")

        elif liste_attributs[i] == "initiale_nom" :
            liste_questions.append("Le nom de ce pays commence par un "+str(liste_valeurs[i]))

        elif liste_attributs[i] == "initiale_nom_entre" :
            liste_questions.append("Le nom de ce pays commence par une lettre entre "+str(liste_valeurs[i][0])+" et " +str(liste_valeurs[i][1]))

        elif liste_attributs[i] == "initiale_capitale" :
            liste_questions.append("Le nom de la capitale de ce pays commence par un "+str(liste_valeurs[i]))

        elif liste_attributs[i] == "initiale_capitale_entre" :
            liste_questions.append("Le nom de la capitale de ce pays commence par une lettre entre "+str(liste_valeurs[i][0])+" et " +str(liste_valeurs[i][1]))

        elif liste_attributs[i] == ("frontieres_1"):
            if liste_valeurs[i] == "None" :
                liste_questions.append("Ce pays est une ile")
            else :
                liste_questions.append("Ce pays a une frontière commune avec "+str(liste_valeurs[i][0]))

        elif liste_attributs[i] == ("frontieres_2"):
            liste_questions.append("Ce pays a des frontières communes avec "+str(liste_valeurs[i][0])+" et "+str(liste_valeurs[i][1]))

        elif liste_attributs[i] == ("continent_1"):
            liste_questions.append("Ce pays est sur le continent "+str(liste_valeurs[i][0]))

        elif liste_attributs[i] == ("continent_2"):
            liste_questions.append("Ce pays est sur le continent "+str(liste_valeurs[i][0])+" ou "+str(liste_valeurs[i][1]))

        elif liste_attributs[i] == ("antarctique"):
            if liste_valeurs[i] == 'True' :
                liste_questions.append("Ce pays possède une partie de l'Antarctique")
            elif liste_valeurs[i] == 'False':
                liste_questions.append("Ce pays ne possède aucune partie de l'Antarctique")
                
        elif liste_attributs[i] == ("fuseaux"):
            if liste_valeurs[i] == 1 :
                liste_questions.append("Ce pays possède un seul fuseau horaire")
            else :
                nb1,nb2=espace_zero(int(liste_valeurs[i][0])),espace_zero(int(liste_valeurs[i][1]))
                liste_questions.append("Ce pays possède entre " + str(nb1) + " et " + str(nb2) + " fuseaux horaires")
            

        elif liste_attributs[i] == ("langue"):
            liste_questions.append("Les habitants de ce pays parlent "+str(liste_valeurs[i]))


        if liste_attributs[i]=="point_culminant":
            nb1,nb2=espace_zero(int(liste_valeurs[i][0])),espace_zero(int(liste_valeurs[i][1]))
            if liste_valeurs[i][1] == 9999:
                liste_questions.append("Le plus haut point de ce pays est supérieur à " +str(nb1)+ " mètres")
            else :
                liste_questions.append("Le plus haut point de ce pays est entre " + str(nb1) + " et " + str(nb2) + " mètres")

        elif liste_attributs[i] == ("mots"):
            if int(liste_valeurs[i]) == 1:
                liste_questions.append("Le nom de ce pays est composé d'un seul mot")
            else :
                liste_questions.append("Le nom de ce pays est composé de "+str(liste_valeurs[i])+" mots")

        elif liste_attributs[i] == ("couleurs_drapeau"):
            if int(liste_valeurs[i]) == 1:
                liste_questions.append("Le fond du drapeau de ce pays est composé d'une seule couleur")
            else :
                liste_questions.append("Le fond du drapeau de ce pays est composé de "+str(liste_valeurs[i])+" couleurs")


                
    return liste_questions

def espace_zero(nombre):
    nombre_espace=str(nombre)
    if nombre>999:
        nombre_espace=nombre_espace[0:-3]+' '+nombre_espace[-3:]
        if nombre>999999:
            nombre_espace=nombre_espace[0:-7]+' '+nombre_espace[-7:]
            if nombre>999999999:
                nombre_espace=nombre_espace[0:-11]+' '+nombre_espace[-11:]
                if nombre>999999999999:
                    nombre_espace=nombre_espace[0:-15]+' '+nombre_espace[-15:]
    return nombre_espace


