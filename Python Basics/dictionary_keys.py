#dictionary keys must be immutable i.e must not be changed, so we cant use a list to start as a key in our dictionary, most of the times, strings are used
#keys must be unique also, must only exist once

dictionary = {
    '123': [1,2,3 ],
    '123' : "hello"
}
print(dictionary['123'])