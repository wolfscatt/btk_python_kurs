# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# Kullanımı: open(dosya_yolu, dosya_erişim_modu)

# ------------------- Dosya Erişim Modları -------------------
# "w": (Write) yazma modu. Dosyayı oluşturur ve üzerine yazar veriler varsa siler.
# file = open("newFile","w")   # Dosyayı şuan mevcut dizinde yazma modunda oluşturur

# "a": (Append) ekleme modu. Dosya konumda yoksa oluşturur ve üzerinde veriler varsa da altına bizim gönderdiğimiz verileri eklemeye devam eder.
# file = open("appendFile","a")    # Dosyayı mevcut dizinde ekleme modunda oluşturur.

# "x": (Create) oluşturma modu. Dosya zaten mevcutsa hata verir.
# file = open("newFile","x")    # 6. satırdaki kod çalıştırılır ve "newFile" dosyası oluşturulursa bu satırdaki kod hata verir.

# "r": (Read) okuma modu. Dosya konumda yoksa hata verir okuyamaz.
# file = open("readFile","r")   # Böyle bir dosya dizinde bulunmadığından hata verir.
# content = file.read()         # bu satır bütün dosya içeriğini okur
# content = file.readline()     # bu satır dosyadaki tek bir satırı okur
# content = file.readlines()    # bu satır dosyadaki bütün satırları bir liste elemanı olarak atar.

# Dosya Güncelleme işlemi dosyayı "r+" modunda açarak yapılır. Dosyanın direkt başına gönderdiğimiz kelimeleri yazar.



