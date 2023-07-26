digitcount = 0
capitalcount = 0

char = [0,1,4,5]
digit = [2,3,6,7,8,9]

numberplat = input("enter number plat no : ")

if len(numberplat)==10:
    for i in digit:
        if ord(numberplat[i])>=48 and ord(numberplat[i])<=57:
            digitcount = digitcount + 1
    for i in char:
        if ord(numberplat[i])>=65 and ord(numberplat[i])<=90:
            capitalcount = capitalcount + 1
    if capitalcount==4 and digitcount==6:
        print("valid number plate")
    else:
        print("Invalid number plate")
else:
    print("Invalid number plate")

