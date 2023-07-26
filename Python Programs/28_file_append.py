file = open("forth.txt","a")

userdata = input("enter data to write in file : ")
file.write(userdata)
print("data written successfully")

file.close()

file = open("forth.txt","r")
data = file.read()
print(data)