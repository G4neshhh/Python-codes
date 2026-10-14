class addition():
    def addition(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return(self.a+ self.b)

ob1=addition()
a=int(input("Enter a first value: "))
b=int(input("enter second value: "))

ob1.addition(a,b)       #only declared attribut are using it 
s=ob1.add()                               # . dot only in objectts not in functions
print(f"additon is {s}")

# same we are create a for all arithmatic equation just change the nae of calss math and add more function means in 
#oops method add like  def multi(self) like these are 