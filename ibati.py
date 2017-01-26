import random

class Customer:
        def drinks(self):
            if self.wealth > 60:
                self.drink = random.randint(1, 2) * 20
                self.tips = random.randint(0, 20)
                self.wealth -= self.drink + self.tips
                return True
            else:
                self.drink = 0
                self.tips = 0
                return False

        def playat(self, tbnum, rounds):
            self.tblplay = [random.randint(1,tbnum) for i in range(rounds)]



class Returning(Customer):
    def rich(self):
        self.wealth = random.randint(100, 300)
        self.bet = 0
        return False


class OneTime(Customer):
    def rich(self):
        self.wealth = random.randint(200, 300)
        self.bet = random.randint(0, (self.wealth / 3))
        return False


class Bachelor(Customer):
    def rich(self):
        self.wealth = random.randint(200, 500) + 0
        self.bet = random.randint(0, self.wealth)
        return False

customers = []
for i in range(1,20):
    customers.append(Returning())
print(customers)

#
# class Table(object):
#     def __init__(self, customers):
#         self.customers = customers
#
#
# class Roulette(Table):
#
#     def minimumbet(self):
#         self.minimumbet = random.randint([0, 50, 100])
#
#     def simulategame(self, bets, amount):
#
#         def abovemin(amount):
#             above = []
#             for item in self.customers:
#                 above.append(bool(self.customers.bet[item] >= self.minimumbet))
#             return above
#
#         def spinthewheel(bets):
#             occ = random.randint(0, 36)
#             print('Spinning the wheel...')
#             print('The Ball lands on...', occ)
#             correcte = []
#             for item in bets:
#                 correcte.append(bool(item == occ))
#             if correcte.count(True) == 0:
#                 print("No winners this round")
#             else:
#                 print("There are", sum(correcte), "correct bets")
#             return correcte
#
#         y = abovemin(amount)
#         z = spinthewheel(bets)
#         playergains = [i*j*k for i, j, k in zip(amount, y, z)]
#         casinogain = sum(amount) - sum(playergains)
#         return [casinogain, [i*30 for i in playergains]]