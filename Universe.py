from Civilization import Civilizaiton
from Grid import Grid
import Tools


class Universe():
    def __init__(self, width, height, civilnum):
        self.width = width
        self.height = height
        self.bg_map = [[Grid(x, y) for x in range(0, self.width)] for y in range(0, self.height)]
        self.civillist = []
        self.civildict = {}

        self.initializeCivil(civilnum)

    def initializeCivil(self, civilnum):
        i = 0
        while i < civilnum:
            g = self.bg_map[Tools.generateRandomNum(self.width)][Tools.generateRandomNum(self.height)]
            if not g.Blackhole() and g.getOwner() is None:
                c = Civilizaiton(g.getCoordinate()[0], g.getCoordinate()[1])
                self.civillist.append(c)
                self.civildict[c.id] = c
                i = i + 1

    def getGrid(self, x, y):
        return self.bg_map[x][y]


# u = Universe(100, 100, 3)
# for c in u.civillist:
#     print(c.__dict__)
# print(u.civildict)