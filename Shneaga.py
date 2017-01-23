import random
import Roulette
import Craps
#
# amounts1 = [10, 85, 120, 65, 150, 122]
# bets1 = [10, 24, 36, 0, 11, 24]
# table1 = Roulette.Roulette(100)
# print(table1.SimulateGame(bets1, amounts1))
# print(table1.SimulateGame(bets1, amounts1))


out = [0,0]
MinBet = [0, 25, 50]

for i in range(10000):
    players = random.randint(0,6)
    MinBetX = random.choice(MinBet)
    amount = random.sample(range(MinBetX,100),players)
    bet = random.sample(range(2,13),players)
    table1 = Craps.Craps(MinBetX)
    out = [i+j for i,j in zip(out,table1.SimulateGame(bet, amount))]
    print(out)
print(out[0]/(out[0]+out[1]))


# Times = list([i for i in range(1,6)]) + [6] + list(reversed([i for i in range(1,6)]))
# Probs = list([i/36 for i in range(1,6)]) + [6/36] + list(reversed([i/36 for i in range(1,6)]))
# Coeff = [0.9/i for i in Probs]








#
# # Coeff = [42.65, 35.54, 28.43, 21.32, 14.21, 7.11, 14.21, 21.23, 28.43, 35.54, 42.65]
# altCoeff = [30.490974729241877, 14.216216216216218, 8.804321728691477, 6.100810081008101, 4.484149855907781,
#             3.4021608643457384, 4.484149855907781, 6.100810081008101, 8.804321728691477, 14.216216216216218,
#             30.490974729241877]

