#parameters 
def say_hello(name, emoji):
    print(f'hello {name} {emoji}')

#positional arguments (the values we give a function)...we have to make sure they are in the right position
say_hello('David', '🤗')
say_hello('Favour', '🤗')
say_hello('Laja', '🤗')

#keyword arguments
# say_hello(emoji='🤗🤗', name='Djones')

#default parameters, without parameters, call the default
def hi(name='Djonesplays', emoji='🏸'):
    print(f'how are you {name} {emoji}')
    
hi()

