i = 1
while i<=2:
    j=1
    while j<=3:
        print(i,"",j)
        j=j+1
    i=i+1
    
print(f"same logic for loop")
for i in range(1,3):
    for j in range(1,4):
        print(i,"",j)
        
print(f"by user giving input number")
m =int(input("enetr a value for m"))
n = int(input("enter a value for n"))
for m in range(1,m+1):
    for n in range (1,n+1):
        print(m,"",n)
    
        
