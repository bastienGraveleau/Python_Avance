def mediane(liste):
    liste_triee = sorted(liste)

    n = len(liste_triee)

    if n % 2 == 1:
        mediane = liste_triee[n // 2]
    else:
        mediane = (liste_triee[n // 2 - 1] + liste_triee[n // 2]) / 2

    return mediane

ma_liste = [5, 2, 3, 6, 9, 8, 7, 45]
result = mediane(ma_liste)
print("La médiane de la liste est :", result)