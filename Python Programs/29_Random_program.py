import random2

userno = int(input("enter the no 1,100: "))
luckyno = random2.randint(1,100)

if userno == luckyno:
    print("congratulations")
else:
    print("better luck next time , lucky no is : ",luckyno)


