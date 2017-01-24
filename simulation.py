import random
# This is used to fixethe random generator so we can test the output

import Roulette
import Craps
#
# amounts1 = [10, 85, 120, 65, 150, 122]
# bets1 = [10, 24, 36, 0, 11, 24]
# table1 = Roulette.Roulette(100)
# print(table1.SimulateGame(bets1, amounts1))
# print(table1.SimulateGame(bets1, amounts1))
#
# amounts1 = [25, 85, 120, 65, 150, 122]
# bets1 = [10, 24, 36, 0, 11, 24]
# table1 = Craps.Craps(10)
# print(table1.SimulateGame(bets1, amounts1))
# print(table1.SimulateGame(bets1, amounts1))


# Simultaion
out = [0,0]
MinBet = [0, 25, 50]

for i in range(10000):
    players = random.randint(0,6)
    MinBetX = random.choice(MinBet)
    amount = random.sample(range(MinBetX,150),players)
    bet = random.sample(range(2,13),players)
    table1 = Craps.Craps(MinBetX)
    out = [i+j for i,j in zip(out,table1.SimulateGame(bet, amount))]
    print(out)
print(out[0]/out[1])
