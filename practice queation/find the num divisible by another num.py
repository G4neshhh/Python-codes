# print("the divisible by 13 is : ")
# for i in range ( 1,100):
#     if  i % 13 == 0:
#         print(i)

# using lambda function and filter function ()
l = [12,13,23,45,67,63,144,45,6,555,67,78]
result = list(filter(lambda x : x % 13 == 0,l))
print("only write a divied num ",result)
