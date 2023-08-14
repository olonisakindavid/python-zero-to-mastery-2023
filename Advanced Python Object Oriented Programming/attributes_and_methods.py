# blueprint - make it singular not plural
# memory efficient, repeatable and organised, makes for better organisation of code, thinking less procedural
class PlayerCharacter:
    # Class Object Attribute..not dynamic, its an actual attribute in the class
    membership = True  # true for all object, doesnt change across instances
    # constructor or init method

    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name  # attributes / properties
            self.age = age

# method
    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'my name is {self.name}')


# instanciate  --calling the class to create an object
player1 = PlayerCharacter('David', 21)
player2 = PlayerCharacter('Delight', 22)

player2.attack = 50

print(player1.run('hello'))
print(player2.shout())
