"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print("x/y:", x/y)
except ZeroDivisionError as zde:
    print("Bir sayı sıfıra bölünemez." , zde)
except ValueError as ve:
    print("Lütfen geçerli bir sayı giriniz.", ve)


def check_password(psw):
    import re
    if len(psw) < 8:
        raise ValueError("Parola en az 8 karakter olmalı")
    if not re.search("[a-z]", psw):
        raise ValueError("Parola en az bir küçük harf içermeli")
    if not re.search("[A-Z]", psw):
        raise ValueError("Parola en az bir büyük harf içermeli")
    if not re.search("[0-9]", psw):
        raise ValueError("Parola en az bir rakam içermeli")
    if not re.search("[_@$]", psw):
        raise ValueError("Parola en az bir özel karakter içermeli: _@$")
    if re.search(r"\s", psw):
        raise ValueError("Parola boşluk karakteri içermemeli")
    return True

password = input("Parola girin: ")
try:
    check_password(password)
except ValueError as err:
    print(err)


class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Yaş negatif olamaz")
        elif len(name) == 0:
            raise ValueError("İsim boş olamaz")
        else:
            self.name = name
            self.age = age

p = Person("Muharrem", -10)
print(p.name, p.age)

"""

#uygulama

# Sayı dışı değerleri içeren bir liste verildiğinde,
# bunları tamsayıya dönüştüren ve
# geçersiz değerleri atlayan program
liste = ["1", "2", "5a", "10b", "abc","10","50"]

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

# Kullanıcıdan sürekli sayı girmesini isteyen,
# "q" girilince programı sonlandıran ve
# geçersiz sayı girişlerinde uyarı veren program

while True:
    sayi = input("sayi:")
    if sayi=="q":
        break

    try:
        result = float(sayi)
        print("girdiğiniz sayı:", result)
    except ValueError:
        print("geçersiz sayı")
        continue

#Girilen parolayı türkçe karakter hatası veren program

def checkPassword(parola):
    turkce_karakterler = "çğıöşüÇĞİÖŞÜ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez.") 
        else:
            pass
    print("Parola geçerli.")

parola = input("Parola girin: ")
try:
    checkPassword(parola)
except TypeError as te:
    print(te)

