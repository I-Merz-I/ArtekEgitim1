# meyveler = ["elma","armut","muz"]

# for meyve in meyveler:
#     print(f"meyvenin adi {meyve}")

# d = {"k1":1, "k2":2, "k3":4}


# Dictionary üzerinde for döngüsü

# for key,value in d.items():
#     print (key,value) 


# sayilar = [1,3,5,7,9,12,19,21]
# toplam = 0
# for i in sayilar:
#     if(i%3==0):
#         print (i)
#     toplam += i
# print(f"toplam : {toplam}")

# numbers = []
# i=0
# while i<5:
#     sayi = int(input("sayi giriniz: "))
#     numbers.append(sayi)
#     i+=1

# numbers.sort()
# print(numbers)


# urunler=[]

# adet = int(input("kaç ürün eklemek istersiniz: "))
# i=0

# while i<adet:
#     name = input("ürün adı: ")
#     price = int(input("ürün fiyatı: "))
#     urunler.append({"name": name, "price": price})
#     i+=1

# for urun in urunler:
#     print(f"urun adi: {urun['name']} urun fiyati: {urun['price']}")


#for döngüsü range ile

# for item in range(5,100,10):
#     print(item) 


#enumerate = indeks numarası ile birlikte elemanları döndürür

# sehirler = ["kocaeli", "istanbul", "ankara", "izmir"] 
# for index, sehir in enumerate(sehirler):
#     print(index, sehir)


# #zip : İki veya daha fazla listeyi paralel olarak döndürür
# names = ["ali", "veli", "ayse"]
# ages = [25, 30, 22]
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old")


#Listeye şartlı eleman ekleme (list comprehension)

# numbers = [ x**2 for x in range(10)if x%3==0]
# print(numbers)

# myString = "Hello World"
# mylist = [letter for letter in myString]
# print(mylist)


#Sayı tahmin oyunu
import random

sayi = random.randint(1,100)
can = int(input("Kaç hakkınız olsun? "))
hak = can
while hak>0:
    tahmin = int(input("Tahmininizi girin: "))
    if tahmin<sayi:
        print("Daha büyük bir sayı girin.")
    elif tahmin>sayi:
        print("Daha küçük bir sayı girin.")
    else:
        print("Tebrikler, doğru tahmin! Puaniınız: ", 100 - (100/can)*(can-hak))
        break
    hak -= 1
    print(f"Kalan hakkınız: {hak}")
if hak == 0:
    print(f"Üzgünüm, hakkınız bitti. Doğru sayı {sayi} idi.")