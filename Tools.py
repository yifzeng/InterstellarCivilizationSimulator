import random
import string


def generateNumber(digit):
    seeds = string.digits
    random_str = random.sample(seeds, k=digit)
    return "".join(random_str)


def generateRandomNum(n):
    return random.choice(range(n))


# cols = 3
# rows = 5
# l = [[(row, col) for col in range(0, cols)] for row in range(0, rows)]
# print(l)
# print(l[3][1])
