class grandparent:
    a = 10
    b = 20
    def grandparentmethod(self):
        print("garandparent method called")
    def garandparent1method(self):
        print("called for grandparent")

class parent(grandparent):
    c = 30
    d = 40
    def parentmethod(self):
        print("parent method called")
    def parent1method(self):
        print("called for parent")
class child(parent):
     e = 50
     f = 60
     def childmethod(self):
        print("child method called")
     def child1method(self):
        print("called for child")

myobj = child()
print(myobj.a)
print(myobj.b)
print(myobj.c)
print(myobj.d)
print(myobj.e)
print(myobj.f)
myobj.grandparentmethod()
myobj.garandparent1method()
myobj.parentmethod()
myobj.parent1method()
myobj.childmethod()
myobj.child1method()