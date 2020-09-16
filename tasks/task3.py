import random


class Cat:

    def __init__(self, number):
        self.number = number
        self.boys = random.randint(0, self.number)
        self.girls = self.number - self.boys

    def getBoysNumber(self):
        print('Количество котят мальчиков:', self.boys)


    def getGirlsNumber(self):
        print('Количество котят девочек:', self.girls)

