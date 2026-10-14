def sum_digits(n):
    if n==0:
        return 0
    return(n%10+sum_digits(n//10))
n=int(input("enter a number ;"))
s=sum_digits(n)
print(f"given numbes{n}is sum of digits is {s}")
