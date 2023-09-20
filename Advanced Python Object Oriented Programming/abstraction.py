# hiding/abstracting of information, getting access to only whats neccessary, or needed
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')


player1 = PlayerCharacter('andrei', 100)
player1.name = '!!!'
player1.age = 'BOOO'

print(player1.age)
