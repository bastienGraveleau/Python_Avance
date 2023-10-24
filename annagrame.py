listMot = ["bonjour", "bjuorno"]

def splitTwo (list):

    mid = len(list) // 2
    first = list[mid:]
    second = list[:mid]
    allfirst = set(first)
    allsecond = set(second)

    if allfirst == allsecond:
        print(first, second)
        return"Les listes contiennent les mêmes lettres."
    else:
        print(first, second)
        return"Les listes ne contiennent pas les mêmes lettres."
    
def annagrameSearch (list):
    allLeter = []

    for l in list :
        for a in l:
            allLeter.append(a)

    listTwo = splitTwo(allLeter)
    return listTwo
        


b = annagrameSearch(listMot)
print (b)
