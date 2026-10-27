from array import array
arr=array ('i',[3,5,6,77,7])
print(arr)
sum = 0 
n = int(input("enter sum of number "))
for i in range (n):
    sum = sum+arr[i]
print(sum)


