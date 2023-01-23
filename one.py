"""Muvozanatlashgan T daraxtni hosil qiling, uni 
(binar) daraxt ko’rinishida ekranga chop qiling va:
- berilgan daraxtdagi qiymati juft son bo’lgan 
tugunlarni olib tashlang;
- hosil bo’lgan daraxtdagi barg tugunlari sonini
 aniqlang va ularning qiymatlarini chiqaring."""

def main(l):
    list=[]
    for i in range(1,len(l)+1):
        
        if i%2==1:
         list.append(i)
    return list
print(main([1,2,3,4,5,6,7,8,9,10]))
#[1, 3, 5, 7, 9]