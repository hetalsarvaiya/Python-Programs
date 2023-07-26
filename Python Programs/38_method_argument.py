class myclass:
    a=10
    b=20

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self,a,b):
        print(self.a+a+self.b+b)

myobj = myclass(50,50)
myobj.add(100,100)