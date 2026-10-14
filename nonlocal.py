x=22
def outer():
    x=55
    print("outer varible :",x)
    def inner():
        nonlocal x
        x=22
        print("inner varialbe,",x)
    inner()
    print("nonlocal variable is:",x)   #by using nonlocal 55 is update into 22

outer()
print("global variable",x)