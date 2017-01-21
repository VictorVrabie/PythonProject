import random
# This is used to fixe the random generator so we can test the output
random.seed(3456)

class Roulette:
    def __init__(self, min):
        self.min = min

    def SimulateGame(self, bet, amount):

        def AboveMinimum (amount):
            output = []
            for item in amount:
                output.append(bool(item >= self.min))
            return(output)

        def SpinTheWheel (bet):
            winnumb=random.randint(0,36)
            output = []
            for item in bet:
                output.append(bool(item == winnumb))
            print(" Spinning the wheel...")
            print(" Ball lands on " + str(winnumb))
            if sum(output) > 0:
                print(" There are " + str(sum(output)) + " correct bet(s)")
            else:
                print("No winners this round")
            return (output)


        vec = []
        gain = 0
        a = AboveMinimum(amount)
        s = SpinTheWheel(bet)
        for item in range(len(amount)):
            if a[item]*s[item]== 0:
                vec.append(0)
                gain += amount[item]
            else:
                vec.append(amount[item]*30)
        return ([gain, vec])





