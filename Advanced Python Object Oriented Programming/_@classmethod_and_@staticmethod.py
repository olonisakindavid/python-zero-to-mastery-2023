# blueprint - make it singular not plural
# memory efficient, repeatable and organised, makes for better organisation of code, thinking less procedural
class PlayerCharacter:
    # Class Object Attribute..not dynamic, its an actual attribute in the class
    membership = True  # true for all object, doesnt change across instances
    # constructor or init method

    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name  # gattributes / properties
            self.age = age

# method
    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('David', num1 + num2)

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2


# instanciate  --calling the class to create an object
player3 = PlayerCharacter('David', 21)
print(PlayerCharacter.adding_things(2, 3))
print(player3.age)
