import numpy as np

# Python listesinden NumPy array oluşturma

# py_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]

# np_array=np.array([1,2,3,4,5,6,7,8,9])

# py_multi = [[1,2,3],[4,5,6],[7,8,9]]
# np_multi = np_array.reshape(3,3)

# print(py_multi)
# print(np_multi)

# print(np_array.ndim)  # Boyut sayısı
# print(np_multi.ndim)  # Boyut sayısı

# print(np_array.shape)  # Boyut bilgisi
# print(np_multi.shape)  # Boyut bilgisi


# # result = np.array([1,3,5,7,9])
# result = np.arange(1,10)
# print(result)

# result2 = np.arange(10,100,3)
# print(result2)

# result3 = np.zeros(10)
# result4 = np.ones(10)

# result5 = np.linspace(0,100,5)
# print(result5)  

# result6 = np.random.randint(0,100,10)
# print(result6)

# np_array2 =np.arange(50)
# np_multi2 = np_array2.reshape(5,10)
# print(np_multi2.sum(axis=1))  # Satırların toplamı
# print(np_multi2.sum(axis=0))  # Sütunların toplamı


#Uygulamalar

#1-)(0 ile 100 arasında eşit aralıklı 5 sayı üretin.
result = np.linspace(0, 100, 5)

#2-)[-1,1] arasında 10 tane rastgele sayı üretin.
result2 = np.random.randn(10)

#3-)3x5 boyutunda 0-50 arasında bir matris üret
# ve bu matrisin satır ve sütün toplamlarını bulun.

matris = np.random.randint(0, 50,(3, 5))
satir_toplam = matris.sum(axis=1)
sutun_toplam = matris.sum(axis=0)
# print("Matris:\n", matris)
# print("Satır Toplamları:", satir_toplam)
# print("Sütun Toplamları:", sutun_toplam)   

#4-) martisin en büyük, en küçük ve ortalamasını bulun.
en_buyuk = matris.max()
en_kucuk = matris.min()
ortalama = matris.mean()

#5-) üretilen martisin en büyük elemanının ve  en küçük elemanının indeksini bulun.
en_buyuk_indeks = matris.argmax()
en_kucuk_indeks = matris.argmin()

#6-)Martisirin tüm satırlarıdaki ilk elemanı alın.
ilk_elemanlar = matris[:, 0]


