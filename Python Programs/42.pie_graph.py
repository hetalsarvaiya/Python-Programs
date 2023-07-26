from matplotlib import pyplot as plt

branches = ["CE", "IT", "EC", "IC", "EE"]
seats = [170, 110, 35, 23, 10]
color = ["pink", "blue", "yellow", "red", "green"]

plt.subplot(1,2,1)
plt.pie(seats, labels=branches, autopct="%.2f", colors=color)
plt.legend()
plt.title("Clg1")

branches1 = ["CE", "IT", "EC", "IC", "EE"]
seats1 = [100, 125, 70, 33, 20]
color = ["pink", "blue", "yellow", "red", "green"]

plt.subplot(1,2,2)
plt.pie(seats1, labels=branches1, autopct="%.2f", colors=color)
plt.title("Clg2")
plt.legend()
plt.show()
