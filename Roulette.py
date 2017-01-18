import random
# This is used to fixethe random generator so we can test the output
random.seed(3456)


def AboveMinimum (bet, minbet):
    output = []
    for item in bet:
        output.append(bool(item>minbet))
    return(output)


def NumAboveMinimum (bet, minbet):
    output = []
    for item in bet:
        if item > minbet:
            output.append(item)
        else:
            output.append(0)
    return(output)


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
bets1 = [10, 24, 30, 0, 11, 24]

class Roulette(object):
    def Roulette(minbet):
        return AboveMinimum(amounts1,minbet)

    def SimulateGame(minbet,bet,amount):
        vec = []
        gain = 0
        winnumb = random.randint(0, 36)
        print(" Ball lands on " + str(winnumb))
        for item in amount:
            if item <= minbet:
                vec.append(0)
                gain += item
            elif bet[amounts1.index(item)] != winnumb:
                vec.append(0)
                gain += item
            else:
                vec.append(item * 30)

        return ([gain, vec])


table1 = Roulette.Roulette(100)
print(Roulette.SimulateGame(100,bets1,amounts1))





