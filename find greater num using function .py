def greater(x,y):
    if x>y:               #this is you function man you create it 
        return x
    return y

x = int(input("enetr any vlue for x ;"))
y = int(input("enetr anay value for y:"))
k =greater(x,y)
                              #bro in that u call the function by help off k 
print("the gretaest value is",k )

#now simple make for 3 value 
def greater3(x,y,z):
    if x>y and x>z:                    #using right logic operator not using or becuse they only ather wise 
        return x
    if y>z:
        return y
    return z
x = int(input("enter x value:"))
y = int(input("enetr y value;"))
z = int(input("enetr z value :"))

k = greater3(x,y,z)
print("the graatest value is :",k)
    