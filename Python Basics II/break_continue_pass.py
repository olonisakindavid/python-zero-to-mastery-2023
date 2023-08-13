my_list = [1, 2, 3]
for item in my_list:
    continue
    print(item)
  # goes back to for loop

i = 0
while i < len(my_list):
    i += 1
    continue
    print(my_list[i])


# pass - doesnt really do anything, just passes to the next line
for item in my_list:
    pass  # just to keep here till i wanna put something.
