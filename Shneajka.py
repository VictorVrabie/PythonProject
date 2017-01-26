import random
class Customer:
    def __init__(self, wealth, bet):
        self.wealth = wealth
        self.bet = bet

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
    def rich(self, Table.Minbet):
        self.wealth = random.randint(100,300)
        self.bet = Table.Minbet
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
    def CasinoGain(self):
        self.profitgain = 0.05*Table.CasinoGain

class Barmen(Employee):
    def Tips(self):
        self.tips += Customer.tips

