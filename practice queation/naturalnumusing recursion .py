def sumofnaturalnum(n):
    if n<=1:
        return n 
     
    else :
        return (n+sumofnaturalnum(n-1))

n = int(input("enter a number: "))
for i in range (n):
    if i<=0:
        print("positive number: ")
    else :
        print(sumofnaturalnum(n))

