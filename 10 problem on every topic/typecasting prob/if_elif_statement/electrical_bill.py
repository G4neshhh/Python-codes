# 🔥 Level 5 — Challenge

# 10. Electricity Bill Calculator ⚡

# Take electricity units from the user.

# Calculate the bill according to these slabs:

# Units	Rate
# 0–100	₹5/unit
# 101–200	₹7/unit
# 201–300	₹10/unit
# Above 300	₹15/unit

# Example:

# Enter units: 250

# Your program should calculate the bill according to the applicable slabs.

# 💡 Important

# For Q10, don't simply do:

# bill = units * 10

# You need to understand slab-wise calculation.

units = int(input("Enter your electricity bill units "))

if (units <=100 ):
    bill= units*5
    print(f"units rate is 5 And bill {bill}")
elif (units <=200 ):
    bill = units*7 
    print(f"units rate is 7 $ and bill {bill}")
elif (units <=300 ):
    bill = units * 10
    print(f"units rate is 10$ and this bill is {bill}")
elif (units >=400):
    bill = units* 15 
    print(f"units rate is 15$ and that bill is {bill }")

