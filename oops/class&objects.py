class student:
    collagename =" iit patana"
    def setData(self,rollno,name):
        self.rollno=rollno
        self.name=name

    def displayData(self):
        print(f"rollno={self.rollno}")
        print(f"name={self.name}")
        print(f"collagename{self.collagename}")

s1=student()
s1.setData(1001,"advi")
s1.displayData()

s2=student()
s2.setData(1002,"ganu")
s2.collagename ="vjit nashik"
s2.displayData()

