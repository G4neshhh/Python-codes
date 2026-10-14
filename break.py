for i in range (1,11):
    print(i)
    if i>5:
        break
    
    
print(f"now for multi")
for i in range (1,11):
    for j in range(1,8):
        print(i,j)
        if j>1:
           break

print(f"for continue")

for n in range(1,12):
    if n>5:
        continue
    print(n)

print(f"now tell me")
for i in range (1,11):
     if i<5:
         continue
     print(i)
        
        
