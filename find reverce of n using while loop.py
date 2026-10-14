#find reverce of n by using while loop
n = int(input("enter a number for reverce;"))
rev = 0 # 475 => 574
while n>0:
    r = n % 10
    rev = rev*10+r 
    n = n //10
print(f"{n} s revers value is {rev}")
    
