try:
    file = open("second.txt", "r")
except FileNotFoundError:
    print("file is missing")