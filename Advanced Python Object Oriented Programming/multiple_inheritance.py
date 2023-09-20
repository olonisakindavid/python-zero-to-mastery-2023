# multiple inheritance is complex
class User:
    def sign_in(self):
        print('logged in')


# sub classes

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.power = arrows

    def checks_arrows(self):
        print(f' {self.arrows} remaining')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, arrows)


hb1 = HybridBorg('borgie', 50, 100)
# print(hb1.run())
print(hb1.attack())
