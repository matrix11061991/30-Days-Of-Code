def shadBinToDec(chaine) :
    rang = len(chaine) - 1
    resultat = 0
    for i in range (len(chaine)):
        if chaine[i] == "1":
            resultat += 2 ** rang
        rang -= 1
    return resultat
#   En local ça ne marche pas sans le mot clé : "print"!!!
print(shadBinToDec('11111101'))