from Civilization import Civilizaiton
from Grid import Grid
import Tools


class Universe():
    def __init__(self, width, height, civilnum):
        self.width = width
        self.height = height
        self.civilnum = civilnum
        self.bg_map = [[Grid(x, y) for x in range(0, self.width)] for y in range(0, self.height)]
        self.civillist = []
        self.civildict = {}

        self.initializeCivil(civilnum)

    def initializeCivil(self, civilnum):
        i = 0
        while i < civilnum:
            g = self.bg_map[Tools.generateRandomNum(self.width)][Tools.generateRandomNum(self.height)]
            if not g.Blackhole() and g.getOwner() is None:
                c = Civilizaiton(g)
                self.civillist.append(c)
                self.civildict[c.id] = c
                i = i + 1

    def getGrid(self, x, y):
        return self.bg_map[x][y]

    def getExpandableGrid(self, grid):
        result = []
        x = grid.getX()
        y = grid.getY()
        xl = x - 1
        xr = x + 1
        yu = y - 1
        yd = y + 1

        if xl >= 0 and self.isExpandable(self.getGrid(xl, y)):
            result.append(self.getGrid(xl, y))
        if xr <= self.width and self.isExpandable(self.getGrid(xr, y)):
            result.append(self.getGrid(xr, y))
        if yu >= 0 and self.isExpandable(self.getGrid(x, yu)):
            result.append(self.getGrid(x, yu))
        if yd <= self.height and self.isExpandable(self.getGrid(x, yd)):
            result.append(self.getGrid(x, yd))

        if xl >= 0 and yu >= 0 and self.isExpandable(self.getGrid(xl, yu)):
            result.append(self.getGrid(xl, yu))
        if xr <= self.width and yu >= 0 and self.isExpandable(self.getGrid(xr, yu)):
            result.append(self.getGrid(xr, yu))
        if xl >= 0 and yd <= self.height and self.isExpandable(self.getGrid(xl, yd)):
            result.append(self.getGrid(xl, yd))
        if xr <= self.width and yd <= self.height and self.Expandable(self.getGrid(xr, yd)):
            result.append(self.getGrid(xr, yd))

        return result

    def isExpandable(grid):
        if grid.Blackhole() or grid.getOwner() is not None:
            return False
        else:
            return True


# u = Universe(100, 100, 3)
# for c in u.civillist:
#     print(c.__dict__)
# print(u.civildict)