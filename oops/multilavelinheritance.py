
class areatest:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        ar=self.l*self.b
        return ar

class volumetest(areatest):
    def __init__(self,l,b,h):
        self.h=h

        areatest.__init__(self,l,b)
        print("area constractor  ")
    def volume(self):
        vol=self.l*self.b*self.h
        return vol 

class densitytest(volumetest):
    def __init__(self, l, b, h,m):
        self.m=m
        volumetest.__init__(self,l,b,h)

    def density1(self):
        v=self.l*self.b*self.h
        d=self.m/v
        return d


den=densitytest(6,8,10,2000)
deob=den.density1()
print(f"density is {deob} ")

v1=den.volume()
a1=den.area()                       
print(f"area of circle is {a1}")
print(f"volume of the circle is , {v1}")   
        


