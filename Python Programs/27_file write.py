file = open("third.txt","w")

userdata = input("enter data to write in file : ")
file.write(userdata)
print("data written successfully")

file.close()

file = open("third.txt","r")
data = file.read()
print(data)