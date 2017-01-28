import random
random.seed(1)

# nbroulettetables = 10
# nbcrapstables =10
# nbbarmen = 4
# employeewage = 200
# startingcash = 50000
# nbcustomers =100
# sharereturningcustomers = 0.5
# sharebachelorcustomers = 0.1
# freestartbudget = 200

class customer(object):
    def __init__(self, custID, table=0, bet =0, budget=0):
        self.custID = custID
        self.table = table
        self.bet = bet
        self.budget = budget
    def getDrink(self):
        drinkcost = random.randint(1,2) * 20
        self.budget -= drinkcost
        return drinkcost
    def giveTip(self):
        tip = random.randint(0,20)
        self.budget -= tip
        return tip
class returningcustomer(customer):
    def __init__(self, custID, bet=0, table=0, budget=0):
        super(returningcustomer, self).__init__(custID, table, budget, bet)
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
        super(onetimecustomer, self).__init__(custID, table, budget, bet)
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
    def __init__(self, freestartbudget, custID, table=0, budget=0, bet=0, ):
        super(bachelorcustomer, self).__init__(custID, table, budget, bet)
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
class Employee(object):
    def __init__(self, wage):
        self.wage = wage
class Croupier(Employee):
    def __init__(self, croupierID, wage, partofwin=0):
        super(Croupier, self).__init__(wage)
        self.partofwin = partofwin
        self.croupierID = croupierID
    def commission(self, partofwin):
        if partofwin > 0:
            self.partofwin += float(partofwin) * 0.05
class Barman(Employee):
    def __init__(self, wage, tips =0, alcsales=0):
        super(Barman, self).__init__(wage)
        self.tips = tips
        self.alcsales = alcsales
    def barmanTips(self, tip):
        self.tips += tip
    def barmanSales(self,sales):
        self.alcsales += sales
class table(object):
    def __init__(self, employeewage, tableID, minimumbet=0):
        self.tableID = tableID
        self.minimumbet = minimumbet
        self.croupier = Croupier(float(tableID),employeewage)
        self.employeewage = employeewage
class Craps(table):
    def __init__(self, tableID, employeewage, croupier=0,  minimumbet =0):
        super(Craps, self).__init__(employeewage,tableID, croupier)
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
        # print(" Throwing the dice")
        # print(" The sum of the upper faces  ", dice)
        # if sum(rightbet) > 0:
        #     print(" There are ", sum(rightbet), " winner(s)")
        # else:
        #     print("No player won")


        Probs = list([i / 36 for i in range(1, 6)]) + [6 / 36] + list(reversed([i / 36 for i in range(1, 6)]))
        Coeff = [0.9 / i for i in Probs]

        PlayerGains = [i * Coeff[k - 2] * j * l for i, k, j, l in zip(amounts, bets, A, rightbet)]
        CasinoGain = sum(amounts) - sum(PlayerGains)

        return [CasinoGain, PlayerGains]
class Roulette(table):

    def __init__(self, employeewage, tableID, croupier=0,  minimumbet=0):
        super(Roulette,self).__init__(employeewage, tableID, minimumbet)
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
        # print(" Spinning the wheel...")
        # print(" Ball lands on " + str(winnumb))
        # if sum(rightnumber) > 0:
        #     print(" There are " + str(sum(rightnumber)) + " correct bet(s)")
        # else:
        #     print("No winners this round")

        PlayerGains = [i * j * k * 30 for i, j, k in zip(amounts, A, rightnumber)]
        CasinoGain = sum(amounts) - sum(PlayerGains)
        return [CasinoGain, PlayerGains]


class Casino(object):
    def __init__(self, nbroullettetables, nbcrapstables, nbbarmen, employeewage, startingcash, nbcustomers, sharereturningcustomers, sharebachelorcustomers, freestartbudget):
        self.cash = startingcash
        self.nbroulettetables = nbroullettetables
        self.nbcrapstables = nbcrapstables
        self.nbbarmen = nbbarmen
        self.employeewage = employeewage
        self.nbcustomers = nbcustomers
        self.sharereturningcustomers = sharereturningcustomers
        self.sharebachelorcustomers = sharebachelorcustomers
        self.freestartbudget = freestartbudget
    def getCash(self,income):
        if income > 0:
            self.cash += float(income)*0.95
    def DrinkCash(self,cash):
        self.cash += cash

    def SimulateEvening(self):
            #Create the customers
            loscostumers = []
            for i in range(int(self.sharereturningcustomers * self.nbcustomers)):
                loscostumers.append(returningcustomer(i+1))
            for i in range(int(self.sharereturningcustomers * self.nbcustomers ), int(self.sharereturningcustomers * self.nbcustomers + self.sharebachelorcustomers * self.nbcustomers)):
                loscostumers.append((bachelorcustomer(i+1, self.freestartbudget)))
            for i in range(int(self.sharereturningcustomers * self.nbcustomers + self.sharebachelorcustomers * self.nbcustomers), int(self.nbcustomers)):
                loscostumers.append((onetimecustomer(i+1)))


            #Create the tables
            lostables = []
            for i in range(self.nbroulettetables):
                lostables.append(Roulette(i+1,self.employeewage))
            for i in range(self.nbcrapstables):
                lostables.append(Craps(i+self.nbroulettetables+1, self.employeewage))

            # Create the Croupiers
            loscroupiers = []
            for i in range(self.nbroulettetables + self.nbcrapstables):
                loscroupiers.append(Croupier(i,self.employeewage))

            #Create de Barmans
            losbarmans=[]
            for i in range(self.nbbarmen):
                losbarmans.append(Barman(i,self.employeewage))


            for i in range(3):

                losdrinkers = []
                for i in range(len(loscostumers)):
                    if loscostumers[i].budget > 60:
                        losdrinkers.append(loscostumers[i])
                losdrinkers = random.sample(losdrinkers, len(losbarmans))

                    # Update the budgets and the gains
                for i in range(len(losdrinkers)):
                    losbarmans[i].barmanTips(losdrinkers[i].giveTip())
                    losbarmans[i].barmanSales(losdrinkers[i].getDrink())
                    self.DrinkCash(losdrinkers[i].getDrink())

                    # Sitdown players for a round
                for i in range(len(loscostumers)):
                    loscostumers[i].sitdown(lostables)

                    # Update the bets since now they are seated at tables
                for i in range(len(loscostumers)):
                    loscostumers[i].setbet()

                    # Create a list with lists of players for each table
                jugadores = [[] for item in lostables]
                for z in range(len(jugadores)):
                    for item in range(len(loscostumers)):
                        if loscostumers[item].table == lostables[z]:
                            jugadores[z].append(loscostumers[item])

                    # Simulate one round
                for i in range(len(lostables)):
                    amounts = []
                    for j in range(len(jugadores[i])):
                        amounts.append(jugadores[i][j].bet)
                    auxiliary = lostables[i].SimulateGame(amounts)
                    for j in range(len(jugadores[i])):
                        jugadores[i][j].updatewealth(auxiliary[1][j])
                    loscroupiers[i].commission(auxiliary[0])
                    self.getCash(auxiliary[0])

                    # Drinking one more time
                losdrinkers = []
                for i in range(len(loscostumers)):
                    if loscostumers[i].budget > 60:
                        losdrinkers.append(loscostumers[i])
                losdrinkers = random.sample(losdrinkers, len(losbarmans))

                    # Update the budgets and the gains
                for i in range(len(losdrinkers)):
                    losbarmans[i].barmanTips(losdrinkers[i].giveTip())
                    losbarmans[i].barmanSales(losdrinkers[i].getDrink())
                    self.DrinkCash(losdrinkers[i].getDrink())

            # We don't forget to pay our employees
            self.cash -= self.employeewage * (self.nbbarmen + self.nbcrapstables + self.nbroulettetables)


JoyCasino = Casino(10, 10, 4, 200, 50000, 100, 0.5, 0.1, 200)

JoyCasino.SimulateEvening()

print(JoyCasino.cash)