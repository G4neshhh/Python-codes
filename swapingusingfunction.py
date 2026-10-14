def swaping(x,y):
    temp=x
    x=y               #we can also using x,y=y,x
    y=temp
    return(x,y)
x=int(input("enter first number:"))
y=int(input("second number:"))
x,y=swaping(x,y)
print(f"after swaping the x={x},and y={y}")

