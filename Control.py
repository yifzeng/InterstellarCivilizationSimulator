from Grid import Grid
import random


def control(univ):
    random.shuffle(univ.civillist)
    civils = univ.civillist
    for c in civils:
        if c.alive:
            for i in range(len(c.absorbList) + 1):
                civilExpand(c, univ)
                occupyProcess(c, univ)

    civilUnite(univ)

    if countAlive(univ) == 0:
        for c in civils:
            print(c.id + " has taken " + str(len(c.ownedSpace)))
            print(c.display())
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
        # random.shuffle(civil.frontierSpace)
        frontierGrid = random.choice(civil.frontierSpace)
        expandGrid = univ.getExpandableGrid(frontierGrid)
        if len(expandGrid) > 0:
            occupyGrid = random.choice(expandGrid)
            occupyGrid.owner = civil.id
            civil.occupyingSpace.append(occupyGrid)
            civil.frontierSpace.append(occupyGrid)
            othercivil = scoutOtherCivil(civil, occupyGrid, univ)
            if othercivil is None:
                break
            else:
                civilEncounter(civil, univ.civildict[othercivil], univ)

        else:
            civil.frontierSpace.remove(frontierGrid)
            if len(civil.frontierSpace) == 0 and len(civil.occupyingSpace) == 0:
                civil.alive = False
                break


def scoutOtherCivil(civil, grid, univ):
    result = univ.checkOwnerAround(grid)  # the method returns the ids of owner of the grid
    while civil.id in result:
        result.remove(civil.id)
    if len(result) == 0:
        return None
    else:
        random.shuffle(result)
        return result[0]


def occupyProcess(civil, univ):

    for grid in civil.occupyingSpace.copy():

        if grid.getResourceAmount() > 0:
            if grid.getResourceType() == "L":
                if grid.getResourceAmount() >= civil.tech:
                    civil.life = civil.life + civil.tech
                    grid.deductResourceAmount(civil.tech)
                else:
                    civil.life = civil.life + grid.getResourceAmount()
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


def civilEncounter(a, b, univ):

    if a.character == b.character and a.character == "F":
        if (a.id + b.id) not in univ.unitePair.keys() and (b.id + a.id) not in univ.unitePair.keys():
            univ.unitePair[a.id + b.id] = (a, b, (a.tech + b.tech), (a.tech / b.tech - a.tech // b.tech))

    elif a.character == b.character and a.character == "K" or (a.character == "F"
                                                               and b.character == "K") or (a.character == "K"
                                                                                           and b.character == "F"):
        if ((a, b) or (b, a)) not in univ.warPair:
            univ.warPair.append((a, b))
    elif a.character == "A":
        civilRunaway(a)


def civilUnite(univ):
    delete = []
    if univ.unitePair:
        for key, (a, b, totaltech, increment) in univ.unitePair.items():

            if (a.tech + b.tech) - totaltech >= increment:
                if (b.life > a.life):
                    a, b = b, a
                a.absorbList.append(b.id)
                b.alive = False
                a.absorb(b)
                print("Unite happen in round " + str(univ.round) + " ," + a.id + " absorb " + b.id)
                delete.append(key)
        for i in delete:
            del univ.unitePair[i]


def civilWar(univ):

    pass


def civilRunaway(a):

    pass


def cleanFrontierGrid(civil, univ):
    for frontierGrid in civil.frontierSpace.copy():
        expandGrid = univ.getExpandableGrid(frontierGrid)
        if len(expandGrid) == 0:
            civil.frontierSpace.remove(frontierGrid)