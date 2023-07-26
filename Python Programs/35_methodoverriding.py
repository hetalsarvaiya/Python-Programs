class first:
    a = 10
    b = 20

    def msg(self):
        print("first class msg printed")

class second(first):
    c = 30
    d = 40

    def msg(self):
        print("second class msg printed")

secondobj = second()
secondobj.msg()