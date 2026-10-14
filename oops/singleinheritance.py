class areatest:
    def __init__ (self,l,b):
        self.l=l
        self.b=b
        print("area consutructors called: ")

    def area (self):
        ar=(self.l*self.b)
        return ar
class volumetest (areatest):
    def __init__(self,l,b,h):         
        self.h=h
        areatest.__init__(self,l,b)             #in that case wee using the above class just 
                                                #call in other class that is  single inheritance
        print("calling to a area conctractor ")
    def volume(self):
        vol=(self.l*self.b*self.h)
        return vol

vob1=volumetest(7,6,3)
v1=vob1.volume()
a1=vob1.area()                       
print(f"area of circle is {a1}")
print(f"volume of the circle is , {v1}")





are1=areatest(8,9)
ar1=are1.area()
print(f"the area of circle is {ar1}")
