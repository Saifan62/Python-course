class Dog:

    species = "Canis lupus familiaris"


    def __init__(self, name, age):
        self.name = name
        self.age = age

Havanse = Dog("Havanse", 4)
Maltese = Dog("Maltese", 3)

print("Dog is a ", Dog.species)
print("Havanse is a ", Havanse.species)
print("Maltese is a ", Maltese.species)
print("{} is {} years old".format(Havanse.name, Havanse.age))
print("{} is {} years old".format(Maltese.name, Maltese.age))

