from Grid import Grid
import random


def control(univ):

    pass


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


def civilEncounter(a, b):

    pass