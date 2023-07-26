num=int(input("Enter the number : "))

for i in range(1,101):
    if num == i:
        print("valid number")
        break
else:
    print("Invalid number")