import random

class Customer:
    def __init__(self, typeC):
        self.typec = typeC

    def drinks(self):
        if self.wealth > 60:
            self.drink = random.randint(1,2)*20
            self.tips = random.randint(0,20)
            self.wealth -= self.drink+self.tips
            return True
        else :
            self.drink = 0
            self.tips = 0
            return False

class Returning(Customer):
    def rich(self):
        self.wealth = random.randint(100,300)
        self.bet = Table.min
        return False

class OneTime(Customer):
    def rich(self):
        self.wealth = random.randint(200,300)
        self.bet = random.randint(0,(self.wealth/3))
        return False

class Bachelor(Customer):
    def rich(self):
        self.wealth = random.randint(200,500) + 0
        self.bet = random.randint(0,self.wealth)
        return False

class Employee :
    def __init__(self,wage):
        self.wage=wage

class Croupier(Employee):
    def CasinoGains(self):
        if Table.CasinoGain > 0:
        self.profitgain += 0.05*Table.CasinoGain

class Barmen(Employee):
    def Tips(self):
        self.tips += Customer.tips

class Table:
    def __init__(self, min):
        self.min = min

    def SimulateGame(self,typetable, bet, amount):

        def AboveMinimum (amount):
            output = []
            for item in amount:
                output.append(bool(item >= self.min))
            return(output)

        self.CasinoGain=0
        self.PlayerGains = []

        if typetable == "roulette":
            def SpinTheWheel(bet):
                winnumb = random.randint(0, 36)
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
            self.PlayerGains = [i * j * k * 30 for i, j, k in zip(amount, AboveMinimum(amount), SpinTheWheel(bet))]
            self.CasinoGain = sum(amount) - sum(self.PlayerGains)
            if self.CasinoGain > 0:
                self.CasinoGain = self.CasinoGain*0.95

        elif typetable == "craps":
            def RollTheDice(bet):
                Dices = random.randint(1, 6) + random.randint(1, 6)
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
            Coeff = [0.9 / i for i in Probs]

            a = AboveMinimum(amount)
            r = RollTheDice(bet)
            self.PlayerGains = [i * j * l * Coeff[k - 2] for i, j, l, k in zip(amount, a, r, bet)]
            self.CasinoGain = sum(amount) - sum(self.PlayerGains)
            if self.CasinoGain > 0:
                self.CasinoGain = self.CasinoGain*0.95

        return [self.CasinoGain, self.PlayerGains]







# class Customer(object):
#     def __init__(self, typeC):
#         self.typeC = typeC
#         if self.typeC == "Returning":
#             self.bet = 10
#             self.budget = random.randint(100, 300)
#         elif self.typeC == "New":
#             self.budget = random.randint(200, 300)
#             self.bet = random.randint(0, int((self.budget) / 3))
#         else:
#             self.budget = random.randint(200, 500)
#             self.bet = random.randint(0, int(self.budget))
#
#
# def CustomerTypes(total, returning, bachelor):
#         ret = int(total * (returning / 100))
#         bch = int(total * (bachelor / 100))
#         new = total - (ret + bch)
#         types = []
#         types.extend(["Returning" for i in range(ret)])
#         types.extend(["New" for i in range(new)])
#         types.extend(["Bachelor" for i in range(bch)])
#         return (list(zip(range(total), [Customer(types[i][1]).budget for i in range(total)],
#                          [Customer(types[i][1]).bet for i in range(total)])))
