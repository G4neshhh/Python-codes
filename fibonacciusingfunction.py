def fibo(n):
    a,b=-1,1
    for i in range (1,n+1):
        c=a+b
        print(c)
        a=b
        b=c

n=int(input("enter a number:"))
fibo(n)                   #idhar hum ne use call kr diu
