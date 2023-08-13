def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 !=0:
      return False

print(is_even(51))

#to make this code clean
def is_even(num):
    return num % 2 == 0
print(is_even(51))