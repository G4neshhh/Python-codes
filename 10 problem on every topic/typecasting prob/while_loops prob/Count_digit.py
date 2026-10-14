# Count Digits

# Take an integer from the user and count how many digits it contains.

# Example:

# Enter number: 58392
# Number of digits = 5

# Hint: Use % and //.

n = int(input("enter a digits num "))
count =0
while n>0:
    r=n%10
    count+=1
    n=n//10
print(count)