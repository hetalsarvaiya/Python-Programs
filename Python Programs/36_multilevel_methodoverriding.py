class grandparent:
    a = 10
    b = 20
    def msg(self):
        print("garandparent method called")

class parent(grandparent):
    c = 30
    d = 40
    def msg(self):
        print("parent method called")
class child(parent):
     e = 50
     f = 60
     def msg(self):
        print("child method called")

myobj = child()
myobj.msg()