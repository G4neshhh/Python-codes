class time:
    def __init__(self,hour=0,min=0):
        self.hour=hour
        self.min=min

    def display(self):   
            print(f"hour is ={self.hour}and min ={self.min}")

    def addtime(self,t1,t2):
            self.hour=t1.hour+t2.hour
            self.min=t1.min+t2.min
            if t3.min>60:
                t3.min-=60
                t3.hour=t3.hour+1


t1=time(4,50)
t2=time(5,40)
t3=time()


t3.addtime(t1,t2)
t3.display() 