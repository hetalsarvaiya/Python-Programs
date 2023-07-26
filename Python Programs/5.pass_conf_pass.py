password=(input("Enter the password : "))
Retypepassword=(input("Enter the Re-Enterpassword :"))
if password=="" or Retypepassword=="":
    if password=="" and Retypepassword!="":
        print("password can not be blank")
    elif password!="" and Retypepassword=="":
        print("Retypepassword can not be blank")
    else:
        print("Field can not be blank")
else:
    if password=="hetal@123" and Retypepassword=="hetal@123":
        print("Correct password and login")
    else:
        print("please enter correct password")