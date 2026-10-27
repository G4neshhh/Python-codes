
a=0
b=1

num = int(input("enter a number here : "))

for i in range (1,num +1):
    c=a+b
    a=b
    b=c
    print(c)

    