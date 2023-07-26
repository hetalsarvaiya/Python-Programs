digitcount = 0

mobno = input("enter mobile no : ")

if len(mobno)==10:
    for i in range(0,len(mobno)):
        if ord(mobno[i])>=48 and ord(mobno[i])<=57:
            digitcount = digitcount + 1
    if digitcount==10:
       if ord(mobno[0]) == 57 or ord(mobno[0]) == 56 or ord(mobno[0]) == 55 or ord(mobno[0]) == 54:
          print("valid mobile no")
       else:
          print("first digit must be 6 or 7 or 8 or 9")
    else:
        print("all must be digits")
else:
    print("enter the number 10 digit")

