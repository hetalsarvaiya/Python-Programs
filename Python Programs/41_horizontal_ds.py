from matplotlib import pyplot as plt

mydata = {"cases":[100,200,50,70],"cities":["ahemdabad","surat","rajkot","vadodara"],
           "info":[{"date":"12 june 2023","state":"gujarat","time":" 10:20 PM"}]}

city = mydata["cities"]
case = mydata["cases"]

plt.xlabel("Cities Of Gujarat")
plt.ylabel("Cases Of Gujarat")
plt.title("Gujarat covid cases "+(mydata["info"][0]["date"])+(mydata["info"][0]["time"]))
plt.barh(city,case,color='r')
plt.show()