from array import array
arr=array('i')                #creating a empty array


n=int(input("enter a element in the array "))


print("enter elements :")    #/ print ke niche hii for use krna ok no gap no space 
for i in range(n):                                      
    item=int(input())
    arr.append(item)

sum=0
for i in range (n):
    sum=sum+arr[i]

print("sum of elements of array is",sum)