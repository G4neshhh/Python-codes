x = int(input("enter value of x num :"))
n = int(input("enter num:"))
i = 1
pw=1
fact=1
sum=0
while i<= n:
    pw=pw*x
    fact=fact*i
    sum=sum+pw/fact
    i= i+1
print(f" {x} of power is  is;{sum}")
    
