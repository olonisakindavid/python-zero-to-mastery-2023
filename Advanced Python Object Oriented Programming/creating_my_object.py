# blueprint - make it singular not plural
class PlayerCharacter:
    # constructor or init method
    def __init__(self, name, age):
        self.name = name  # attributes / properties
        self.age = age

# method
    def run(self):
        print('run')
        return 'djones'


# instanciate  --calling the class to create an object
player1 = PlayerCharacter('David', 21)
player2 = PlayerCharacter('Delight', 22)
print(player1.age)
print(player2.run())
# player2.attack = 50
