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
        self.speed = 0
        self.strength = 0
        self.attack = 0
        self.defense = 0
        self.blackholeTrans = 0
        self.ownedSpace = []
        self.frontierSpace = [grid]
        self.occupyingSpace = [grid]
        self.absorbList = []
        self.init()

    def init(self):
        self.character = Character.getCharacter()
        self.id = self.character + Tools.generateSeq(6)
        self.frontierSpace[0].owner = self.id
        self.color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        if self.color == (200, 200, 200) or self.color == (255, 255, 255):
            self.color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        self.life = 20
        self.tech = 0.0001
        self.alive = True
        if self.character == "A":
            self.lifeConsume = 1
            self.blackholeTrans = 10
        elif self.character == "F":
            self.lifeConsume = 2
            self.defense = self.defenseCal()
        else:
            self.lifeConsume = 4
            self.attack = self.attackCal()

        self.strength = self.strengthCal()

    def absorb(self, b):
        print(self.id + " absorb method")
        self.life = self.life + b.life
        self.tech = self.tech + b.tech
        for grid in b.ownedSpace:
            grid.owner = self.id
        self.ownedSpace = self.ownedSpace + b.ownedSpace
        self.frontierSpace = self.frontierSpace + b.frontierSpace
        self.occupyingSpace = self.occupyingSpace + b.occupyingSpace
        self.absorbList = self.absorbList + b.absorbList
        b.alive = False

    def strengthCal(self):
        return round((self.life * self.tech), 8)

    def attackCal(self):
        return round(self.life * (1 + self.tech), 8)

    def defenseCal(self):
        return round(self.life * (1 + self.tech), 8)

    def getStrength(self):
        self.strength = self.strengthCal()
        return self.strength

    def getAttack(self):
        self.attack = self.attackCal()
        return self.attack

    def getDefense(self):
        self.defense = self.defenseCal()
        return self.defense

    def getConsume(self):
        return random.randint(5, 10)

    def display(self):
        return "id:%s character:%s life:%s tech:%s strength:%s attack:%s defense:%s" % (
            self.id, self.character, round(self.life, 8), round(self.tech,
                                                                8), self.strengthCal(), self.attackCal(), self.defenseCal())
