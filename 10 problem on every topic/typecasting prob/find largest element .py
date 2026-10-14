list1 = [3, None, 14, None, 8, 21, None, 5]

# largest_num = None

# for item in list1:3
#     if item is None:
#         continue
        
#     if largest_num is None or item > largest_num:
#         largest_num = item

# print("The greatest number is:", largest_num)






list1 = [1,4,56, 67,8,21]
largest = list1[1]
i=0
while largest < len(list1):
  if list1[i] > largest:
    largest = list1[i]
    i +=1
print(largest)