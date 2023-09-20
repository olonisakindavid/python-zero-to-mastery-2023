# many - forms
class User(object):
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

# sub classes


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.power = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - of {self.num_arrows}')


wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)
