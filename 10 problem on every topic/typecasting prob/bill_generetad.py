# 10. Bill Calculator 💰

# A restaurant bill is entered by the user as a string:

# bill = input("Enter bill amount: ")

# The user enters:

# 850

# Convert the bill into a suitable numeric type and calculate:

# GST = 18%
# Final bill = bill + GST

# Expected:

# Bill = 850
# GST = 153.0
# Final Bill = 1003.0

bill = input("Enter bill amount: ")

print(f"your bill is ",bill)

GST = (int(bill))*18/100
print(f"GST is ",GST)

total = int(bill) + GST
print(f"Total bill is", total)
