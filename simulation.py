import random
# This is used to fixethe random generator so we can test the output
random.seed(3456)

import Roulette
import Craps

amounts1 = [10, 85, 120, 65, 150, 122]
bets1 = [10, 24, 36, 0, 11, 24]
table1 = Roulette.Roulette(100)
print(table1.SimulateGame(bets1, amounts1))
print(table1.SimulateGame(bets1, amounts1))

amounts1 = [10, 85, 120, 65, 150, 122]
bets1 = [8, 24, 36, 0, 11, 24]
table1 = Craps.Craps(10)
print(table1.SimulateGame(bets1, amounts1))
print(table1.SimulateGame(bets1, amounts1))
