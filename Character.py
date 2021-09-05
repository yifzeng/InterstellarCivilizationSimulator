import random
class Character():

    def __init__(self):
        self.characters = ["A","F","K"] # A: Leave Me Alone, F: Make Friends, K: Kill Them All
        self.character = random.choice(self.characters)        
    
    def getCharacter(self):
        return self.character

print(Character().getCharacter())
