def sum(n):
    if n==1:
        s=1
    else:
        s=n+sum(n-1)
        return s
    

n=int(input("enter a number:"))
s=sum(n)
print(f"given n is {n}and there sum is{s}")
