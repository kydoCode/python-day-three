class Student:
    # Initier une liste vide: ma_liste = [] ; dans une classe, inutile de mettre les [] dans la signature de la méthode (ligne 4). 
    # On ne spécifie pas explicitement que marks est une liste. Si TypeError: vérifier le typage au gré du traitement de la donnée dans le programme à chaque étape.  Vérifier que le type liste est correct avant de l'assigner à self.marks.
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age  
        self.marks = marks
    
    def add_mark(self, one_mark):
        # Append est une méthode de liste, donc on utilise les (), pas les []
        # -> Ajouter élément one_mark à la liste self.marks -> self.marks.append(one_mark)
        # -> Appeler l'élément d'une liste par son index: nom_de_la_liste[one_mark]
        self.marks.append(one_mark)

    def compute_average(self):
        average = 0

       # Contrôle pour éviter la division par zéro, on peut aussi faire avec try except (gestion des exceptions); passer des print aux étapes intermédiaires pour identifier d'où vient l'erreur / analyser comment circule la donnée.
        
       # if len(self.marks) == 0:
       #     print("Liste vide, abort calcul")
       # else: 
        average = sum(self.marks) / len(self.marks)
        return average
    
    def display_facts(self):
        print(f"Nom: {self.name}")
        print(f"Age: {self.age}")
        print(f"Moyenne: {self.compute_average()}")

# Instances
# Attention à passer les données comme demandées dans la classe, erreurs possibles else (typage dynamique de Python). 
studentOne = Student("Eric", 20, [15, 17, 18, 9, 13]) 
studentTwo = Student("Paul", 17, [17, 9, 2, 8, 11, 16])
studentThree = Student("Julia", 23, [14, 10, 7])
studentFour = Student("Avery", 26, [12])

# print(studentOne.display_facts(), studentTwo.display_facts(), studentThree.display_facts())
studentOne.display_facts()
studentTwo.display_facts()
studentThree.display_facts()
studentFour.display_facts()