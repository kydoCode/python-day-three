def compter_lettres(inputString):

    emptyArray = {}

    for element in inputString:
        if element == element.isalpha():
            emptyArray[element] = inputString.count(element)
        return emptyArray

test = compter_lettres("bonjour")
print(test)
testDeux = compter_lettres("Python est génial")
print(testDeux)

# def compter_lettres(inputString):
#    #clé= lettre ; valeur = nb d'occurences
#    #ex : 'b': 2
#
#    for element in inputString:
#        inputString.count(element)
#
#
#    letterAmount = 0 # counter
#    outputDict = {}
#
#    for element in inputString:
#        outputDict[element] = int(element)
#            if element in outputDict == True:
#                letterAmount += 1
# print(outputDict)
