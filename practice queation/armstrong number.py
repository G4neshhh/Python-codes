lower = int(input("enter a lower limit hare : "))
upper = int(input("enter a upper limit hare : "))

for num in range (lower,upper +1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp>0:
        digit=temp%10
        sum += digit**order
        temp //=10
    if num == sum:
        print(num)