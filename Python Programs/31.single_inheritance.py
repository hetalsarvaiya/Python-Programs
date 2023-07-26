class parent:
    a=10
    b=20

    def parentmethod(self):
        print("parent method called")

class child(parent):
    c=30
    d=40

    def childmethod(self):
        print("child method called")

myobj = child()
print(myobj.a)
print(myobj.b)
print(myobj.c)
print(myobj.d)
myobj.parentmethod()
myobj.childmethod()
