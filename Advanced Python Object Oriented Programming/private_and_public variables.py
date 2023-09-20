# using _    ..but doesnt guarantee it   -private    also like dunder file __something__, so we shouldnt overwrite

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')


player1 = PlayerCharacter('andrei', 100)

print(player1.age)
