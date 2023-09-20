# the binding of data and functions that manipulate that data encapsulated into one object
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age


player1 = PlayerCharacter('andrei', 100)
print(player1.name)
print(player1.age)
