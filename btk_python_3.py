# Error -> Hata

# Error Handling  -> Hata Yakalama
 
 
# try: 
#     x = int(input('x:'))
#     y = int(input('y:'))
#     print(x/y)
# except ZeroDivisionError as ex:
#     print('y için 0 giremezsiniz')
#     print(ex)
# except ValueError:
#     print('x ve y için sayısal değerler girmelisiniz.')

# while True:
#     try:
#         x = int(input('x:'))
#         y = int(input('y:'))
#         print(x/y)
#     except Exception as ex:
#         print('yanlış bilgi girdiniz', ex)
#     else:
#         break


# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Parola En az 7 karakter içermelidir.")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola Küçük harf içermelidir.")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Parola Büyük harf içermelidir.")
#     elif not re.search("[0-9]",psw):
#         raise Exception("Parola rakam içermelidir.")
#     elif not re.search("[_#$%]",psw):
#         raise Exception("Parola alpha numeric karakterler içermelidir.")
#     elif re.search("\s",psw):
#         raise Exception("Parola Boşluk içermemelidir")
#     else:
#         print("Geçerli Parola")

# password = '1234567Aa_'

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# finally:
#     print("Validation Okey")


class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception("Name Bilgisi fazla karakter içeriyor")
        else:
            self.name = name

p = Person('Ömerrrrrrrrrrr', 1996)