liste = ["1","2","5a","10b","abc","13","53"]

# for i in liste:
#     try:
#         result = int(i)
#         print(result)      
#     except ValueError:
#         print(f"{i} Sayıya Çevrilemedi")
#         continue

# while True:  
#     sayi = input('Sayı Giriniz: ')
#     if sayi == 'q':
#          break
#     try:
#         result = int(sayi)
#         print('Girdiğiniz Sayı: ', result)
#         break
#     except ValueError:
#         print("Geçersin sayı")
#         continue

# def check_password(parola):
#     turkce_karakterler = 'şçıöüğİ'
#     for i in parola:
#         if i in turkce_karakterler:
#             raise Exception("Parola Türkçe Karakterler İçeremez")
#         else:
#             pass
#     print("Geçerli Parola")

# parola = input("Parolan Giriniz:")
# try:
#     check_password(parola)
# except Exception as err:
#     print(err)

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif Sayı")

    result = 1
    for i in range(1,x+1):
        result *= i
    return result

sayilar = [4,5,9,13,-5,'13b']
for k in sayilar:
    try:
        y = faktoriyel(k)
    except ValueError as err:
        print(err)
        continue
    print(y)

