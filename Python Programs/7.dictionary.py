#key (left) = value (right)  {} = disctionary , []=value ()=perenthisis
#to access value key required

mydata = {"gujarat":"ahemdabad"}
print(mydata["gujarat"])

mydata2 = {"ahemdabad":200,"surat":300,"rajkot":300}
print(mydata2["rajkot"]+mydata2["surat"]+mydata2["ahemdabad"])

mydata3 = {"ahemdabad":200,"surat":300,"rajkot":[150,300,0]}
print(mydata3["rajkot"][2])

mydata4 = {"ahemdabad":[{"date":"1 may 2023","cases":75},
                        {"date":"2 may 2023","cases":175},
                        {"date":"3 may 2023","cases":[275,500,0]}],
                        "surat":300, "rajkot":[150,300,0]}
print(mydata4["ahemdabad"][1]['cases'])
print(mydata4["ahemdabad"][2]['cases'][1])