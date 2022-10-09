# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy

def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list



def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def factorize(n):
    factor = []
    for i in range(1, n + 1):
        if (n % i == 0):
            factor.append(i)
    factor_answer = ''
    for i in factor:
        factor_answer = factor_answer + str(i) + ' '
    return factor_answer.strip()




class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._type = 'Зелёный дракон'
        self._experience = 10

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(str(x + y))
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._type = 'Красный дракон'
        self._experience = 15

    def question(self):
        x = randint(100, 300)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(str(x - y))
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 20
        self._type = 'Чёрный дракон'
        self._experience = 20

    def question(self):
        x = randint(2,20)
        y = randint(2,20)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(str(x * y))
        return self.__quest




class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class GuessTroll(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 10
        self._type = 'Тролль-генератор'
        self._experience = 20

    def question(self):
        x = randint(1, 5)
        self.__quest = 'Угадай сгенерированное число от 1 до 5'
        self.set_answer(x)
        return self.__quest

class SberPrimeTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 20
        self._type = 'Простой тролль'
        self._experience = 20

    def question(self):
        x = randint(1, 100)
        self.__quest = 'Число', str(x), 'простое?'
        self.set_answer('да' if is_prime(x) else 'нет')
        return self.__quest

class FactorizeTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._type = 'Разложившийся тролль'
        self._experience = 15

    def question(self):
        x = randint(1, 50)
        self.__quest = 'Перечислите через запятую множители числа', str(x)
        self.set_answer(factorize(x))
        return self.__quest

enemy_types = [GreenDragon, RedDragon, BlackDragon, GuessTroll, SberPrimeTroll, FactorizeTroll]
