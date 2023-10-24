ma_liste = [1, 2, 3, 4, 5, 9, 7]
z = 10
def addEntier (k, list) :
    listEntierAdd = []

    for i in range(len(list)):

        for a in range(i + 1, len(list)):

            if list[i] + list[a] == k :

                listEntierAdd.append((list[i], list[a]))
    
    return listEntierAdd

x = addEntier(z, ma_liste)

if x:
    print("Les combinaisons qui donnent", z, "sont :", x)
else:
    print("Aucune combinaison trouvée.")

