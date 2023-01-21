(1)
"""Mahsulot nomlaridan tashkil topgan ro’yxat berilgan.
Ro’yxat elementlaridagi SONY firmasida ishlab chiqilgan 
mahsulotlardan tashkil topgan yangi ro’yxat yarating."""



list=['PS2','PS3','PSP','Kontrolleri','DualShock3 kontrolleri','PlayStation Move kontrolleri',
'WM-F5 "Okinawa" sport Walkmani','WM-F404, televizor tyunerli yuqori darajadagi model (1990-yil)',
'1990-yillarning boshidagi "Sport" Walkman modeli','Sony Walkman WM-EX194 (2004-yil)'
]
SONY=[]
SONY.append(list)
print(SONY)

"""answer=[['PS2', 'PS3', 'PSP', 'Kontrolleri', 'DualShock3 kontrolleri', 
'PlayStation Move kontrolleri', 'WM-F5 "Okinawa" sport Walkmani', 
'WM-F404, televizor tyunerli yuqori darajadagi model (1990-yil)', 
'1990-yillarning boshidagi "Sport" Walkman modeli', 
'Sony Walkman WM-EX194 (2004-yil)']]"""

(2)
"""Guruh talabalarini olgan baholari bo’yicha (beshliklar, to’rtliklar, uchliklar) 
yangi ro’yxatini navbat (FIFO) qoidasi asosida shakllantiring?"""

import queue
q1 = queue.Queue(4) #The max size is 5.
q1.put('Pirnazarov Jasur')
q1.put('Jurayev Kamronbek')
q1.put("Eshqobilov Kamoliddin")
q1.put("Yarashov Eldorjon")
print(q1.full()) # will return true.
q2=queue.Queue(2)
q2.put('Yuldoshov Asliddin')
q2.put("Salohhiddinov Fayozbek")
print(q2.full())
q3=queue.Queue(1)
q3.put('Pirnazarov Jasurbek')

print(q3.full()) #will return true
