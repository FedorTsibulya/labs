# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):
    def __init__(self, hero):
        self._health = 100
        self._attack = 50
        self._experience = 0
        self._name = hero

    def attack(self, target):
        target._health -= self._attack

    def gain_exp(self, target):
        self._experience += target._experience

