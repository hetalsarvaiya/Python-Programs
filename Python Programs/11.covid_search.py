import requests

url = requests.get("https://data.covid19india.org/data.json")
mydata = url.json()

for i in mydata:
    print(i)

date = input("enter the date : ")
for i in range(0,len(mydata["case_time_series"])):
    if date == mydata["case_time_series"][i]["date"]:
        print("date found")
        print(mydata[i]["case_time_series"][i])
        print("new case : ",mydata["cases_time_series"][i]["dailyconfirmed"])
        break
else:
    print("date not found")
