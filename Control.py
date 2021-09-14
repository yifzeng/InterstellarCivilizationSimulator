from Grid import Grid
import random


def control(univ):
    random.shuffle(univ.civillist)
    civils = univ.civillist
    for c in civils:
        civilExpand(c, univ)
        occupyProcess(c, univ)

    if countAlive(univ) == 0:
        for c in civils:
            c.display()
        return False
    return True


def showAllOwnedGrid(civil):
    allGrid = []
    for i in civil.ownedSpace:
        allGrid.append(i.getCoordinate())
    allGrid.sort()
    print(allGrid)


def countAlive(univ):
    alivecivil = len(univ.civillist)
    for c in univ.civillist:
        if c.alive == False:
            alivecivil = alivecivil - 1
    return alivecivil


def civilExpand(civil, univ):

    while len(civil.frontierSpace) > 0:
        random.shuffle(civil.frontierSpace)
        frontierGrid = random.choice(civil.frontierSpace)
        expandGrid = univ.getExpandableGrid(frontierGrid)
        if len(expandGrid) > 0:
            occupyGrid = random.choice(expandGrid)
            occupyGrid.owner = civil.id
            civil.occupyingSpace.append(occupyGrid)
            civil.frontierSpace.append(occupyGrid)
            break
        else:
            civil.frontierSpace.remove(frontierGrid)
            if len(civil.frontierSpace) == 0 and len(civil.occupyingSpace) == 0:
                civil.alive = False
                break


def occupyProcess(civil, univ):

    for grid in civil.occupyingSpace.copy():

        if grid.getResourceAmount() > 0:
            if grid.getResourceType() == "L":
                if grid.getResourceAmount() >= civil.getStrength():
                    civil.life = civil.life + civil.getStrength()
                    grid.deductResourceAmount(civil.getStrength())
                else:
                    civil.life = civil.life + civil.getStrength() - grid.getResourceAmount()
                    grid.deductResourceAmount(grid.getResourceAmount())
            elif grid.getResourceType() == "S":
                civil.tech = civil.tech + grid.getResourceAmount()
                grid.deductResourceAmount(grid.getResourceAmount())
        if grid.getResourceAmount() <= 0:
            civil.occupyingSpace.remove(grid)
            civil.ownedSpace.append(grid)
        if len(civil.frontierSpace) == 0 and len(civil.occupyingSpace) == 0:
            civil.alive = False

            break


def civilEncounter(a, b):

    pass


def war(a, b):

    pass


def cleanFrontierGrid(civil, univ):
    for frontierGrid in civil.frontierSpace.copy():
        expandGrid = univ.getExpandableGrid(frontierGrid)
        if len(expandGrid) == 0:
            civil.frontierSpace.remove(frontierGrid)