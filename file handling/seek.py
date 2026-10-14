fobj=open ("test3.txt",'r+')
if not fobj:
    print("file is not found")
else:
    fobj.seek(5,0)
    fobj.write("chutiya banaya tumko")
    fobj.seek(0,0)
    str=fobj.read()
    print(str)
    fobj.close()
    