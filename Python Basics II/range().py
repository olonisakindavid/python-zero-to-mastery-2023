#very useful in for loops, creates a special type of object we can iterate over

for number in range(0,10):
    # print(number)
    print('i love Jesus')

for _ in range(0,10):   #underscores can be used actually
    print(_)

#range comes with 3 parameter..called step,
for _ in range(0,10,2):  
    print(_)

for _ in range(10,0, -1):   #descending
    print(_)

for _ in range(10):   #underscores can be used actually
    print(_)

for _ in range(2):  
    print(list(range(10)))