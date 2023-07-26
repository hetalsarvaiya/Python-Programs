def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*i
    return fact
num=int(input("enter the no :"))
x=factorial(num)
print("factorial num is : ",x)

