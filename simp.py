def simp(mot):
    mot = mot.lower()
    mot = mot.replace("-"," ")
    mot = mot.replace("é","e")
    mot = mot.replace("è","e")
    mot = mot.replace("ç","c")
    mot = mot.replace("ê","e")
    mot = mot.replace("ë","e")
    return(mot)