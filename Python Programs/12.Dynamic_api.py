import requests

url1 = "https://inshorts.deta.dev/news?category="
url2 = input("enter the category : ")
url = requests.get(url1+url2)
mydata = url.json()

for i in range(0,len(mydata["data"])):
    print(mydata["data"][i]["title"])
