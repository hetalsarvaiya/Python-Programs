import datetime

date = datetime.datetime.now()
d = date.day
mn = date.month

if d==25 and mn==12:
    print("Xmas sale flat 50% off")

if d==14 and mn==11:
    print("happy teachers day")

if d=="Thursday" and d=="Friday":
    print("Buy one get one free")

a = date.strftime("%A") # name of day long

if a=="Thursday" or a=="Friday":
    print("buy one get one free")

a = date.strftime("%A")
b = date.strftime("%I")
c = date.strftime("%p")

if a=="Thurday" and c=="PM":
    if b=="3" or b<="4":
        print("Happy hours,Extra 25% off")

if c=="AM":
    if b=="10" or b<="12":
        print("Morning show flat 99/-")
