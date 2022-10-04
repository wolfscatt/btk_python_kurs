import re
from unittest import result
import random
  
""" 
list = [1,2,5,3,6]
website ="http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

leng_course = len(course)
result = course[::-1]   # String dizinisi tersten yazdırma
website_karakter = website[-3:]
result = bool(website.find('com'))

result = list.pop(2)

# numbers = [x for x in range(13)]
numbers = [x for x in range(13) if x%3==0]   # ÇOOOOOK GÜZEL BİR YÖNTEM

numbers2 = []
for x in range(13):
    if (x%3==0):
     numbers2.append(x)
print(numbers2)

#print(numbers)

 
# isimler = ['Oğuzhan', 'Enes', 'Selim']
# for index, isim in enumerate(isimler, start=1):
#   print(index, isim)
# print(result)
# print(website_karakter)
# print(f"Course String'i Uzunluğu: {leng_course}")
"""

# ------------------- Sayı Tahmin Oyunu --------------------
r = random.randint(1,100)
can = int(input("Sayı Tahmin Oyunu İçin Hak Sayınızı Giriniz: "))
hak = can
print(f"Rastgele Oluşturulan Sayıyı Tahmin Etmek İçin {hak} Hakkınız Vardır.")
puan = 100
kacıncı_hak = 0
while hak >-1 : 
    hak -= 1
    kacıncı_hak += 1
    tahmin = int(input("Tahmininizi Giriniz: "))
    if(tahmin<r):
        print(f"Daha Yüksek sayılar tahmin ediniz. {hak} hakkınız kaldı.")
    if(tahmin>r):
        print(f"Daha Küçük sayılar tahmin ediniz. {hak} hakkınız kaldı.")
    if(tahmin==r):
        print(f"Tebrikler {kacıncı_hak}. hakkınızda sayıyı tahmin ettiniz. Ve aldığınız puan: {puan - (puan/can)*(kacıncı_hak-1)}")
        break
    elif (hak==0):
        print("Hakkınız bitmiştir! Oyunu Kaybettiniz.")
        


