print("enter the subject marks")
ph = int(input("physics mark enter;"))
ch = int(input("chemistry marks enter;"))
ma = int(input("math marks enter;"))


total = (ph+ch+ma)
print("total marks is",total)

per = (total/300)*100

print(per,"% is")

if ph>33 and ch>33 and ma>33:
    print("student is pass")
else:
    print("student is fail")
        
