for i in range (1,5):
    for j in range(1,4-i+1):
        print("  ",end="")     #space vr pan depend krt ki output ks aarange hoil tr ok
    for j in range (i,0,-1):
        print("*","",end="")  #agar j ki jaga i liya to 1 2 3 print honag star ki jagaha 
    print()
