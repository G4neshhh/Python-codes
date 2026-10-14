# Simple Calculator 🧮

# Take two numbers and an operator from the user.

# Example:

# Enter first number: 20
# Enter second number: 5
# Enter operator: *

# Perform:

# + → Addition
# - → Subtraction
# * → Multiplication
# / → Division

# Output:

# Result = 100

# If the user enters an invalid operator:

# Invalid operator

# Bonus: Also handle division by zero.


num1 = int(input("enter first number :"))
num2 = int(input("ENTER second number :"))
print("operator : '+' '-' '*' '/' ")
operator = input("enter a operator :")

if (operator== '+'):
    print(num1 + num2)
elif (operator == '-'):
    print(num1 - num2)
elif (operator == '*'):
    print(num1 * num2 )
elif (operator == '/'):
    print(num1 / num2 )
else :
    print("Enter invalid input ")