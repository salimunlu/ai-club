import os
os.getcwd()   # get current working directory (şuanki çalışma dizinin al)
os.chdir("lesson-6/Material-2")  # change directory (çalışma dizinini değiştir)

# Bütün bir dosyayı okumak
# with keyword'ü ile dosyayı açıyoruz. İşimiz bittiğinde dosya otomatik kapanacaktır.
# UTF 8 yaygın karakter kodlama sistemidir. Türkçe'deki karakterler dahil
# birçok dildeki karakterleri destekler.
with open("dosya1.txt", encoding="utf8") as file:
    icerik = file.read()
    print(icerik)


# Dosya yolu (file path) bilgisi ile dosya okuma
with open("C:/Users/salim.unlu/Documents/trial.txt", encoding="utf8") as file:
    icerik = file.read()
    print(icerik)

# Satır satır dosya okuma (line by line)
with open("password.txt", encoding="utf8") as f:
    for line in f:
        line = line.strip()
        print(line)

with open("password.txt", encoding="utf8") as f:
    lines = f.readlines()
    lines = [satir.strip() for satir in lines]
    print(lines)



with open("password.txt", "r", encoding="utf8") as f:   # "r" okuma modu
    user_data = {}
    for line in f:
        line_list = line.strip().split(",")
        user_data[line_list[0]] = line_list[1]
    print(user_data)



