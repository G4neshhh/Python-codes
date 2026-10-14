n = int(input("enter any number:"))
i =2
flag = True
while i<n and flag==True:
    if n%i==0:
         flag=False
         i=i+1
if flag==True:
        print(n,"is prime")
else:
    print(n,"is not prime number")
#now for cheking the fisrt prime number

n
