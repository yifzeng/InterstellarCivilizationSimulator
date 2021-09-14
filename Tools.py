import random
import string

SEQ = 0


def generateSeq(digit):
    global SEQ
    SEQ = SEQ + 1
    return ("%0" + str(digit) + "d") % SEQ


def generateNumber(digit):
    seeds = string.digits
    random_str = random.sample(seeds, k=digit)
    return "".join(random_str)


def generateRandomNum(n):
    return random.choice(range(n))
