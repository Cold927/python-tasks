"""
Задание 3
Написать класс "Кошка". В качестве аргумента, класс принимает число - кол-во котят.
В конструкторе класса случайным образом создаются котята мальчики (кол-во) и
котята девочки (кол-во), общее кол-во которых равно аргументу класса - кол-во котят.
У класса есть два метода: метод "девочки", возвращает кол-во котят девочек и метод "мальчики",
который возвращает кол-во котят мальчиков.

number - общее количество котят
boys - количество котят мальчиков
girls - количество котят девочек
"""
import random


class Cat:

    def __init__(self, number):
        """
        :param number: number of cats
        :type number: type number
        """
        self.number = number
        self.boys = random.randint(0, self.number)
        self.girls = self.number - self.boys

    def getBoysNumber(self):
        print('Количество котят мальчиков:', self.boys)

    def getGirlsNumber(self):
        print('Количество котят девочек:', self.girls)

