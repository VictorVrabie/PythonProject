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
bets1 = [10, 24, 36, 0, 11, 24]

class Roulette(object):
    def Roulette(minbet):
        return AboveMinimum(amounts1,minbet)

    def Win(minbet):
        vec=[]
        gain = 0
        for item in amounts1:
            if item>minbet:
                vec.append(item)
                gain += 0
            else:
                gain += item
                vec.append(0)
        return ([gain,vec])
print(Roulette.Win(100))






def min(minbet):
    output = []
    for item in amounts1:
        if item > minbet:
            output.append(bets1[amounts1.index(item)])
    return(SpinTheWheel(output))
    return([sum(),])
print(min(50))




