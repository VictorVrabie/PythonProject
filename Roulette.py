import random
# This is used to fixethe random generator so we can test the output
random.seed(3456)


def AboveMinimum (bet, minbet):
    output = []
    for item in bet:
        output.append(bool(item>minbet))
    print(output)


def SpinTheWheel (bets):
    winnumb=random.randint(0,36)
    output = []
    for item in bets:
        output.append(bool(item == winnumb))
    print(" Ball lands on " + str(winnumb))
    if sum(output) > 0:
        print(" There are " + str(sum(output)) + "correct bet(s)")
    else:
        print("No winners this round")


amounts1 = [10, 85, 120, 65, 150, 122]
bets1 = [10, 24, 36, 0, 11, 24]
class Roulette(object):
    def __init__(self,Roulette):
        self.Roulette = Roulette
    def Roulette(minbet):
        Roulette.Roulette= AboveMinimum(amounts1,minbet)

    def SimulateGame(bet,amount):
        Roulette.Roulette.SimulateGame = SpinTheWheel(bet)

table1 = Roulette.Roulette(100)
print(table1.SimulateGame(bets1,amounts1))