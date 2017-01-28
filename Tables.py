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
    def __init__(self, custID, table=0, bet =0, budget=0):
        self.custID = custID
        self.table = table
        self.bet = bet
        self.budget = budget


class returningcustomer(customer):
    def __init__(self, custID, bet=0, table=0, budget=0):
        super(returningcustomer, self).__init__(custID)
        super(returningcustomer, self).__init__(table)
        super(returningcustomer, self).__init__(budget)
        super(returningcustomer, self).__init__(bet)
        self.budget = random.randint(100, 300)
    def setbet(self):
        if self.budget >= self.table.minimumbet:
            self.bet = self.table.minimumbet
        else:
            self.bet=0
    def sitdown(self, tablelist):
        self.table = random.choice(tablelist)
    def standup(self, table=0):
        self.table = table
    def updatewealth(self,update):
        self.budget += update -self.bet
class onetimecustomer(customer):

    def __init__(self, custID, table=0, bet=0, budget=0):
        super(onetimecustomer, self).__init__(custID)
        super(onetimecustomer, self).__init__(table)
        super(onetimecustomer, self).__init__(budget)
        super(onetimecustomer, self).__init__(bet)
        self.budget = random.randint(200, 300)
        self.bet = random.randint(0, self.budget)
    def sitdown(self, tablelist):
        self.table = random.choice(tablelist)
    def standup(self, table=0):
        self.table = table
    def updatewealth(self,update):
        self.budget += update -self.bet
    def setbet(self):
        return False
class bachelorcustomer(customer):
    def __init__(self, custID, table=0, budget=0, bet=0):
        super(bachelorcustomer, self).__init__(custID)
        super(bachelorcustomer, self).__init__(table)
        super(bachelorcustomer, self).__init__(budget)
        super(bachelorcustomer, self).__init__(bet)
        self.budget = random.randint(200, 500) + freestartbudget
        self.bet = random.randint(0, self.budget // 3)
    def sitdown(self, tablelist):
        self.table = random.choice(tablelist)
    def standup(self, table=0):
        self.table = table
    def updatewealth(self,update):
        self.budget += update -self.bet
    def setbet(self):
        return False
class table(object):
    def __init__(self, tableID, minimumbet=0):
        self.tableID = tableID
        self.minimumbet = minimumbet
class Craps(table):
    def __init__(self, tableID, minimumbet =0):
        super(Craps, self).__init__(tableID)
        super(Craps,self).__init__(minimumbet)
        self.minimumbet = random.choice([0, 25, 50])
    def SimulateGame(self, amounts):
        A = []
        for item in amounts:
            A.append(bool(item >=self.minimumbet))
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

    def __init__(self, tableID, minimumbet=0):
        super(Roulette,self).__init__(tableID)
        super(Roulette,self).__init__(minimumbet)
        self.minimumbet = random.choice([50, 100, 200])

    def SimulateGame(self, amounts):
        A=[]
        bets = [random.randint(0,36) for i in amounts]
        for item in amounts:
            A.append(bool(item >= self.minimumbet))
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

#Sitdown players for a round
for i in range(0, len(loscostumers)):
    loscostumers[i].sitdown(lostables)

#Update the bets since now they are seated at tables
for i in range(1,len(loscostumers)):
    loscostumers[i].setbet

#Create a list with lists of players for each table
jugadores = [[] for item in lostables]
for z in range(0, len(jugadores)):
    for item in range(0, len(loscostumers)):
        if loscostumers[item].table == lostables[z]:
            jugadores[z].append(loscostumers[item])

#
# # Check that the functions are working and tables are getting players
# print(jugadores)
# for i in range(len(jugadores)-1):
#     print(len(jugadores[i]))


# Simulate one round
for i in range(len(lostables)):
    amounts = []
    for j in range(len(jugadores[i])):
        amounts.append(jugadores[i][j].bet)
    auxiliary=lostables[i].SimulateGame(amounts)

# update the wealth of each customer

    playergains = auxiliary[1]
    casinogain = auxiliary[0]
    jugadores[i][j].updatewealth(playergains[j])
    print(auxiliary)