def gcd(m,n):
    if n==0:
        g=m
    else:
        g=gcd(n,m%n)
    return g


m=int(input("enter  first number;"))
n=int(input("enter second number;"))
g=gcd(m,n)
print(f"{m}first and seconds{n} greatest common divisoin is {g}")