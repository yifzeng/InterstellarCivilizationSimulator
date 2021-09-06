import random
import string


def generateNumber(digit):
    seeds = string.digits
    random_str = random.sample(seeds, k=digit)
    return "".join(random_str)


def generateRandomNum(n):
    return random.choice(range(n))
