import random
# This is used to fixethe random generator so we can test the output
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
            Dices = random.randint(2, 12)
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

        Coeff = [42.65, 35.54, 28.43, 21.32, 14.21, 7.11, 14.21, 21.23, 28.43, 35.54, 42.65]
        #altCoeff = [66.59205776173285, 32.23423423423423, 20.80912364945978, 15.1017101710171, 11.688760806916425, 9.40456182472989, 11.688760806916425, 15.1017101710171, 20.80912364945978, 32.23423423423423, 66.59205776173285]
        PlayerGains = [i * Coeff[k-2] *j * l for i, j, k, l in zip(amount,bet, AboveMinimum(amount), RollTheDice(bet))]
        CasinoGain = sum(amount) - sum(PlayerGains)
        return [CasinoGain, [i  for i in PlayerGains]]



# import random
# random.seed(3456)
# thousandsthrows = []
# for i in range(1000):
#     thousandsthrows.append(int(random.randint(1, 6)) + int(random.randint(1, 6)))
#
# from collections import Counter
# import numpy as np
# from matplotlib import pyplot as plt
#
# labels, values = zip(*Counter(thousandsthrows).items())
# indexes = np.arange(len(labels))
# width = 1
# plt.bar(indexes, values, width)
# plt.xticks(indexes + width * 0.5, labels)
# plt.show()



