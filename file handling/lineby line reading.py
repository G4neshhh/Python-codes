obj=open("text56.txt",'r')
if not obj:
    print("file is not open")
else:
    for line in obj:      # in that code file is reading one by one 
        print(line)
    obj.close()
