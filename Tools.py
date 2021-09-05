import random
import string


def generateNumber(digit):
    seeds = string.digits
    random_str = random.sample(seeds, k=digit)
    return "".join(random_str)


def generateRandomNum(n):
    return random.choice(range(n))


def getExpandableGrid(x, y, maxX, maxY, univ):
    result = []
    xl = x - 1
    xr = x + 1
    yu = y - 1
    yd = y + 1

    if xl >= 0 and isExpandable(univ.getGrid(xl, y)):
        result.append(univ.getGrid(xl, y))
    if xr <= maxX and isExpandable(univ.getGrid(xr, y)):
        result.append(univ.getGrid(xr, y))
    if yu >= 0 and isExpandable(univ.getGrid(x, yu)):
        result.append(univ.getGrid(x, yu))
    if yd <= maxY and isExpandable(univ.getGrid(x, yd)):
        result.append(univ.getGrid(x, yd))

    if xl >= 0 and yu >= 0 and isExpandable(univ.getGrid(xl, yu)):
        result.append(univ.getGrid(xl, yu))
    if xr <= maxX and yu >= 0 and isExpandable(univ.getGrid(xr, yu)):
        result.append(univ.getGrid(xr, yu))
    if xl >= 0 and yd <= maxY and isExpandable(univ.getGrid(xl, yd)):
        result.append(univ.getGrid(xl, yd))
    if xr <= maxX and yd <= maxY and isExpandable(univ.getGrid(xr, yd)):
        result.append(univ.getGrid(xr, yd))


def isExpandable(grid):
    if grid.Blackhole() or grid.getOwner() is not None:
        return False