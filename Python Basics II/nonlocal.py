#refers to parent local
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:",x)

    
    inner()
    print("outer:", x)

outer()

#scope is useful so we dont use cpu resources too much