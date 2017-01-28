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
    def getDrink(self):
        self.budget -= (random.randint(1,2) * 20 + Barman.barmantips())


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

class Employee(object):
    def __init__(self, wage=0):
        self.wage = wage

class Croupier(Employee):
    def __init__(self, croupierID, wage=0, partofwin=0):
        super(Croupier, self).__init__(wage)
        self.partofwin = partofwin
        self.croupierID = croupierID
    def commission(self, partofwin):
        if partofwin > 0:
            self.partofwin += float(partofwin) * 0.05

class Barman(Employee):
    def __init__(self, wage=0, alcsales =0):
        super(Barman, self).__init__(wage)
        self.alcsales = alcsales
    def barmantips(self):
        self.alcsales +=random.randint(0,20)

#Create the customers
loscostumers = []
for i in range(int(sharereturningcustomers * nbcustomers)):
    loscostumers.append(returningcustomer(i+1))
for i in range(int(sharereturningcustomers * nbcustomers ), int(sharereturningcustomers * nbcustomers + sharebachelorcustomers * nbcustomers)):
    loscostumers.append((bachelorcustomer(i+1)))
for i in range(int(sharereturningcustomers * nbcustomers + sharebachelorcustomers * nbcustomers), int(nbcustomers)):
    loscostumers.append((onetimecustomer(i+1)))



#Create the tables
lostables = []
for i in range(nbroulettetables):
    lostables.append(Roulette(i+1))
for i in range(nbcrapstables):
    lostables.append(Craps(i+nbroulettetables+1))

loscroupiers = []
for i in range(nbroulettetables+nbcrapstables):
    loscroupiers.append(Croupier(i))


losbarmans=[]
for i in range(nbbarmen):
    losbarmans.append(Barman(i))

losdrinkers = []
for i in range(len(loscostumers)):
    if loscostumers[i].budget > 60:
        losdrinkers.append(loscostumers[i])