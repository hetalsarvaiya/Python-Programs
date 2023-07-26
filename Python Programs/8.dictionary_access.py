mydata = {"maharastra":{"mumbai":{"city":"metrocity","metrotrain":"yes"},"population":"3 cr"},
          "gujarat":["ahemdabad","surat","rajkot"],
          "rajsthan":["ajmer","jaislmer",{"capital":"jaipur"},["mewad","rj","inr"]]}

print(mydata["maharastra"]['mumbai']['city'])
print(mydata["rajsthan"][1])
print(mydata["gujarat"][2])
print(mydata["rajsthan"][3][1])
print(mydata["rajsthan"][2]['capital'])