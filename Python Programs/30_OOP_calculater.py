class calc:
    a=10
    b=20

    def add(self):
        print("addition of",self.a,"and",self.b,"is : ",self.a+self.b)
    def sub(self):
        print("substraction of",self.a,"and",self.b, "is : ",self.a-self.b)
    def mul(self):
        print("Multiplication of",self.a,"and",self.b,"is : ", self.a*self.b)
    def div(self):
        print("division of",self.a,"and",self.b, "is : ", self.a/self.b)

myobj = calc()
myobj.add()
myobj.sub()
myobj.mul()
myobj.div()
