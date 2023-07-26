class grandfather:
    a = 10
    b = 20
    def grandfathermethod(self):
        print("garandfather method called")
    def garandfather1method(self):
        print("called for grandfaher")

class grandmother:
    c = 30
    d = 40
    def grandmothermethod(self):
        print("garandmother method called")
    def garandmother1method(self):
        print("called for grandmother")

class father(grandfather,grandmother):
    e = 50
    f = 60
    def fathermethod(self):
        print("father method called")
    def faher1method(self):
        print("called for father")

class mother:
    g = 70
    h = 80
    def mothermethod(self):
        print("mother method called")
    def mother1method(self):
        print("called for mother")
class child(father,mother):
     x = 90
     y = 100
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
print(myobj.g)
print(myobj.h)
print(myobj.x)
print(myobj.y)
myobj.grandfathermethod()
myobj.garandfather1method()
myobj.grandmothermethod()
myobj.garandmother1method()
myobj.fathermethod()
myobj.faher1method()
myobj.mothermethod()
myobj.mother1method()
myobj.childmethod()
myobj.child1method()