from Resource import Resource
class Grid():
    def __init__(self, x, y):
        self.coordinate=(x,y)        
        self.resource = Resource()
        self.isBlackhole = False
        self.owner = None
        if self.resource.getType() == "B":
            self.isBlackhole = True

    def getCoordinate(self):
        return self.coordinate

    def getResourceType(self):
        return self.resource.getType()

    def getResourceAmount(self):
        return self.resource.getAmount()
    
    def Blackhole(self):
        return self.isBlackhole
    
    def getOwner(self):
        return self.owner



    

