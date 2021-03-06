from Civilization import Civilizaiton
from Grid import Grid
import Tools


class Universe():
    def __init__(self, rows, cols, civilnum):
        self.rows = rows
        self.cols = cols
        self.civilnum = civilnum
        # self.bg_map = [[Grid(row, col) for col in range(0, self.cols)] for row in range(0, self.rows)]
        (mapR, blackholeR, resourceL, resourceS) = self.creatMap(rows, cols)
        self.bg_map = mapR
        self.blackhole_map = blackholeR
        self.resourceL_map = resourceL
        self.resourceS_map = resourceS
        self.civillist = []
        self.civildict = {}
        self.unitePair = {}
        self.warPair = {}
        self.round = 0
        self.initializeCivil(civilnum)

        # print("Life resources")
        # for i in self.resourceL_map:
        #     print(i.getResourceAmount(), end=", ")

        # print("Science resources")
        # for j in self.resourceS_map:
        #     print(j.getResourceAmount(), end=", ")

    def creatMap(self, rows, cols):
        mapResult = []
        blackholeResult = []
        resourceLResult = []
        resourceSResult = []

        for row in range(0, rows):
            mapResult.append([])
            for col in range(0, cols):
                grid = Grid(row, col)
                if grid.getResourceType() == "L":
                    resourceLResult.append(grid)
                if grid.getResourceType() == "S":
                    resourceSResult.append(grid)
                if grid.Blackhole():
                    blackholeResult.append(grid)
                mapResult[row].append(grid)
        return mapResult, blackholeResult, resourceLResult, resourceSResult

    def initializeCivil(self, civilnum):
        i = 0
        while i < civilnum:
            randomRow = Tools.generateRandomNum(self.rows)
            randomCol = Tools.generateRandomNum(self.cols)
            g = self.bg_map[randomRow][randomCol]
            if not g.Blackhole() and g.getOwner() is None:
                c = Civilizaiton(g)
                self.civillist.append(c)
                self.civildict[c.id] = c
                i = i + 1

    def getGrid(self, row, col):
        return self.bg_map[row][col]

    def getExpandableGrid(self, grid):
        result = []
        (row, col) = grid.getCoordinate()
        coll = col - 1
        colr = col + 1
        rowu = row - 1
        rowd = row + 1
        if coll >= 0 and self.isExpandable(self.getGrid(row, coll)):
            result.append(self.getGrid(row, coll))
        if colr < self.cols and self.isExpandable(self.getGrid(row, colr)):
            result.append(self.getGrid(row, colr))
        if rowu >= 0 and self.isExpandable(self.getGrid(rowu, col)):
            result.append(self.getGrid(rowu, col))
        if rowd < self.rows and self.isExpandable(self.getGrid(rowd, col)):
            result.append(self.getGrid(rowd, col))

        if coll >= 0 and rowu >= 0 and self.isExpandable(self.getGrid(rowu, coll)):
            result.append(self.getGrid(rowu, coll))
        if colr < self.cols and rowu >= 0 and self.isExpandable(self.getGrid(rowu, colr)):
            result.append(self.getGrid(rowu, colr))
        if coll >= 0 and rowd < self.rows and self.isExpandable(self.getGrid(rowd, coll)):
            result.append(self.getGrid(rowd, coll))
        if colr < self.cols and rowd < self.rows and self.isExpandable(self.getGrid(rowd, colr)):
            result.append(self.getGrid(rowd, colr))

        return result

    def isExpandable(self, grid):
        if grid.Blackhole() or grid.getOwner() is not None:
            return False
        else:
            return True

    def checkOwnerAround(self, grid):
        result = []
        (row, col) = grid.getCoordinate()
        coll = col - 1
        colr = col + 1
        rowu = row - 1
        rowd = row + 1
        if coll >= 0 and self.isOccupied(self.getGrid(row, coll)):
            result.append(self.getGrid(row, coll).owner)
        if colr < self.cols and self.isOccupied(self.getGrid(row, colr)):
            result.append(self.getGrid(row, colr).owner)
        if rowu >= 0 and self.isOccupied(self.getGrid(rowu, col)):
            result.append(self.getGrid(rowu, col).owner)
        if rowd < self.rows and self.isOccupied(self.getGrid(rowd, col)):
            result.append(self.getGrid(rowd, col).owner)

        if coll >= 0 and rowu >= 0 and self.isOccupied(self.getGrid(rowu, coll)):
            result.append(self.getGrid(rowu, coll).owner)
        if colr < self.cols and rowu >= 0 and self.isOccupied(self.getGrid(rowu, colr)):
            result.append(self.getGrid(rowu, colr).owner)
        if coll >= 0 and rowd < self.rows and self.isOccupied(self.getGrid(rowd, coll)):
            result.append(self.getGrid(rowd, coll).owner)
        if colr < self.cols and rowd < self.rows and self.isOccupied(self.getGrid(rowd, colr)):
            result.append(self.getGrid(rowd, colr).owner)

        return result

    def isOccupied(self, grid):
        if grid.getOwner() is not None:
            return True
        else:
            return False


# u = Universe(100, 100, 3)
# for c in u.civillist:
#     print(c.__dict__)
