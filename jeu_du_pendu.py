import random

# Array de mots à deviner

words_to_guess = []

# Fonction de génération aléatoire de mots

def generate_words(words_to_guess):
    # words_gen = []
    return random.choice(words_to_guess) #words_gen = 

# Fonction de compte du nb de lettres

def letters_count(inputString):

    emptyArray = {}

    for element in inputString:
        counter = inputString.count(element)
        emptyArray[element] = counter
    return emptyArray
