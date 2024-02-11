# Formule de Fibonacci: 
# F(n)=F(n−1)+F(n−2)
## Calcul d'une valeur donnée a à un index n donné:
# a(n+1) = a(n) + a(n-1)
a = 0
b = 1
c: int
d = [a, b]

stopValue = int(input("Valeur d'arrêt pour la suite de Fibonacci : "))

for element in range(d[0], stopValue):
    print("Element à l'index", element, "dont la valeur stockée dans la liste est:  ", d[element]) # affiche la liste à l'index de l'élément passé dans la boucle
    c = b + a
    d.append(c)
    a, b = b, c
print(d) # print(d) --> affiche toute la liste