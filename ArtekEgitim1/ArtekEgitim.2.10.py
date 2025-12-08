"""
import math # "as islem" yaparsak math modülüne islem ismiyle erişiriz
from math import factorial, sqrt # math modülünden sadece factorial ve sqrt fonksiyonlarını alırız

value = dir(math)
print(value)

value = help(math.factorial)
print(value)

"""
import random

result = random.random() # 0.0 ile 1.0 arasında rastgele bir sayı üretir
print(result)

result = int(random.uniform(10,100))
print(result)

result = random.randint(10,100) # 10 ile 100 arasında rastgele bir tam sayı üretir
print(result)

names = ["orkun","el bilal","gökhan","djalo"]
result = names[random.randint(0,len(names)-1)]
print(result)

result = random.choice(names)
print(result)

greeting = "kargalar sürü ile kartal yanliz uçar"
result = random.choice(greeting)
print(result)

liste = list(range(10))
random.shuffle(liste) # liste elemanlarının sırasını rastgele karıştırır
print(liste)

liste = range(100)
result = random.sample(liste,5) # liste içinden 5 tane rastgele eleman seçer
print(result)



