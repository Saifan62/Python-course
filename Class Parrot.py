class Parrot:

    species = "bird"


    def __init__(self, name, age):
        self.name = name
        self.age = age

blu= Parrot("Blu",10)
woo= Parrot("Woo",15)

print("Parrot is a ", Parrot.species)
print("Blu is a ", blu.species)
print("Woo is a ", woo.species)

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
