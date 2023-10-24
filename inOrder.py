liste = [1, 2, 3, 4]
def listInOrder (list):

    for index in range(len(list) - 1):

        if list[index + 1] > list[index] :
            order = True

        else:
            order= False

    if order == True :
        print( "la liste est dans l'ordre")
        
    else:
        print (" la liste n'est pas dans l'ordre")
    
orderOflist = listInOrder(liste)