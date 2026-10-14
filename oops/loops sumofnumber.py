class math1:
    def __init__(self,n):
        self.n=n

    def sum1(self):
        sum=0
        for i in range (1,n+1):
            sum=sum+i
        return sum

    def sumodd(self):
            sumo=0
            for i in range (1,n+1):
                sumo=sumo+2*i-1
            return sumo
    
    def factorial(self):
            prod=1
            for i in range (1,n+1):
              prod=prod*i
            return prod
              
    
n=int(input("enter a number:"))

ob1=math1(n)
s=ob1.sum1()
print(s)

ob2=math1(n)
s2=ob1.sumodd()
print(f"the sum of odd number is {s2}")

ob3=math1(n)
ft=ob3.factorial()
print(f"facatorial n number of  is {ft} ")

        
        