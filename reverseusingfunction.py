def reverse(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev

n=int(input("enter nay number:"))
rev=reverse(n)
print(f"revers is {rev}")
