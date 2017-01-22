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

        PlayerGains = [i * j * k * 30 for i, j, k in zip(amount, AboveMinimum(amount), SpinTheWheel(bet))]
        CasinoGain = sum(amount) - sum(PlayerGains)
        return [CasinoGain, [i for i in PlayerGains]]





