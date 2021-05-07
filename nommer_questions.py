def nommer_questions(liste_attributs,liste_valeurs):

    liste_questions=[]

    for i in range(len(liste_attributs)):

        if liste_attributs[i]=="superficie_entre":
            nb1,nb2=espace_zero(int(liste_valeurs[i][0])),espace_zero(int(liste_valeurs[i][1]))
            liste_questions.append("Ce pays fait entre " + str(nb1) + " et " + str(nb2) + " km²")

        elif liste_attributs[i]=="superficie_sup":
            nb1=espace_zero(int(liste_valeurs[i][0]))
            liste_questions.append("Ce pays fait + de " + str(nb1) + " km²")

        elif liste_attributs[i]=="superficie_inf":
            nb1=espace_zero(int(liste_valeurs[i][0]))
            liste_questions.append("Ce pays fait - de " + str(nb1) + " km²")

        elif liste_attributs[i]=="population_entre":
            nb1,nb2=espace_zero(int(liste_valeurs[i][0])),espace_zero(int(liste_valeurs[i][1]))
            liste_questions.append("Ce pays possède entre " + str(nb1) + " et " + str(nb2) + " d'habitants")

        elif liste_attributs[i]=="population_sup":
            nb1=espace_zero(int(liste_valeurs[i][0]))
            liste_questions.append("Ce pays possède + " + str(nb1) + " d'habitants")

        elif liste_attributs[i]=="population_inf":
            nb1=espace_zero(int(liste_valeurs[i][0]))
            liste_questions.append("Ce pays possède - de " + str(nb1) + " d'habitants")

        elif liste_attributs[i] == "initiale_nom" :
            liste_questions.append("Le nom de ce pays commence par un "+str(liste_valeurs[i]))

        elif liste_attributs[i] == "initiale_nom_entre" :
            liste_questions.append("Le nom de ce pays commence par une lettre entre "+str(liste_valeurs[i][0])+" et " +str(liste_valeurs[i][1]))

        elif liste_attributs[i] == "initiale_capitale" :
            liste_questions.append("Le nom de la capitale de ce pays commence par un "+str(liste_valeurs[i]))

        elif liste_attributs[i] == "initiale_capitale_entre" :
            liste_questions.append("Le nom de la capitale de ce pays commence par une lettre entre "+str(liste_valeurs[i][0])+" et " +str(liste_valeurs[i][1]))

        elif liste_attributs[i] == ("frontieres_1"):
            liste_questions.append("Le pays a une frontière commune avec "+str(liste_valeurs[i][0]))

        elif liste_attributs[i] == ("frontieres_2"):
            liste_questions.append("Le pays a des frontières communes avec "+str(liste_valeurs[i][0])+" et "+str(liste_valeurs[i][1]))

        elif liste_attributs[i] == ("continent_1"):
            liste_questions.append("Le pays est sur le continent "+str(liste_valeurs[i][0]))

        elif liste_attributs[i] == ("continent_2"):
            liste_questions.append("Le pays est sur le continent "+str(liste_valeurs[i][0])+" ou "+str(liste_valeurs[i][1]))

        elif liste_attributs[i] == ("antarctique"):
            if liste_valeurs[i] == 'True' :
                liste_questions.append("Le pays possède une partie de l'Antarctique")
            elif liste_valeurs[i] == 'False':
                liste_questions.append("Le pays ne possède aucune partie de l'Antarctique")
                
        elif liste_attributs[i] == ("fuseaux"):
            nb1,nb2=espace_zero(int(liste_valeurs[i][0])),espace_zero(int(liste_valeurs[i][1]))
            liste_questions.append("Ce pays possède entre " + str(nb1) + " et " + str(nb2) + " fuseaux horaires")       

                
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


