from array import array 
arr=array ('i')
n=int(input("enter a array value:"))

print("Enter a elementin that array :")
for i in range(n):
    item=int(input())
    arr.append(item)
for i in range (n//2):
    arr[i],arr[n-(i+1)]=arr[n-(i+1)],arr[i]
    print("reverse array is")
    for i in range (n):
        print(arr[i])
                 




