def factorial( a ):
    if a == 0 :
        return 1
    else :
        return ((a)*(factorial(a-1)))
num = int(input("enter a value of "))
result = factorial(num)
print("the factorial is ", result )
    
    