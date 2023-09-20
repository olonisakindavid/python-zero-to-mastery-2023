# e.g in a game, lets explain inheritance

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
    def __init__(self, name, num_arrows):
        self.name = name
        self.power = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - of {self.num_arrows}')


wizard1 = Wizard('Merlin', 60)
print(isinstance(wizard1, object))
# print(isinstance(wizard1, Wizard))
# format is isinstance(instance, Class)
