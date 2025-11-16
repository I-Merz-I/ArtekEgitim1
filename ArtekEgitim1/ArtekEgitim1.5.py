#İf blokları

# x = int(input("x: "))
# y = int(input("y: "))

# if x > y :
#     print("x y den büyük")
# elif x==y :
#     print("x y eşit")
# else:
#     print("y x den büyük")


# 1-)

# isim = input("isminiz: ")
# yas = int(input("yasiniz: "))
# egitim = input("egitim: ")

# if (yas>=18) and ((egitim=="üniversite") or (egitim=="lise")):
#     print("ehliyet alabilirsiniz")
# else:
#     print("ehliyet alamazsiniz")


# 2-)

import datetime

tarih = input("lütfen aracin trafiğe cikis tarihini giriniz: ")
tarih = tarih.split("/")

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis

if fark.days < 365:
    print("birinci servis araligi")
elif fark.days>365 and fark.days<365*2 :
    print("ikinci servis araligi")
elif fark.days>365*2 and fark.days<365*3 :
    print("üçüncü servis araligi")
else:
    print("hatali tarih")




                  




