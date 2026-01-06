class Bangladesh:
    def capital(self):
        print("Dhaka is the capital of Bangladesh")

    def Language(self):
        print("The official language of Bangladesh is Bengali")

    def type(self):
        print("Bangladesh is a developing country")

class West_Indies:

    def capital(self):
        print("Kingston is the capital of Jamaica")

    def Language(self):
        print("The official language of Jamaica is English")

    def type(self):
        print("Jamaica is a developing country")


obj_bd= Bangladesh()
obj_WI= West_Indies()

for country in (obj_bd, obj_WI):
    country.capital()
    country.Language()
    country.type()
    
    