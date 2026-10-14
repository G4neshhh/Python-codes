# . Mixed Type Casting

# Given:

# a = "10"
# b = 5.5
# c = 2

# Using type casting, calculate:

# Result = (a + b) * c

# Expected result should be a float.

# Don't change the original variables.

a = "10"
b = 5.5
c = 2

result = (int(a)+float(b)*c)
print(float(result))