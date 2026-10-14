
class math:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c 
        print("constraction are called ")

    def greater(self):
        if a>b and a>c:
            return a 
            print(f"{a} a is greter than b ") 

        elif b<c:  
            return c 
        
        else :
    
            return b

a=int(input("enter a first number: "))
b=int(input("enter b second number :"))
c =int(input("enter c thrid number :"))

ob1 =math(a,b,c)
g=ob1.greater()
print("greater num is ",g)






















