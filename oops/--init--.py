class student():
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
        print("constructor called ")

    def displayData(self):
        print(f"rollno is {self.rollno}")
        print(f"student name is {self.name}")

    def __del__(self):
    
        print("discustractor")


rollno=input("enter a roll number of student; ")
name=input("enter a valid name: ")

s1=student(22,"ganu")
s1.displayData()

s2=student(rollno,name)
s2.displayData()
del s2
