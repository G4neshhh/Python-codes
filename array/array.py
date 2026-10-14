from array import array
arr=array('i',[6,7,8,8,5,4,9])
print(arr)
arr.remove(8)
arr.append(889)  #last  array mai insert hota hai  
arr.insert(1,22) #when 1 is posion and 22 value
arr.extend([6,88,97])
print("elements are:")
for i in range(len(arr)):
    print(arr[i])
