def add(*args):
    print(args)
    print(type(args))
    sum=0
    for i in args:
        sum +=i
    print(sum)


add(1,2,3,4,6,7,8)
        \

# also use of **kwargs 

def myDetails(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)

myDetails(name="ganu",age="22",work="unemployment")