fobj=open("text56.txt",'r')
if not fobj:
    print("file is not open ")
else:
    str=fobj.read()
    print(str)
    fobj.close()

