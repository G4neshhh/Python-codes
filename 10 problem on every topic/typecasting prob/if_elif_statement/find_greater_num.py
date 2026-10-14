# Find Greater Number

# Take two numbers from the user and print which number is greater.

# Example:

# Enter first number: 25
# Enter second number: 40

# 40 is greater

# Also handle the case where both numbers are equal.

num1= int(input("enter a first num :"))
num2= int(input("enter a second num :"))

if (num1>num2):
    print(f"{num1} is a greater number ")
elif (num1<num2):
    print(f"{num2} is a greater number ")
elif (num1==num2):
    print("both are same equal value")
