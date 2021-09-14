import random


class Resource():
    def __init__(self):
        self.types = ["S", "L", "N", "B"]  # S: Science, L: Life support, N: Nothing, B: Blackhole
        self.type = None
        self.amount = 0

        def randomSet(self):
            r = random.randint(1, 1000)
            if r < 100:
                self.type = "S"  # S: Science
                self.amount = r / 10000
            elif 100 < r <= 500:
                self.type = "L"  # L: Life support
                self.amount = r / 100
            elif r == 999:
                self.type = "B"
                self.amount = 0
            else:
                self.type = "N"  # N: Nothing
                self.amount = 0

        randomSet(self)

    def getType(self):
        return self.type

    def getAmount(self):
        return self.amount

    def deductAmount(self, amount):
        self.amount = self.amount - amount
