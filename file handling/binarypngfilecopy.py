fobj1=open("system.png",'rb')    #bas r ke pichee binary data ka "b" lagana hai bs 
fobj2=open("mintu.png",'wb')     #same yaha par bhi wahi kiya gaya hai "b" lagaya gaya hai 
if not fobj1:
    print("image is not found")
else:
    str=fobj1.read()
    fobj2.write(str)
    print('image is copy ')
    fobj1.close()
    fobj2.close()
