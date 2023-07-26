from matplotlib import pyplot as plt

price = [229,212,215.20,214]
time = ["9:15","9:16","9:17","9:18"]

plt.xlabel("TIME")
plt.ylabel("PRICE")
plt.title("Realince share")
plt.plot(time,price,color="b")
plt.show()