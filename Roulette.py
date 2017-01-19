import random
# This is used to fixe the random generator so we can test the output
random.seed(3456)


def AboveMinimum (bet, minbet):
    output = []
    for item in bet:
        output.append(bool(item>= minbet))
    return(output)

def SpinTheWheel (bets):
    winnumb=random.randint(0,36)
    output = []
    for item in bets:
        output.append(bool(item == winnumb))
    print(" Spinning the wheel...")
    print(" Ball lands on " + str(winnumb))
    if sum(output) > 0:
        print(" There are " + str(sum(output)) + " correct bet(s)")
    else:
        print("No winners this round")
    return (output)

class Roulette(object):

    def SimulateGame(minbet,bet,amount):
        vec = []
        gain = 0
        a = AboveMinimum(amount, 100)
        s = SpinTheWheel(bet)
        for item in range(len(amount)):
            if a[item]*s[item]==0:
                vec.append(0)
                gain += amount[item]
            else:
                vec.append(amount[item]*30)
        return ([gain, vec])


amounts1 = [10, 85, 120, 65, 150, 122]
bets1 = [10, 24, 36, 0, 11, 24]
print(Roulette.SimulateGame(100,bets1,amounts1))
print(Roulette.SimulateGame(100,bets1,amounts1))




