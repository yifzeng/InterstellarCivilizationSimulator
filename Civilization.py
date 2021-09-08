import Character
import Tools
from Grid import Grid
import random


class Civilizaiton():
    def __init__(self, grid):
        self.character = None
        self.id = ""
        self.color = (0, 0, 0)
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
        self.init()

    def init(self):
        self.character = Character.getCharacter()
        self.id = self.character + Tools.generateSeq(6)
        self.color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        if self.color == (200, 200, 200) or self.color == (255, 255, 255):
            self.color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
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