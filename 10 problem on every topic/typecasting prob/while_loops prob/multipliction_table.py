# Multiplication Table

# Take a number from the user and print its multiplication table from 1 to 10.

# Example:

# Enter number: 7

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 10 = 70



n = int(input("enter table number :"))
i=1
while i<=10:
    print(f"{n} * {i} = {n * i}")
    i=i+1
