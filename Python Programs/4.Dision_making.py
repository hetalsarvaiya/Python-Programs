email=(input("Enter the email : "))
password=(input("Enter the password : "))

if email=="" or password=="":
   if email=="" and password !="":
      print("email can not be blank")
   elif email!="" and password=="":
       print("password can not be blank")
   else:
       print("field can not be blank")
else:
    if email == "hetu.com" and password == "hetal@123":
        print("login success")
    else:
        print("Invalid username and password")

