fobj=open("Test44.txt",'w')
if not fobj:
    print("file is not present ")
# when file is not present then "w" command create a new file in code 
else:
    fobj.write("now ganu is starting there coding jurney ")
    print("file is created")
fobj.close()
