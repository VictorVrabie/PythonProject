import random
# This is used to fixe the random generator so we can test the output
random.seed(3456)
class Craps:
    def __init__(self,min):
        self.min = min

    def SimulateGame(self, bet, amount):

        def AboveMinimum (amount):
            output = []
            for item in amount:
                output.append(bool(item >= self.min))
            return(output)

        def RollTheDice (bet):
            Dices = random.randint(1, 6) + random.randint(1,6)
            output = []
            for item in bet:
                output.append(bool(item == Dices))
            print(" Throwing the dices")
            print(" The winning sum is " + str(Dices))
            if sum(output) > 0:
                print(" There are " + str(sum(output)) + " winner(s)")
            else:
                print("No player won")
            return (output)

        Probs = list([i / 36 for i in range(1, 6)]) + [6 / 36] + list(reversed([i / 36 for i in range(1, 6)]))
        Coeff = [0.9 /i for i in Probs]

        a=AboveMinimum(amount)
        r=RollTheDice(bet)
        PlayerGain = [i * Coeff[k - 2] * j * l for i, k, j, l in zip(amount, bet, a, r)]
        CasinoGain = sum(amount)-sum(PlayerGain)
        PlayerGains = sum(PlayerGain)
        return [CasinoGain, PlayerGains]