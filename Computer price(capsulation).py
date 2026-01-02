class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxprice(self, price):
        self.__maxprice = price

c= Computer()
c.sell()

price = int(input("Enter new price: "))
c.__maxprice = price
c.sell()


c.setMaxprice(price)
c.sell()