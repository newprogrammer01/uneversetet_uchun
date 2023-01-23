"""BOSCH va PHILIPS konsernlari tomonidan ishlab chiqilgan 
mahsulot nomlaridan tashkil topgan ikkita ro’yxat berilgan. 
Har ikkala 
firma tomonidan ishlab chiqilgan bir xil mahsulotlar ro’yxati tuzilsin.  
"""
list=[]
BOSCH=['kitob','daftar','ruchka','qalam','marker','bloknot','aksisuarlar']

PHILIPS=['Xaritalar','Doskalar','printer','marker','daftar','soat','qalam']
if BOSCH[3]==PHILIPS[6]:

   list.append(BOSCH[3])
print(list) #['qalam']