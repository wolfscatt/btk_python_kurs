# ------------------- Function -------------------
from numpy import square
 
 
def sayHello(name):
    ''' 
    DOCSTRİNG: Fonksiyona Girilen İsme Göre Önüne Hello Ekleyerek geri dönüş yapan program
    INPUT: name
    OUTPUT: "Hello" + name
    '''
    return "Hello "+ name
msg=sayHello("Ömer")
#print(msg)
#print(help(sayHello)) # help metodu fonksiyondan bilgi almak için kullanılır

# def add(a,b,c = 0):
#     return sum((a,b,c))      # belirttiğimiz sayıda parametre göndererek toplama yapar
# print(add(13,53))

# def add(*params):              # *params bir tuple listesi döner. eğer **params yapsak bir dictionary dönerdi.
#     print(type(params))
#     return sum((params))       # *params sayesinde istediğimiz kadar parametre gönderebiliriz.
# print(add(10,23,51,21))

# def displayUser(**args):
#     print(type(args))
#     for key,value in args.items():
#         print('{} is {} '.format(key,value))

# displayUser(name = 'Ömer', age = 21, phone = '5536972626')
# displayUser(name = 'Burcu', age = 26, job = 'Civil Engineering', phone = '5536972626')


# def myFunc(a,b,*args,**kwargs):    # **kwargs: Key Word Arguments
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)

# myFunc(13,9,53,11,key1 = 'value1', key2 = 'value2')

# def square(num): return num**2

numbers = [2,3,4,7]

square = lambda num: num**2       # lambda expression = lambda ifadesi isimsiz bir fonksiyon oluşturabiliyoruz

# result = list(map(lambda num: num**2,numbers))
# result = list(map(square,numbers))
result = list(filter(lambda num: num%2==0,numbers))    # numbers listesindeki çift sayıları filter metodu sayesinde almış olduk

# for i in map(square,numbers):
#     print(i)

print(result)
