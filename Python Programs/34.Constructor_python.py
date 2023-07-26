class myclass:
    a = 10
    b = 20

    def __init__(self,f,s):
        self.a = f
        self.b = s
    def additon(self):
        print("addition of ",self.a,"and",self.b,"is : ",self.a+self.b)

myobj = myclass(100,200)
myobj.additon()