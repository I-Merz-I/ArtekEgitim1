#Dosya Yönetimi

# "w" modu: Yazma modu, dosya zaten varsa içeriğini siler ve yeni içerik yazar.

# file = open("newfile.txt", "w")
# file.write("Bu yeni bir dosyadır.\n")
# file.close()

# "a" modu: Ekleme modu, dosya zaten varsa içeriğin sonuna ekler.

# file = open("newfile.txt", "a")
# file.write("Bu satir eklenmiştir.\n")
# file.close()

# "x" modu: Oluşturma modu, dosya zaten varsa hata verir.

# file = open("new_file.txt", "x")
# file.write("Bu dosya yeni oluşturuldu.\n")
# file.close()

#"r" modu: Okuma modu, dosya zaten varsa içeriğini okur.

# file = open("newfile.txt", "r")
# content = file.read()
# print(content)
# file.close()

#" with " ifadesi: Dosya işlemlerini daha güvenli ve temiz bir şekilde yapmayı sağlar.

with open("newfile.txt", "r") as file:
    content = file.read()
    print(content)
    print(file.tell())  # Mevcut dosya imlecinin konumunu gösterir
    file.seek(0)  # Dosya imlecini başa alır

# "r+" modu: Okuma ve yazma modu, dosya zaten varsa içeriğini okur ve yazabilir.

with open("newfile.txt", "r+") as file:
    content = file.read()
    print("Mevcut içerik:")
    print(content)
    file.write("Bu satir r+ modunda eklendi.\n")


