ma_liste = [1, 5, 8, 3, 10, 7] 

def pair (liste):
    max = None
    
    for n in liste:
        if n % 2 == 0:  # Vérifie si le nombre est pair
            if max is None or n > max:
                max = n
    
    if max is not None:
        return max
    else:
        return "Aucun nombre pair trouvé dans la liste"


maxPair = pair(ma_liste)
print(maxPair)