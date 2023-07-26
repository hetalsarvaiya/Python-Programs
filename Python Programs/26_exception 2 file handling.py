file = open("first program.txt","r")
data = file.read()

file = open("second.txt","r")
data1 = file.read()

print(data+" ** "+data1)

try:
    open("first program.txt","r")
    open("second.txt","r")
except FileNotFoundError:
    print("file not found")
except FileNotFoundError:
    print("file not found")

