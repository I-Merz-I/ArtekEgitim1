import numpy as np

x = np.array([0,1,2,3,4,5,6,7])
y = np.array([])

for i in x:
    if i % 2 != 0:
        y = np.append(y,i)
    else:
        continue

z = x.reshape(2,4)

rev = np.flip(x)

satir_ort = np.mean(z,axis=1)

sütün_ort = np.mean(z,axis=0)




print(y)
print(x)
print(z)
print(rev)
print(satir_ort)
print(sütün_ort)
