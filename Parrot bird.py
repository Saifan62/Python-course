class Parrot:

    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is a {}".format(Blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))
