import random
x = [20, 14 ,1]
print(random.choice(x))












# import random
#
# nbRoulette = 10
# nbCraps = 10
# nbBarmen = 4
# EmployeeWage = 200
# CasionStartCash = 50000
# nbCustomers = 100
# prcReturning = 50
# prcBachelor = 10
# BachelorFree = 200
#
#
# class Table(object):
#     def __init__(self, croupier, ID):
#         self.croupier = croupier
#         self.ID = ID
#         self.players =
#
#     def Profit(self):
#         return Flase
#
#
# class Roulette(Table):
#     def __init__(self,MinimumBet):
#         self.MinimumBet = MinimumBet
#
#     def Profit(self):
#         self.CasinoGain = 0
#         self.PlayerGains = []
#
#         def AboveMinimum(MinimumBet):
#             MinimumBet = random.randint([50, 100, 200])
#             output = []
#             for item in amount:
#                 output.append(bool(item >= MinimumBet))
#             return (output)
#
#         def SpinTheWheel(bet):
#             winnumb = random.randint(0, 36)
#             output = []
#             for item in bet:
#                 output.append(bool(item == winnumb))
#             print(" Spinning the wheel...")
#             print(" Ball lands on " + str(winnumb))
#             if sum(output) > 0:
#                 print(" There are " + str(sum(output)) + " correct bet(s)")
#             else:
#                 print("No winners this round")
#             return (output)
#
#         self.PlayerGains = [i * j * k * 30 for i, j, k in zip(amount, AboveMinimum(amount), SpinTheWheel(bet))]
#         self.CasinoGain = sum(amount) - sum(self.PlayerGains)
#         if self.CasinoGain > 0:
#             self.CasinoGain = self.CasinoGain * 0.95
#
#         return(self.CasinoGain)
