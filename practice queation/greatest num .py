num1 = int(input("enter a value for a"))
num2 = int(input("enter a value for b"))
num3 = int(input("enter a value for c"))

if num1>num2 and num1>num3:
    print("num1 is greater")
elif num1<num2 and num2>num3:
    print(num2,"b is greater")
else :
    print(num3," c is a greater value")