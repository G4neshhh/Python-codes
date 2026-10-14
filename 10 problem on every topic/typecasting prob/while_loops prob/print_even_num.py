# Print Even Numbers

# Using a while loop, print all even numbers from 1 to 20.

# Expected:

# 2 4 6 8 10 12 14 16 18 20
n = int(input("enter your number "))
i=1 
while i<=n:
    j=2*(i)
    print(j)
    i=i+1