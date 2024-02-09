def compter_lettres(inputString):
    #clé= lettre ; valeur = nb d'occurences
    #ex : 'b': 2

    emptyDic = {}

    for element in inputString:
        counter = inputString.count(element)
        emptyDic[element] = counter
        # emptyDic.append{element: counter}
    return emptyDic

test = compter_lettres("bonjour")
print(test)