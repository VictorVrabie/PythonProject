import random
# This is used to fixethe random generator so we can test the output
random.seed(3456)


def AboveMinimum (bet, minbet):
    output = []
    for item in bet:
        output.append(bool(item>bet))
    print(output)


def SpinTheWheel (bets):
    winnumb=random.randint(0,36)
    output = []
    for item in bets:
        output.append(bool(item == winnumb))
    print(" The winning number is " + str(winnumb))
    if sum(output) > 0:
        print(" The number of winners is " + str(sum(output)))
    else:
        print("There are no winners")

