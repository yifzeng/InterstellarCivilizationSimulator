from Grid import Grid
class Universe():
    def __init__(self, width, height):
        self.width = width
        self.height = height            
        self.bg_map = [[Grid(x,y) for x in range(0,self.width)] for y in range(0,self.height)]

    def getGrid(self,x,y):
        return self.bg_map[x][y]


# u = Universe(100,100)
# g = u.getGrid(1,4)
# print(g.__dict__)
# for i in u.bg_map:
#     for j in i:
#         print(j.__dict__)