def simp(mot):
    mot = mot.lower()
    mot = mot.replace("ç","c") 
    mot = mot.replace("top1","irak")
    mot = mot.replace("usa","etats unis")
    mot = mot.replace("rdc","republique démocratique du congo")
    mot = mot.replace("bosnie","bosnie herzegovine")
    mot = mot.replace("emirats","emirats arabes unis")
    mot = mot.replace("timor","timor oriental")
    mot = mot.replace("antigua","antigua et barbuda")
    mot = mot.replace("papouasie","papouasie nouvelle guinee")
    mot = mot.replace("macedoine","macedoine du nord")
    mot = mot.replace("saint christophe","saint christophe et nieves")
    mot = mot.replace("saint vincent","saint vincent et les grenadines")
    mot = mot.replace("sao tome","sao tome et principe")
    mot = mot.replace("trinite","trinite et tobago")
    mot = mot.replace("-"," ")
    mot = mot.replace("'"," ")
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
    return(mot)

def simp_liste(liste):
    liste2=[]
    for i in range(len(liste)):
        liste2.append(simp(liste[i]))
    return liste2

def simp_liste_p2(liste):
    liste2=[]
    for i in range(len(liste)):
        liste2.append(simp_liste(liste[i]))
    return liste2

def simp_liste_p3(liste):
    liste2=[]
    for i in range(len(liste)):
        liste2.append(simp_liste_p2(liste[i]))
    return liste2
