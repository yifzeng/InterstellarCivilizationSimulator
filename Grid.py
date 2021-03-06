from Resource import Resource


class Grid():
    def __init__(self, row, col):
        self.coordinate = (row, col)
        self.resource = Resource()
        self.isBlackhole = False
        self.owner = None

        if self.resource.getType() == "B":
            self.isBlackhole = True

    def deductResourceAmount(self, amount):
        self.resource.deductAmount(amount)

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

    def getX(self):
        return self.getCoordinate()[0]

    def getY(self):
        return self.getCoordinate()[1]
