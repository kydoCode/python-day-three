class Student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = []
    
    def add_mark(self, one_mark):
        self.mark.append[one_mark]
    
    def compute_average(self):
        average = 0
        average = sum(self.mark) / len(self.mark)
        return average
    
    def display_facts(self):
        print(f"Nom: {self.name}")
        print(f"Age: {self.age}")
        print(f"Moyenne: {self.compute_average()}")

# Instances

studentOne = Student("Eric", 20, [15, 17, 18]) 
studentTwo = Student("Paul", 17, 17)
studentThree = Student("Julia", 23, 14)

print(studentOne.display_facts(), studentTwo.display_facts(), studentThree.display_facts())