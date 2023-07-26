class grandfather:
    a = 10
    b = 20
    def msg(self):
        print("garandfather method called")


class grandmother:
    c = 30
    d = 40
    def msg(self):
        print("garandmother method called")

class father(grandfather,grandmother):
    e = 50
    f = 60
    def msg(self):
        print("father method called")

class mother:
    g = 70
    h = 80
    def msg(self):
        print("mother method called")

class child(father,mother):
     x = 90
     y = 100
     def msg(self):
        print("child method called")


myobj = child()
myobj.msg()