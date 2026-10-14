

def factorial(n):
    i=1
    prod=1
    while i<=n:
        prod=prod*i
        i = i + 1
    return prod

n = int(input("enter any value  :"))

print("Factorial is ",factorial(n))
