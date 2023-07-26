name = "hetal"
num1 = int(input("enter the 1st no :"))
num2 = int(input("enter the 2nd no :"))
try:
   print(name)
   print(num1/num2)
   open("second.txt","r")
except NameError:
    print("variable not declare")
except ZeroDivisionError:
    print("not divided by zero")
except FileNotFoundError:
    print("file is missing")
