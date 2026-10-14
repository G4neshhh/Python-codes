n =int(input("enter any number;"))
i = 0
esum= 0
osum=0
while i<=n:
    if  i%2== 0:
        esum= esum+i
    else:
        osum=osum+i
    i=i+1
print(f"odd sum {osum} and even sum {esum}")
        
