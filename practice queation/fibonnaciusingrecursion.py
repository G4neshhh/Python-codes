a=0
b=1
def fibo (n):
    if n <= 1:
        return n
    else :
        return fibo (n-1) + fibo(n-2)

n = int(input("enter number here: "))

for i in range (n):
    if i <=0:
        print("enter a positive number ")
    else :
        print("fibonacci sequence is :")
        for i in range (n):
            print(fibo(i))


