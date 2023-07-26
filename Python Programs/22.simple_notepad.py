file=open("first program.txt","r")

data=file.read()
print(data)

ltrcount=0
validcount=0
other=0

for i in range(0,len(data)):
    if ord(data[i])>=65 and ord(data[i])<=90:
        ltrcount=ltrcount+1
    elif ord(data[i])>=97 and ord(data[i])<=122:
        ltrcount=ltrcount+1
    elif ord(data[i])==32 or ord(data[i])==46 or ord(data[i])==44:
        validcount=validcount+1
    else:
        other=other+1

if other>=1:
    print("This paragraph is not valid")
else:
    print("this paragraph is valid")