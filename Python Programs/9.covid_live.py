#pip install requests

import requests

url = requests.get("https://data.covid19india.org/data.json")
mydata = url.json()

print(mydata)
print(mydata["cases_time_series"][0]["date"])

print("total no of case_time_series days : ",len(mydata["cases_time_series"]))
print("total no of statewise days : ",len(mydata["statewise"]))
print("total no of tested days : ",len(mydata["tested"]))

for i in mydata:
    print(i)

for i in range(0,len(mydata["cases_time_series"])):
    print(mydata["cases_time_series"][i]["date"])



