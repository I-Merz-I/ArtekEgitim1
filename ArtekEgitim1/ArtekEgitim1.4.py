x,y,z = 2, 5, 10

numbers = 1, 5, 7, 10 ,6

# #1
# a = int(input ("Bir sayı girin: "))
# b = int(input ("Bir sayı daha girin: "))

# c = (a * b ) - ( x + y + z )
# print("Sonuç: ", c)


#2 

# kalansiz= y // x
# print("Kalansiz bölme sonucu: ", kalansiz)

#Atama operatörleri
# Aynı elemanlardan oluşan birden fazla değeri tek bir değişkende tutar
#=, +=, -=, *=, /=, //=, **=, %=

#karşılaştırma operatörleri
# İki değeri karşılaştırmak için kullanılır
#<, >, <=, >=, ==, !=

#Mantıksal operatörler
# Birden fazla koşulu birleştirmek için kullanılır
# and, or, not

x = y = [1, 3, 5]
z = [1, 3, 5]

print(x is y)  # True, çünkü x ve y aynı nesneyi gösteriyor
print(x is z)  # False, çünkü x ve z farklı nesneleri gösteriyor
print(x == z)  # True, çünkü x ve z'nin içerikleri aynı

x= ["elma", "armut"]
print("elma" in x)  # True, çünkü "elma" listede var
print("muz" in x)  # False, çünkü "muz" listede yok
