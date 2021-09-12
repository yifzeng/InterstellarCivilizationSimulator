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
            print(c.id + " has taken " + str(len(c.ownedSpace)))
        return False
    return True


def countAlive(univ):
    alivecivil = len(univ.civillist)
    for c in univ.civillist:
        if c.alive == False:
            alivecivil = alivecivil - 1
    return alivecivil


def civilExpand(civil, univ):
    civil.speed = 1 + len(civil.ownedSpace) // 20
    time = 0
    print(civil.id + ":  " + "civilExpand speed  " + str(civil.speed) + "  time:" + str(time))
    while len(civil.frontierSpace) > 0:
        print(civil.id + ":  " + "len(civil.frontierSpace) " + str(len(civil.frontierSpace)) + " time:" + str(time))

        random.shuffle(civil.frontierSpace)
        grid = random.choice(civil.frontierSpace)
        expandGrid = univ.getExpandableGrid(grid)
        print(civil.id + ":  " + "len(expandGrid) " + str(len(expandGrid)) + " time:" + str(time))
        if len(expandGrid) > 0:
            occupyGrid = random.choice(expandGrid)
            occupyGrid.owner = civil.id
            civil.occupyingSpace.append(occupyGrid)
            time = time + 1
            if time == civil.speed:
                break
        else:
            civil.frontierSpace.remove(grid)
            if len(civil.frontierSpace) == 0:
                civil.alive = False
                break


def occupyProcess(civil, univ):
    print(civil.id + ":  " + "len(civil.occupyingSpace) " + str(len(civil.occupyingSpace)))
    while len(civil.occupyingSpace) > 0:
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