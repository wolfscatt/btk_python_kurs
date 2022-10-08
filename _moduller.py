# ------------------- DateTime Modülü -------------------
from datetime import date, datetime
# # birthday = '9 April 2002 hour 12:15:13'
# # result = datetime.strptime(birthday,'%d %B %Y hour %H:%M:%S')
# # simdi = datetime.now()
# birthday = datetime(2002,4,9,12,30,13)
# result = datetime.timestamp(birthday)    # Verdiğimiz tarih bilgisini saniyeye çevirir 1970'ten itibaren geçen saniye
# result = datetime.fromtimestamp(0)       # Bilgisayarların milat bilgisi sayılan tarihi getirir. 1970 yılı
# print(result)


# ------------------- OS(İşletim Sistemi) Modülü -------------------
import os
# Dizin değiştirme
# os.chdir('C:\\')   # Dizin değiştirme metodu normalde bu dosyanın bulunduğu dizindeydi ama şuan yazdığımız dizinde.
# os.chdir('..')     # Direkt bir üst dizine geçer

# Klasör oluşturma
# os.mkdir("newdirectory")    # newdirectory isminde bir klasör oluşturur.

# Etkin dizini öğrenme
# result = os.getcwd()

# Listeleme
# result = os.listdir()

# Dosya hakkında bilgi alma
# result = os.stat("moduller.py")
# result = datetime.fromtimestamp(result.st_ctime)     # Dosyanın oluşturulma zamanı normalde saniye cinsinden veriliyordu biz fromtimestamp metodu sayesinde gün ay yıl saat şeklinde alabildik.
# result = os.rename('moduller.py','_moduller.py')       # Dosya ismi değiştirme

# Path
# result = os.path.abspath('_moduller.py')       # Dosya uzantısını verir.
# result = os.path.dirname("C:/Users/pc/Desktop/python/_moduller.py")      # Dosyanın yolunu üst klasörlerini verir
# print(result)


# ------------------- Regular Expression Modülü -------------------
import re

str = "Python Kursu: Python Programlama Rehberiniz 40 Saat"
# result = re.findall("Python",str)
# result = re.split(" ",str)
# result = re.sub(" ","-",str)
# result = re.sub("\s","-",str)      # "\s" boşluk karakteri anlamına geliyor 
# result = re.search("Python",str)
# result = result.span()


# ------------------- JSON Modülü -------------------
import json

person_str = '{"name":"Burcu","Languages":["Python","C#"]}'
person_dict = {"name":"Burcu","Languages":["Python","C#"]}

# JSON string to Dictionary
# result = json.loads(person_str)         # loads metodu string, byte gibi ifadeleri okurken kullanılıyor.
# result = result["name"]                 # loads metodu json string'ini dict objesine çeviriyor.
# print(type(result))
# print(result)

# with open("person.json") as file:
#     result = json.load(file)             # load metodu json formatında dosyayı dictionary formatına çeviriyor.
#     print(type(result))
#     print(result["name"])

# Dict to JSON string
# result = json.dumps(person_dict)         # dumps metodu dict olarak gelen bir objeyi json string'ini çeviriyor.
# print(type(result))
# print(result)

# with open("person.json","w") as file:
#     json.dump(person_dict,file)            # dump metodu dict objesini json dosyasına yazmamızı sağlıyor.

personDict = json.loads(person_str)
result = json.dumps(personDict,indent=3,sort_keys=True)
print(personDict)
print(result)
