mystring = "hello"

for i in mystring:
    print(i)

print("total no of characters : ",len(mystring))
print(mystring[0])

for i in range(0,len(mystring)):
    print(mystring[i])

password=input("enter password : ")
if len(password)>=8 and len(password)<=12:
    print("valid")
else:
    print("not valid")