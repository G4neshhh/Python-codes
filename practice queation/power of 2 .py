interm = int(input("enter a number here: "))

result = list(map(lambda x: 2 ** x, range(interm+1)))

print(result)

for i in range (interm+1):
    print("2 power is",result)