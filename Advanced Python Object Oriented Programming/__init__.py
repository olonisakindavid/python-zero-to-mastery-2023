# blueprint - make it singular not plural
# memory efficient, repeatable and organised, makes for better organisation of code, thinking less procedural
class PlayerCharacter:
    # Class Object Attribute..not dynamic, its an actual attribute in the class
    membership = True  # true for all object, doesnt change across instances
    # constructor or init method

    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.name = name  # attributes / properties
            self.age = age

# method
    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'my name is {self.name}')


# instanciate  --calling the class to create an object
player1 = PlayerCharacter('David', 10)
print(player1.shout())
