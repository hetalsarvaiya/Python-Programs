digitcount = 0
capitalcount = 0
specialcount = 0
smallcount = 0

email = input("enter the email : ")

for i in range(0,len(email)):
        if(email[-4]=="."):
            if ord(email[i]) >= 65 and ord(email[i]) <= 90:
              capitalcount = capitalcount + 1

            elif ord(email[i]) >= 48 and ord(email[i]) <= 57:
              digitcount = digitcount + 1

            elif ord(email[i]) == 97 and ord(email[i]) == 122:
              smallcount = smallcount + 1

            elif ord(email[i]) == 46 and ord(email[i]) == 64:
              specialcount = specialcount + 1

        else:
            print("please enter contain must be dot before com")
            break
        if ("@" in email) and (email.count("@")==1):
           print("Valid email")
           break
        else:
            print("please enter @ atleast 1time")
            break



