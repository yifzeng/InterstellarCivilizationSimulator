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

        self.init()

    def init(self):
        self.character = Character.getCharacter()
        self.id = self.character + Tools.generateSeq(6)
        self.frontierSpace[0].owner = self.id
        self.color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        if self.color == (200, 200, 200) or self.color == (255, 255, 255):
            self.color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        self.life = 10
        self.tech = 0.0001
        self.alive = True
        if self.character == "A":
            self.lifeConsume = 1
            self.blackholeTrans = 10
        elif self.character == "F":
            self.lifeConsume = 2
            self.defense = 100
        else:
            self.lifeConsume = 4
            self.attack = 200

        self.strength = self.strengthCal()

    def strengthCal(self):
        return round((self.life * self.tech), 6)

    def getStrength(self):
        self.strength = self.strengthCal()
        return self.strength

    def display(self):
        return "id:%s character:%s life:%s tech:%s strength:%s attack:%s defense:%s" % (
            self.life, self.character, self.life, self.tech, self.strength, self.attack, self.defense)
