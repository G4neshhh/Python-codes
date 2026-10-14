n = int(input("enter the value of n;"))
x = int(input("enter the value of x:"))
i=1
sum=0
while i<=n:
    j,pw,prod=1,1,1
    while j<=2*i-1:
        pw=pw*x
        prod=prod*j
        j=j+1
    k=pw/prod
    sum=sum+k
    i=i+1
print(f"sum of series is {sum}")

#now same program make in for loop
print(f"by using for loop")

n = int(input("enter a n value;"))
x= int(input("enter a x value:"))
sum =0
for i in range (1,n+1):
    pw,prod=1,1
    for j in range(1,2*1):
        pw=pw*x
        prod=prod*j
    k=pw/prod
    sum=sum+k
print(f"sum of series is {sum}")

        
