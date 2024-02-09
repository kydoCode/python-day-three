firstList = [1, 2, 3, 4, 5]
secondList = [-2, 0, 3, 6]
thirdList = [1, 7, 3, 9, 2]
fourthList = [-2, 0, -5, -1]

def plus_grand_element(sequence):
    greatestValue = []
    for element in sequence:
        if element > greatestValue:
            greatestValue += element
    print(greatestValue)

firstSequence = plus_grand_element(firstList)
secondSequence = plus_grand_element(secondList)
thirdSequence = plus_grand_element(thirdList)
fourthSequence = plus_grand_element(fourthList)