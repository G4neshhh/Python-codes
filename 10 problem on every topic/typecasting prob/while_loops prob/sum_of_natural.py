# . Sum of 1 to N

# Take a number n from the user and calculate the sum from 1 to n.

# Example:

# Enter n: 10
# Sum = 55

# Because:

# 1 + 2 + 3 + ... + 10 = 55

n= int(input("enter your num "))
i=1
sum=0
while i<=n:
    sum = sum+1
    print(sum)
    i=i+1