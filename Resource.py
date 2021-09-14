import random


class Resource():
    def __init__(self):
        self.types = ["S", "L", "N", "B"]  # S: Science, L: Life support, N: Nothing, B: Blackhole
        self.type = None
        self.amount = 0.00

        def randomSet(self):
            r = random.randint(1, 1000)
            if r < 100:
                self.type = "S"  # S: Science
                self.amount = round(r / 10000, 8)
            elif 100 < r <= 500:
                self.type = "L"  # L: Life support
                self.amount = round(r / 100, 8)
            elif r == 999:
                self.type = "B"
                self.amount = 0.00
            else:
                self.type = "N"  # N: Nothing
                self.amount = 0.00

        randomSet(self)

    def getType(self):
        return self.type

    def getAmount(self):
        return self.amount

    def deductAmount(self, amount):
        if self.amount < amount:
            self.amount = 0
        else:
            self.amount = round(self.amount, 8) - round(amount, 8)
