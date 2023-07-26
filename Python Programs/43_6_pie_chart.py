from matplotlib import pyplot as plt
Gujrat=["ahemdabad","surat","rajkot","vapi","gandhinagar"]
G_cases=[110,15,50,63,85]

MP=["Gwalior","Bhopal","Indore","Jabalpur","Sagar"]
MP_cases=[150,60,80,90,30]

UP=["Kanpur","Ghaziabad","Lucknow","Agra","Ayodhya"]
UP_cases=[100,50,30,80,35]

Punjab=["Lahore","Rawalpindi","Faisalabad","Gujranwala","Firozpur"]
P_cases=[50,60,80,90,200]

Rajsthan=["Jaipur","Kota","Jodhpur","Bikaner","Udaypur"]
R_cases=[68,43,90,50,30]

Zarkhand=["Ranchi","Deoghar","Jamshedpur","Hazaribagh","Ramgarh"]
Z_cases=[63,89,55,14,70]

plt.subplot(2,3,1)
plt.pie(G_cases,autopct="%.2f",labels=Gujrat)
plt.title("Gujarat covid cases")
plt.legend()

plt.subplot(2,3,2)
plt.pie(MP_cases,autopct="%.2f",labels=MP)
plt.title("MP covid cases")
plt.legend()

plt.subplot(2,3,3)
plt.pie(UP_cases,autopct="%.2f",labels=UP)
plt.title("UP covid cases")
plt.legend()

plt.subplot(2,3,4)
plt.pie(P_cases,autopct="%.2f",labels=Punjab)
plt.title("Punjab covid cases")
plt.legend()

plt.subplot(2,3,5)
plt.pie(R_cases,autopct="%.2f",labels=Rajsthan)
plt.title("Rajsthan covid cases")
plt.legend()

plt.subplot(2,3,6)
plt.pie(Z_cases,autopct="%.2f",labels=Zarkhand)
plt.title("Zarkhand covid cases")
plt.legend()
plt.suptitle("statewise cities cases")
plt.show()



