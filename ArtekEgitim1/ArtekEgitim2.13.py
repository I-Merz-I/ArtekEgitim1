# def outer(num1):
#     print("outer:")
#     def inner(num1):
#         print("inner:")
#         return num1 + 5
#     num2 = inner(num1)
#     print(num1, num2)

# outer(10)

#Decarator Fonksiyonlar

def my_decarator(func):
    def wrapper(name):
        print("fonsiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decarator
def say_hello(name):
    print("Merhaba!",name)

say_hello("Ahmet") 




    