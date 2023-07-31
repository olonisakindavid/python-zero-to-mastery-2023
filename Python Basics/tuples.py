#Tuple
#lists but are not modifiable
#immutable list
#tuples can be valid keys (1,2)

my_tuple = (1,2,3,4,5)
print(5 in my_tuple)
user = {
    (1,2): [1,2,3],
    'greet' : 'hello',
    'age': 20
}

print(user[(1,2)])