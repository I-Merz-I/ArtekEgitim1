"""
def yazdir(isim="Atiba"):
    print("Merhaba "+ isim)

yazdir("Orkun")
yazdir()


def add(*params): #*params değişken sayıda argüman alır
    total = 0
    for n in params:
        total += n
    return total

print(add(1,2,3,4,5))
print(add(10,20,30))
print(add(5,15,25,35,45,55))


def displayUser(**args): #**args değişken sayıda anahtar kelime argümanı alır
    for key, value in args.items():
        print("{} is {}".format(key, value))

displayUser(name="Atiba", age=35, city="Istanbul")
displayUser(name="Orkun", age=24, job="Engineer")
displayUser(name="Gökhan", country="Turkey")


def myFunc(a,*b,**c):
    print(a)
    print(b)
    print(c)

myFunc(10,20,30, name="Atiba", age=35)


#Lambda Fonksiyonları

list1 = [1,2,3,4,5,6,7,8,9,10]  

def square(num):
    return num ** 2
print(square(5))

#Lambda ile aynı fonksiyon

square2 = lambda num: num ** 2
print(square2(6))

result = list(map(square, list1))
print(result)
"""


"""
#Bankamatik Uygulaması

AtibaHesap = {
    "ad": "Atiba",
    "hesapNo": "1234567890",
    "bakiye": 5000,
    "ekHesap": 4000
}

OrkunHesap = {
    "ad": "Orkun",
    "hesapNo": "9876543210",
    "bakiye": 3000,
    "ekHesap": 5000
}
def paraCek(hesap, miktar):
    print(f'Merhaba {hesap["ad"]}')

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Lütfen paranizi aliniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if toplam >= miktar:
            ekHesapKullanimi = input("Ek hesap kullanilsin mi? (e/h): ")
            if ekHesapKullanimi == "e":
                kalanMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kalanMiktar
                print("Lütfen paranizi aliniz.")
            else:
                print(f'Yetersiz bakiye. Bakiyeniz: {hesap["bakiye"]} TL')
        else:
            print("Yetersiz bakiye. İşlem yapilamiyor.")

def bakiyeSorgula(hesap):
    print(f'Hesap Sahibi: {hesap["ad"]}')
    print(f'Bakiye: {hesap["bakiye"]} TL')
    print(f'Ek Hesap: {hesap["ekHesap"]} TL')

paraCek(AtibaHesap, 8000)
paraCek(OrkunHesap, 5500)
bakiyeSorgula(AtibaHesap)
bakiyeSorgula(OrkunHesap)

"""


