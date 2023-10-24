def secondMaxNumber (liste):

    if len(list) < 2 :
       return None
    else : 
        maxList = max(liste)
        list.remove(maxList)
        maxList = max(liste)

        return" Voici le deuxiéme plus grand nombre de la liste : " + str(maxList)


list = [5, 6, 8, 3, 49]
second = secondMaxNumber(list)
print(second)