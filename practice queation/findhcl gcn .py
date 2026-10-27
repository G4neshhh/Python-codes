def findhcl (x,y):
    if x >y:
        smaller = y
    else :
        smaller = x
    for i in range(1, smaller+1):
        if ((x % i == 0 ) and (y % i == 0)):
            hcl=i
    return (hcl)
print("the hcl is",findhcl(12,30))

