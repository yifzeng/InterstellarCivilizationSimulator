from Grid import Grid
import random
import copy
import logging

logging.basicConfig(
    level=logging.DEBUG,  #控制台打印的日志级别
    filename='new.log',
    filemode='w',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
    #a是追加模式，默认如果不写的话，就是追加模式
    #format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    #日志格式
    format='%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s')


def control(univ):
    random.shuffle(univ.civillist)
    civils = univ.civillist
    for c in civils:
        if c.alive:
            for i in range(len(c.absorbList) + 1):
                civilExpand(c, univ)
                occupyProcess(c, univ)

    civilUnite(univ)
    civilWar(univ)

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

        frontierGrid = random.choice(civil.frontierSpace)
        expandGrid = univ.getExpandableGrid(frontierGrid)
        if len(expandGrid) > 0 and civil.alive:
            occupyGrid = random.choice(expandGrid)
            occupyGrid.owner = civil.id
            civil.occupyingSpace.append(occupyGrid)
            civil.frontierSpace.append(occupyGrid)
            othercivil = scoutOtherCivil(civil, occupyGrid, univ)
            if othercivil is None:
                break
            else:
                for oc in othercivil:
                    civilEncounter(civil, univ.civildict[oc], univ)
                break
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
        return result


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

    if {a.character, b.character}.issubset(["F"]):
        if (a.id + b.id) not in univ.unitePair.keys() and (b.id + a.id) not in univ.unitePair.keys():
            univ.unitePair[a.id + b.id] = (a, b, (a.tech + b.tech), (a.tech / b.tech - a.tech // b.tech))

    elif {a.character, b.character}.issubset(["F", "K"]):
        if (a.id + b.id) not in univ.warPair.keys() and (b.id + a.id) not in univ.warPair.keys():
            univ.warPair[a.id + b.id] = ((a, a.life), (b, b.life))
            logging.info("add warPair: " + a.id + "" + b.id)

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
                a.absorb(b)
                logging.info("Unite happen in round " + str(univ.round) + " ," + a.id + " absorb " + b.id)
                print("Unite happen in round " + str(univ.round) + " ," + a.id + " absorb " + b.id)
                delete.append(key)
        for i in delete:
            del univ.unitePair[i]


def civilWar(univ):
    delete = []
    if univ.warPair:
        for key, tmp in univ.warPair.items():
            l = [tmp[0], tmp[1]]
            random.shuffle(l)
            (a, alife) = l[0]
            (b, blife) = l[1]
            if {a.character, b.character}.issubset(["K"]):
                a.life = a.life - b.life * b.tech / 10
                b.life = b.life - a.life * a.tech / 10
                if a.life <= 0 or b.life <= 0:
                    if a.life <= 0:
                        winner = b
                        loser = a
                    elif b.life <= 0:
                        winner = a
                        loser = b
                    loser.alive = False
                    loser.life = alife
                    winner.absorbList.append(loser.id)
                    winner.absorb(loser)
                    logging.info(key + " War end in round " + str(univ.round) + " ," + winner.id + " absorb " + loser.id)
                    print(key + " War end in round " + str(univ.round) + " ," + winner.id + " absorb " + loser.id)
                    delete.append(key)
            elif {a.character, b.character}.issubset(["F", "K"]):
                if a.character == "F":
                    fc, kc = a, b
                else:
                    fc, kc = b, a

                fclife, kclife = fc.life, kc.life

                logging.info(fc.id + "  before  life:" + str(fc.life))
                fc.life = fc.life - kc.life * kc.tech / 10
                logging.info(fc.id + "  after   life:                                " + str(fc.life))

                logging.info(kc.id + "  before  life:" + str(kc.life))
                kc.life = kc.life - kc.life * kc.tech / 20
                logging.info(kc.id + "  after   life:                                " + str(kc.life))

                if fc.life <= 0 or kc.life <= 0:
                    if fc.life <= 0:
                        winner, loser = kc, fc
                        loserlife = fclife
                    elif kc.life <= 0:
                        winner, loser = fc, kc
                        loserlife = kclife

                    loser.alive = False
                    loser.life = loserlife / 2
                    winner.absorbList.append(loser.id)
                    winner.absorb(loser)
                    logging.info(key + " War end in round " + str(univ.round) + " ," + winner.id + " absorb " + loser.id)
                    print(key + " War end in round " + str(univ.round) + " ," + winner.id + " absorb " + loser.id)
                    delete.append(key)

        for i in delete:
            logging.info("delete id :" + i)
            del univ.warPair[i]


def civilRunaway(a):

    return ""


def cleanFrontierGrid(civil, univ):
    for frontierGrid in civil.frontierSpace.copy():
        expandGrid = univ.getExpandableGrid(frontierGrid)
        if len(expandGrid) == 0:
            civil.frontierSpace.remove(frontierGrid)