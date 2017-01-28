class Animal(object):
    """All animals"""
    alive = ""

    def __init__(self, name, age):
        self.name = name
        self.age= age
    # Add your method here!

    def description(self):
        print(self.name)
        print(self.age)

    def setAlive(self, alive):
        self.alive= alive

    def getAlive(self):
        return self.alive

horse = Animal("Hilda", 22)
horse.description()
horse.setAlive(True)
print(horse.getAlive())
horse.alive=False
