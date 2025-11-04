#Değişken tanımlama Kuralları
# Rakam ile başlayamaz
# Büyük küçük harf duyarlıdır
# Türkçe karakter kullanmamalı

# musteriAdi = "Ahmet"
# musteriSoyadi = "Yılmaz"
# musteriAdiSoyadi = musteriAdi + " " + musteriSoyadi
# musteriCinsiyeti = "Erkek"
# musteriTCNo = "12345678901"
# musteriDogumYili = 1990
# musteriAdres = "İstanbul, Türkiye"
# musteriYasi = 2025 - musteriDogumYili


# yaricap = input("Lütfen bir sayı giriniz: ")
# pi = 3.14

# daireAlan = pi * (int(yaricap) ** 2)
# daireCevre = 2 * pi * int(yaricap)


# "len" fonksiyonu string ifadelerin karakter sayısını verir

name= "Ahmet"
surname= "Yılmaz"
age= 30
print("My name is {}{}. I am {} years old.".format(name, surname, age))

message = " Hello There. My name is Muharrem"
print(message.lower()) # tüm harfleri küçük yapar
print(message.upper()) # tüm harfleri büyük yapar
print(message.title()) # her kelimenin ilk harfini büyük yapar
print(message.capitalize()) # sadece ilk harfi büyük yapar
print(message.strip()) # baştaki ve sondaki boşlukları siler
print(message.split()) # string ifadeyi boşluklardan ayırarak liste yapar
print(" ".join(message.split())) # listeyi string ifadeye çevirir
print(message.find("Muharrem")) # aranan ifadenin başladığı indexi verir
print(message.replace("Muharrem", "Ahmet")) # bir ifadeyi başka bir ifade ile değiştirir
print(message.center(50, "*")) # string ifadeyi belirtilen genişlikte ortalar ve boşlukları belirtilen karakter ile doldurur
print(message.count("e")) # belirtilen karakterin kaç kere geçtiğini sayar
print(message.isdigit()) # string ifadenin sadece rakamlardan oluşup oluşmadığını kontrol eder
print(message.isalpha()) # string ifadenin sadece harflerden oluşup oluşmadığını kontrol eder


#Listeler
numbers = [1, 3, 5, 7, 9]
fruits = ["elma", "armut", "muz", "çilek"]

numbers.append(11) # liste sonuna eleman ekler
numbers.insert(0, 0) # belirtilen indexe eleman ekler
numbers.remove(5) # belirtilen elemanı siler
numbers.pop() # son elemanı siler
numbers.sort() # listeyi küçükten büyüğe sıralar
numbers.reverse() # listeyi ters çevirir
numbers.count(3) # belirtilen elemanın kaç kere geçtiğini sayar
numbers.clear() # listeyi temizler


