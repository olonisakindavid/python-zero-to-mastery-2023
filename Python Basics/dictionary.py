#key, values.....data sructures
# dictionary = {
#     'a': 1,
#     'b': 2
# }

# print(dictionary['b'])
# print(dictionary)

# dictionaries arent ordered, hold more info
dictionary = {
    'a' : [1,2,3],
    'b' : 'hello',
    'x' : True
}

#list is ordered
my_list = [
    {
    'a' : [1,2,3],
    'b' : 'hello',
    'x' : True
    },
    {
    'a' : [1,2,3],
    'b' : 'hello',
    'x' : True
    }   
    ]

print(dictionary['a'][2])
print(my_list[0]['a'][1])