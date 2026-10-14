fobj=open("test3.txt",'a')     # nkhiu9 in a ki jagaha x daal to wo test kr lega ki file present hai ki nhi 
if not fobj:
    print("file is not present in data")
else:
    str=input("enter your data...")
    fobj.write(str)
    pos=fobj.tell()
    print("file object postion is ",pos)
fobj.close()
