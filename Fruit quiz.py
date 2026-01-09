import random


class Fruitquiz:

    def __init__(self):

        self.fruits={'apple':'red','orange':'orange','watermelon':'green','banana':'yellow','grape':'purple'}

    def quiz(self):
        while (True):

            fruit,color=random.choice(list(self.fruits.items()))

            print("What is the color of {}".format(fruit))
            user_answer=input("Your answer: ")

            if (user_answer.lower()==color):
                print("Correct!")
            else:
                print("Wrong! The correct answer is {}".format(color))

            option=int(input("Enter 0 to continue or 1 to exit:"))
            if (option):
                    break
        
print("Welcome to Fruit Color Quiz!")
fq=Fruitquiz()
fq.quiz()
        