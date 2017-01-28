import random

nbroulettetables = 10
nbcrapstables =10
nbbarmen = 4
employeewage = 200
startingcash = 50000
nbcustomers =100
sharereturningcustomers = 0.5
sharebachelorcustomers = 0.1
freestartbudget = 200


class customer(object):
    def __init__(self, custID):
        self.custID = custID
    def sitdown(self, tablelist):
        return random.choice(tablelist)

class returningcustomer(customer):
    def __init__(self, bet=0):
        # self.custID = custID
        self.budget = random.randint(100, 300)
        self.bet = bet
    def setbet(self, table):
        if self.budget >= table.minimumbet:
            self.bet = table.minimumbet
        else:
            self.bet=0

class onetimecustomer(object):
    def __init__(self, custID):
        self.custID = custID
        self.budget = random.randint(200, 300)
        self.bet = random.randint(0, self.budget)

class bachelorcustomer(object):
    def __init__(self, custID):
        self.custID = custID
        self.budget = random.randint(200, 500)+freestartbudget
        self.bet = random.randint(0, self.budget // 3)

class table(object):
    def __init__(self, tableID):
        self.tableID = tableID

class Craps(table):
    def SimulateGame(amounts):
        A = []
        minimum = random.choice([0, 25, 50])
        for item in amounts:
            A.append(bool(item >=minimum))
        bets = [random.randint(2, 12) for i in amounts]
        dice = random.randint(1, 6) + random.randint(1, 6)
        rightbet = []
        for item in bets:
            rightbet.append(bool(item == dice))
        print(" Throwing the dice")
        print(" The sum of the upper faces  ", dice)
        if sum(rightbet) > 0:
            print(" There are ", sum(rightbet), " winner(s)")
        else:
            print("No player won")


        Probs = list([i / 36 for i in range(1, 6)]) + [6 / 36] + list(reversed([i / 36 for i in range(1, 6)]))
        Coeff = [0.9 / i for i in Probs]

        PlayerGains = [i * Coeff[k - 2] * j * l for i, k, j, l in zip(amounts, bets, A, rightbet)]
        CasinoGain = sum(amounts) - sum(PlayerGains)

        return [CasinoGain, PlayerGains]

class Roulette(table):

    def SimulateGame(amounts):
        minimum = random.choice([50, 100, 200])
        A=[]
        bets = [random.randint(0,36) for i in amounts]
        for item in amounts:
            A.append(bool(item >= minimum))
        winnumb = random.randint(0, 36)
        rightnumber= []
        for item in bets:
            rightnumber.append(bool(item == winnumb))
        print(" Spinning the wheel...")
        print(" Ball lands on " + str(winnumb))
        if sum(rightnumber) > 0:
            print(" There are " + str(sum(rightnumber)) + " correct bet(s)")
        else:
            print("No winners this round")

        PlayerGains = [i * j * k * 30 for i, j, k in zip(amounts, A, rightnumber)]
        CasinoGain = sum(amounts) - sum(PlayerGains)
        return [CasinoGain, PlayerGains]

#Create the customers
loscostumers = []
for i in range(int(sharereturningcustomers * nbcustomers)):
    loscostumers.append(returningcustomer(i+1))
for i in range(int(sharereturningcustomers * nbcustomers +1), int(sharereturningcustomers * nbcustomers + sharebachelorcustomers * nbcustomers)):
    loscostumers.append((bachelorcustomer(i+1)))
for i in range(int(sharereturningcustomers * nbcustomers + sharebachelorcustomers * nbcustomers +1), int(nbcustomers)):
    loscostumers.append((onetimecustomer(i+1)))

#Create the tables
lostables = []
for i in range(nbroulettetables):
    lostables.append(Roulette(i+1))
for i in range(nbcrapstables):
    lostables.append(Craps(i+nbroulettetables+1))

