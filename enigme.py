def enigme(attribut):
    if attribut=="superficie":
        supermin,supermax = question(pays1,"superficie")
        if supermax == 999999999 :
            return("Ce pays fait plus de " + str(supermin) + " km² !")
        else : return("Ce pays fait entre " + str(supermin) + " et " + str(supermax) + " km² !")
    elif attribut == "population" :
        popmin,popmax = question(pays1,"population")
        if popmax == 999999999 :
            return("Ce pays compte plus de " + str(popmin) + " habitants !")
        else : return("Ce pays compte entre " + str(popmin) + " et " + str(popmax) + " habitants !")
    elif attribut == "initiale_nom" :
        initiale_pays=question(pays1,"initiale_nom")
        return("Ce pays commence par un "+str(initiale_pays))
    elif attribut == "initiale_capitale" :
        initiale_cap=question(pays1,"initiale_capitale")
        return("La capitale de ce pays commence par un "+str(initiale_cap))
    elif attribut == "initiale_capitale_entre" :
        initiale_capmin,initiale_capmax=question(pays1,"initiale_capitale_entre")
        return("La capitale de ce pays commence par une lettre entre "+str(initiale_capmin)+" et " +str(initiale_capmax))
    elif attribut == "initiale_nom_entre" :
        initiale_nommin,initiale_nommax=question(pays1,"initiale_nom_entre")
        return("Le nom de ce pays commence par une lettre entre "+str(initiale_nommin)+" et " +str(initiale_nommax))
    elif attribut == ("frontieres_1"):
        return("ce pays a une frontière commune avec : "+str(question(pays1,"frontieres_1")))
    elif attribut == ("frontieres_2"):
        return("ce pays a des frontières avec : "+str(question(pays1,"frontieres_2")))
    elif attribut== ("continent_1"):
        return("ce pays est sur le continent : "+str(question(pays1,"continent_1")))
