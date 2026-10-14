class height:
    def __init__(self,feet=0,inch=0):
        self.feet=feet
        self.inch=inch

    def displya(self):
        print(f"height feet is ={self.feet} and inch={self.inch}")

    def addheight(self,h2):
        temp=height()
        temp.feet=self.feet+h2.feet
        temp.inch=self.inch+h2.inch
        if temp.inch>=12:
            temp.inch-=12
            temp.feet+=1
        return temp

h1=height (5,8)
h2=height (9,11)
h3=height()
h3= h1.addheight(h2)
h3.displya()


