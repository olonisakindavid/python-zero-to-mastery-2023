#args
def super_func(*args):
    print(*args)
    return sum(args)

print(super_func(1,2,3,4,5))

#args  -this is what python developers already recon with (used too in the community)

#keyword arguments (kwargs)
def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))

#rule: parameters, *args, default parameters, **kwargs
# def super_func(name, *args, i ='hi' **kwargs):
#     following the rule

