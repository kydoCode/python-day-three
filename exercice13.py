firstList = [1, 2, 3, 4, 5]
secondList = [-2, 0, 3, 6]

def somme_elements(sequence):
    addValues = 0
    for element in sequence:
        addValues += element
    print(addValues)

firstSequence = somme_elements(firstList)
secondSequence = somme_elements(secondList)

