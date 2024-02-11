#class Fibonacci:
   # def __init__ (self, a, b, c, d):
   #     self.a = a
   #     self.b = b
   #     self.c = c
   #     self.d = d
# F(n)=F(n−1)+F(n−2)
## Calcul d'une valeur donnée a à un index n donné.
# a(n+1) = a(n) + a(n-1)

# Suite def: reel /reel/reel/reel/reel sdsdsdsd
# a(0) = 0
# a(1) = 1
# a(n+1) = a(n) + a(n-1) pour tout entier n >= 1

getStartValue = int(input("Valeur d'index de départ pour la suite de Fibonacci : "))

# Refactoriser: passer dans une fonction

getStopValue = int(input("Valeur d'arrêt pour la suite de Fibonacci : "))    

def getFibonacci(startValue, stopValue): #self,  
    a = 0
    b = 1
    c: int
    d = [a, b]
    getValidIndex(isValid):

    try:
        print(d[startValue])
    except:
        print("Erreur, dépassement d'index")
        #computeSerie(d.append(startValue))
    for element in range(d[startValue], stopValue):
        print(d[element]) # affiche la liste à l'index de l'élément passé dans la boucle
        c = b + a
        d.append(c)
        a = b
        b = c
        #print(d) # print(d) --> affiche toute la liste
        if len(d) == stopValue+2:
            print(d)
    return(d)
# print(d) # print(d) --> affiche toute la liste 
# finalD = d

getFibonacci(getStartValue, getStopValue)
           
#getFibonacci(10)
#getFibonacci(20)