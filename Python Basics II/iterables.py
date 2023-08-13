#iterable - list, dictionary, tuple,  set, string   (this can be iterated and not integers etc e.g 50)
#iterate -> checks one by one each item in the collection

user = {
    'name': 'David',
    'age': 21,
    'can_swim': False
}

#3 ways to iterate
# for item in user:
#     print(item)  #prints the keys of the dictionary

for item in user.items():
    print(item)  #print the key value pair of the dictionary

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

#shortcut
for key, values in user.items():
    print(key, values)