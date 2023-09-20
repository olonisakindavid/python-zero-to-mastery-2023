class A:
    num = 10


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())
print(D.__mro__)

# depth first search is dealing with the algorithm
