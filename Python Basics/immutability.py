#strings are immutable

selfish = '01234567'

selfish[0] = '8'

print(selfish)

#this will print an error because we cant change an index of a string just like that
#unless you replace the whole variable name, so the previous one will be forgotten in the systems storage


selfish = '81234567'
print(selfish)