# def greetings(name):
#     print(f"Hello {name}")

# greetings("ömer")
# print(greetings)
# sayHello = greetings   # Her iki fonksiyonunda adresi eşitlendi

# print(sayHello)

# Encapsulation
# def outer(num1):
#     print("Outer " , num1)
#     def inner_increment(num1):
#         print("İnner " , num1)
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num2)

# outer(13)


# def factoriel(number):
#     if not isinstance(number,int):
#         raise TypeError("Bir sayı giriniz.")
#     if number <=0:
#         raise ValueError("Negatif Sayıların Faktoriyeli Hesaplanamaz")
#     def inner_factoriel(number):
#         if number <= 1:
#             return 1
#         return number * inner_factoriel(number - 1)    # Recursive yapı
#     return inner_factoriel(number)

# try:
#     f1 = factoriel(4)
#     print(f1)
# except Exception as ex:
#     print(ex)


# --------------- Fonksiyondan geriye fonksiyon döndürmek ---------------
# def usalma(number):
#     def inner(power):
#         return number**power
#     return inner

# two = usalma(2)   # burada two değişkeni de bir fonksiyon olarak kullanılır
# two_ussu_four = two(4)    # görüldüğü gibi two değişkeni de bir method gibi kullanıldı.
# print(two_ussu_four)

# --------------- Fonksiyonları Parametre Olarak Göndermek ---------------
# def toplama(a,b):
#     return a+b
# def cikarma(a,b):
#     return a-b
# def carpma(a,b):
#     return a*b
# def bolme(a,b):
#     return a/b

# def islem(f1,f2,f3,f4,islem_secimi):
#     if islem_secimi == 'toplama':
#         print(f1)
#     elif islem_secimi == 'çıkarma':
#         print(f2(13,9))
#     elif islem_secimi == 'çarpma':
#         print(f3(4,9))
#     elif islem_secimi == 'bölme':
#         print(f4(53,13))
#     else:
#         print("Geçersiz İşlem")

# islem(toplama(13,9),cikarma,carpma,bolme,"toplama")
# islem(toplama(13,9),cikarma,carpma,bolme,"çıkarma")
# islem(toplama(13,9),cikarma,carpma,bolme,"çarpma")
# islem(toplama(13,9),cikarma,carpma,bolme,"bölme")
# islem(toplama(13,9),cikarma,carpma,bolme,"Burcu")


# --------------- Decorator Fonksiyon ---------------
# C# da gördüğümüz Aspect benzeri bir uygulama zannediyorum 

# def my_decorator(func):
#     def wrapper():
#         print("Fonksiyondan Önceki İşlemler")
#         func()
#         print("Fonksiyondan Sonraki İşlemler")
#     return wrapper

# @my_decorator        # 95. satırda yaptığımız işlemi yapıyor aslında
# def sayHello():
#     print("Hello")
# def sayGreeting():
#     print("Greetings")

# # sayHello = my_decorator(sayHello)
# sayHello()

# import math
# import time

# def calculate_time(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         time.sleep(1)
#         func(*args, **kwargs)
#         finish = time.time()
#         print("Fonksiyon "+ func.__name__ +" "+ str(finish-start)+ " saniye sürdü")
#     return inner

# @calculate_time
# def usalma(a,b):
#     print(math.pow(a,b))
    
# @calculate_time
# def faktoriyel(num):   
#     print(math.factorial(num))

# usalma(3,3)
# faktoriyel(5)


# For Döngüsünün içerisinde geçen olay ------ Iterators ------

# liste = [1,2,3,5,6]
# iterator = iter(liste)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break
 
 
# Iterative nesne  
# class MyNumbers:
#     def __init__(self,start,stop):
#         self.start = start
#         self.stop = stop
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start <= self.stop:
#             x = self.start
#             self.start += 1
#             return x
#         else:
#             raise StopIteration
        
# list = MyNumbers(13,20)
# iterator = iter(list)
# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except:
#         break

# for x in list:
#     print(x)


# ------------- Generator -------------
# Liste için bellek üzerinde bir yer ayırıyor. Biz sadece listeyi ekranda göstermek için böyle bir maliyete girmemize gerek yok.
# def cube():
#     liste = []
#     for i in range(5):
#         liste.append(i**3)
#     return liste
# print(cube())

# yield anahtar kelimesi ile yukarıda yapacağımız işlemi tek seferlik yapabiliyoruz. Bu bize bir generator objesi dönüyor.
# def cube():
#     for i in range(5):
#         yield i**3

# iterator = cube()
# #iterator = iter(generator)   # Bu satıra aslında gerek yok generator iterator olan nesne kendi içerisinde itere çeviriyor.

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break
    

generatorListe = (i**3 for i in range(4))      # Köşeli parantez yaptığımızda bellekte bir liste oluşuyor ve elemanları o listeye atıyor. Ama normal parantez kullandığımızda generator çalışıyor.
while True:
    try:
        print(next(generatorListe))
    except StopIteration:
        break