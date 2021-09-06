from Grid import Grid
import random


def control(univ):
    civils = univ.civillist
    for c in civils:
        civilExpand(c, univ)
        occupyProcess(c, univ)


def civilExpand(civil, univ):
    civil.frontierSpace = random.shuffle(civil.frontierSpace)
    while True:
        grid = random.choice(civil.frontierSpace)
        expandGrid = univ.getExpandableGrid(grid)
        if len(expandGrid) > 0:
            occupyGrid = random.choice(expandGrid)
            occupyGrid.owner = civil.id
            civil.occupyingSpace.append(occupyGrid)
            break
        else:
            civil.frontierSpace.remove(grid)
            if len(civil.frontierSpace) == 0:
                break


def occupyProcess(civil, univ):
    speed = 1 + len(civil.ownedSpace) // 5  # occupation speed depends on the owned space amount
    for i in range(speed):
        grid = random.choice(civil.occupyingSpace)
        civil.ownedSpace.append(grid)
        civil.frontierSpace.append(grid)
        civil.occupyingSpace.remove(grid)

        if grid.getResourceType() == "L":
            civil.life = civil.life + grid.getResourceAmount()
        elif grid.getResourceType() == "S":
            civil.tech = civil.tech + grid.getResourceAmount()


def civilEncounter(a, b):

    pass