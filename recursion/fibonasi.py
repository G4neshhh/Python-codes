def fibonsi(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return(fibonsi(n-1)+fibonsi(n-2))

n=int(input("enter any number"))
for i in range(1,n+1):
    f=fibonsi(i)
    print(f)
