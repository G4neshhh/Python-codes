fobj1=open("text56.txt",'r')
fobj2=open("test44.txt",'w')
if not fobj1:
    print("file is not created...")
else:
    str=fobj1.read()
    fobj2.write(str)
    print("file data is copy")
    fobj1.close()
    fobj2.close()
