import Character
from Grid import Grid
import random


class Civilizaiton():
    def __init__(self, grid):
        self.character = None
        self.id = ""
        self.life = 0
        self.alive = False
        self.tech = 0
        self.lifeConsume = 0
        self.strength = 0
        self.attack = 0
        self.defense = 0
        self.blackholeTrans = 0
        self.ownedSpace = [grid]
        self.frontierSpace = [grid]
        self.occupyingSpace = []

        grid.occupyTime = 0
        self.initializeEntity()

    def initializeEntity(self):
        self.character = Character.getCharacter()
        self.id = self.character + self.tool.generateNumber(6)
        self.life = 10000
        self.tech = 100
        self.alive = True
        if self.character == "A":
            self.lifeConsume = 0.01
            self.blackholeTrans = 10
        elif self.character == "F":
            self.lifeConsume = 0.02
            self.defense = 100
        else:
            self.lifeConsume = 0.04
            self.attack = 200

        self.strength = self.strengthCal()

    def strengthCal(self):
        return (self.life / 100) * (self.tech / 20) * ((self.attack + self.defense + self.blackholeTrans) / 100)