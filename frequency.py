def frequence_caracteres(chaine):
    frequences = {}

    for caractere in chaine:
        if caractere in frequences:
            frequences[caractere] += 1
        else:
            frequences[caractere] = 1

    return frequences

chaine = "yoyobou"
resultat = frequence_caracteres(chaine)
print(resultat)
