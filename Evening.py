import random
# random.seed(2)

nbRoulette = 10
nbCraps = 10
nbBarmen = 4
EmployeeWage = 200
CasionStartCash = 50000
nbCustomers = 100
prcReturning = 50
prcBachelor = 10
BachelorFree = 200

tables = []
for i in range(nbRoulette):
    tables.append([i+1 ,"roulette", random.choice([50, 100, 200])])
for i in range(nbCraps):
    tables.append([i+nbRoulette+1, "craps",random.choice([0,25,50])])


class Customer(object):
    def __init__(self, typeC, ID):
        self.typeC = typeC
        self.ID = ID
        self.table = random.choice(tables)
        if self.typeC == "Returning":
            self.bet =self.table[2]
            self.budget = random.randint(100, 300)
        elif self.typeC == "New":
            self.budget = random.randint(200, 300)
            self.bet = random.randint(0, int((self.budget) / 3))
        else:
            self.budget = random.randint(200, 500) + BachelorFree
            self.bet = random.randint(0, int(self.budget))
        self.table = random.choice(tables)

def CustomerTypes(total, returning, bachelor):
        customers=[]
        ret = int(total * (returning / 100))
        bch = int(total * (bachelor / 100))
        new = total - (ret + bch)
        for i in range(ret):
            customers.append(Customer('Returning', i))
        for i in range(new):
            customers.append(Customer('New', i + ret))
        for i in range(bch):
            customers.append(Customer('Bachelor', i + new + ret))
        for i in range(100 - bch, total):
            customers[i].budget += BachelorFree
        return customers

Customers = CustomerTypes(nbCustomers, prcReturning, prcBachelor)


listoftables = []
for i in range(1,len(tables)+1):
    tableplayers = []
    for j in range(nbCustomers):
        if Customers[j].table[0] == i:
            tableplayers.append(Customers[j])
    listoftables.append(tableplayers)

class Table(object):
    def __init__(self, number):
        self.number = number
        self.players = listoftables[number-1]
        self.amounts = []
        for i in range(len(self.players)):
            self.amounts.append(self.players[i].bet)


    def SimulateGame(self):

        if tables[self.number-1][1] == "roulette":
            MinimumBet = tables[self.number-1][2]
            amounts = self.amounts
            bets = [random.randint(0,36) for i in amounts]

            def AboveMinimum(amounts):
                output = []
                for item in amounts:
                    output.append(bool(item >= MinimumBet))
                return output

            def SpinTheWheel(bets):
                winnumb = random.randint(0, 36)
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

            PlayerGains = [i * j * k * 30 for i, j, k in zip(amounts, AboveMinimum(amounts), SpinTheWheel(bets))]
            CasinoGain = sum(amounts) - sum(PlayerGains)
            if CasinoGain > 0:
                CasinoGain = CasinoGain * 0.95
            return [CasinoGain, PlayerGains,bets,amounts]


        elif tables[self.number-1][1] == "craps":
            MinimumBet = tables[self.number-1][2]
            amounts = self.amounts
            bets = [random.randint(2,12) for i in amounts ]

            def AboveMinimum(amounts):
                output = []
                for item in amounts:
                    output.append(bool(item >= MinimumBet))
                return output

            def RollTheDice(bets):
                dice = random.randint(1, 6) + random.randint(1, 6)
                output = []
                for item in bets:
                    output.append(bool(item == dice))
                print(" Throwing the dice")
                print(" The sum of the upper faces  ", dice)
                if sum(output) > 0:
                    print(" There are ", sum(output), " winner(s)")
                else:
                    print("No player won")
                return output

            a = AboveMinimum(amounts)
            r = RollTheDice(bets)

            Probs = list([i / 36 for i in range(1, 6)]) + [6 / 36] + list(reversed([i / 36 for i in range(1, 6)]))
            Coeff = [0.9 / i for i in Probs]

            qualify = [i * j for i, j in zip(a, r)]
            PlayerGains = [i * Coeff[k-2] * j for i, k, j in zip(amounts, bets, qualify)]
            CasinoGain = sum(amounts) - sum(PlayerGains)
            return [CasinoGain, PlayerGains]

print(Table.SimulateGame(Table(11)))



# class Customer:
#     def __init__(self, typeC):
#         self.typec = typeC
#
#     def Drinks(self):
#         if self.wealth > 60:
#             self.drink = random.randint(1,2)*20
#             self.tips = random.randint(0,20)
#             self.wealth -= self.drink+self.tips
#             return True
#         else :
#             self.drink = 0
#             self.tips = 0
#             return False
#
#     def TableChoice(self):
#         self.tablechoice = random.randint(0,(nbRoulette+nbCraps))
#
# class Returning(Customer):
#     def rich(self):
#         self.wealth = random.randint(100,300)
#         self.bet = Table.min
#         return False
#
# class OneTime(Customer):
#     def rich(self):
#         self.wealth = random.randint(200,300)
#         self.bet = random.randint(0,(self.wealth/3))
#         return False
#
# class Bachelor(Customer):
#     def rich(self):
#         self.wealth = random.randint(200,500) + BachelorFree
#         self.bet = random.randint(0,self.wealth)
#         return False
#
# class Employee :
#     def __init__(self,EmployeeWage):
#         self.wage=EmployeeWage
#
# class Croupier(Employee):
#     def CasinoGains(self):
#         if Table.CasinoGain > 0:
#         self.profitgain += 0.05*Table.CasinoGain
#
# class Barmen(Employee):
#     def Tips(self):
#         self.tips += Customer.tips
