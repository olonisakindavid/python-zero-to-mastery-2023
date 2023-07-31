#unordered collections of unique objects, no duplicates, think of it like a dictionary,
my_set = {1,2,3,4,5,5}
my_set.add(100)
my_set.add(2)
print(my_set)

# my_list = [1,2,3,4,5,5]   converting list to set
# print(set(my_list))

# my_set = {1,2,3,4,5,5}  converting list to set
# print(list(my_set))
new_set = my_set.copy()
print(new_set)
print(my_set)