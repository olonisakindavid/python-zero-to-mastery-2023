user = {
    'basket': [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

print('basket' in user)
print('age' in user.keys())
print(20 in user.values())
print(user.items())

user2 = user.copy()
print(user.clear())
print(user2)

print(user.pop('age'))
print(user)

print(user.popitem()) #pops out last key and value
print(user.update({'age': 55}))