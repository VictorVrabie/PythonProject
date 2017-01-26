import random
# random.seed(20)

nbRoulette = 10
nbCraps = 10
nbBarmen = 4
EmployeeWage = 200
CasionStartCash = 50000
nbCustomers = 100
prcReturning = 50
prcBachelor = 10
BachelorFree = 200
RouletteMinimum = [50, 100, 200]
CrapsMinimum = [0, 25, 50]


class Customer(object):
    def __init__(self, typeC, ID):
        self.typeC = typeC
        self.ID = ID
        if self.typeC == "Returning":
            self.bet = 10
            self.budget = random.randint(100, 300)
        elif self.typeC == "New":
            self.budget = random.randint(200, 300)
            self.bet = random.randint(0, int((self.budget) / 3))
        else:
            self.budget = random.randint(200, 500) + BachelorFree
            self.bet = random.randint(0, int(self.budget))
        self.table = random.randint(1,(nbRoulette+nbCraps)+1)

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
for i in range(1, (nbRoulette+nbCraps)+1):
    tableplayers = []
    for j in range(nbCustomers):
        if Customers[j].table == i:
            tableplayers.append(Customers[j])
    listoftables.append(tableplayers)


class Table(object):
    def __init__(self, number):
        self.number = number
        self.players = listoftables[number-1]
        self.amounts = []
        for i in range(len(self.players)):
            self.amounts.append(self.players[i].bet)

class Roulette(Table):

    def SimulateGame(self):
        minamount = random.choice(RouletteMinimum)
        amount = self.amounts
        bets=[]
        for i in range(len(self.players)):
            bets.append(random.randint(0,36))

        def AboveMinimum(amounts):
            output = []
            for item in amounts:
                output.append(bool(item >= minamount))
            return (output)

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

        PlayerGains = [i * j * k * 30 for i, j, k in zip(amount, AboveMinimum(amount), SpinTheWheel(bets))]
        CasinoGain = sum(amount) - sum(PlayerGains)
        if CasinoGain > 0:
            CasinoGain = CasinoGain * 0.95
        return (CasinoGain, PlayerGains,amount,bets)


print(Roulette.SimulateGame(Table(13)))






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
