def simp(mot):
    mot = mot.lower()
    mot = mot.replace("-"," ")
    mot = mot.replace("é","e")
    mot = mot.replace("è","e")
    mot = mot.replace("ç","c")
    mot = mot.replace("ê","e")
    mot = mot.replace("ë","e")
    mot = mot.replace("à","a")
    mot = mot.replace("â","a")
    mot = mot.replace("î","i")
    mot = mot.replace("ï","i")
    mot = mot.replace("ô","o")
    mot = mot.replace("ù","u")
    mot = mot.replace("û","u")
    mot = mot.replace("ü","u")
    mot = mot.replace("æ","ae")
    mot = mot.replace("œ","oe")
    mot = mot.replace("ç","c") 
    mot = mot.replace("dz","algerie")
    mot = mot.replace("baguette","france")
    print(mot)
    return(mot)

def simp_list(liste):
    liste2=[]
    for i in range(len(liste)):
        liste2.append(simp(liste[i]))
    return liste2
