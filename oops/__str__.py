class addition():
    def __init__(self,a,b):                     #write every code right itd case sensetive 
        self.a=a
        self.b=b
        print("constructor are colled")

    def __str__(self):
        str="a is="+(a)+"b is"+(b)
        return str

    def add(self):
        return(self.a+self.b)

a=input("enter any name ;")
b=input("enter any second name;")  

s1=addition(a,b)
print(s1)
s=s1.add()
print(s)
