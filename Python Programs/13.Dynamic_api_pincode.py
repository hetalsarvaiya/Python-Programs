import requests

url1 = "https://api.postalpincode.in/pincode/"
url2 = input("enter the Pincode : ")
url = requests.get(url1+url2)
mydata = url.json()

for i in range(0,len(mydata)):
    print(mydata[i]["PostOffice"])


#Pincode_information = json.loads(url.text)
#necessary_info = Pincode_information[0]["PostOffice"][0]
#for key,value in necessary_info.items():
#   print(f"{key} : {value}")