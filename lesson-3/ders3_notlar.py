# Dictionary (Sözlük) Oluşturma
# Sözlükler, anahtar (key) ve değer (value) çiftlerini içeren veri yapılarıdır.

# Bir sözlük örneği oluşturuluyor ve sıcaklık bilgilerini barındırıyor.
my_dict = {"Ankara":25, "İstanbul":23, "Agri":20}
print(my_dict)
print(type(my_dict))

# Sözlükten 'Ankara' anahtarına ait değer erişiliyor.
my_dict["Ankara"]
type(my_dict["Ankara"])

# Sözlükten 'get' metodu ile 'İstanbul' anahtarına ait değer erişiliyor.
my_dict.get("İstanbul")

# Sözlük öğelerine erişim
items = my_dict.items()  # .items() metodu ile anahtar-değer çiftlerini içeren bir görünüm elde ediliyor.
type(items)

# Oyuncu bilgilerini içeren daha karmaşık bir sözlük örneği.
player_id = {
    "Name": "Kobe Bryant",
    "Height": 1.90,
    "Weight": 96,
    "Active": False,
    "Number": (8, 24),
    "Point": {
        "2014-15": 22.3,
        "2015-16": 17.6
    }
}

# İç içe sözlüklerde erişim
player_id.get("Point").get("2014-15")

# Sözlüğün anahtar ve değerlerine erişim.
player_id.keys()
player_id.values()

# Bir anahtar-değer çiftini sözlükten çıkarma
player_id.pop("Active")
player_id

# Eleman Ekleme
player_id["Country"] = "USA"
print(player_id)

# Elemanın Değerini Değiştirme
player_id["Height"] = player_id["Height"] * 100
print(player_id)

# Eleman Silme
del player_id["Country"]
print(player_id)

# Koşullu ifadeler (IF, ELIF, ELSE)
# Basit bir koşullu ifade örneği.
my_bool = True

if my_bool:
    print("my_bool is True")

# Kullanıcı girdisi ile koşullu ifade örneği
a = int(input("Birinci sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz: "))

if a < b:
    print(f"{a} sayısı {b} sayısından küçüktür.")
elif a == b:
    print(f"{a} sayısı {b} sayısına eşittir.")
else:
    print(f"{a} sayısı {b} sayısından büyüktür.")

# Not kontrolü yapan başka bir koşullu ifade örneği.
score = float(input("Notunuzu giriniz: "))

if score >= 90:
    print("Notunuz: A")
elif score >= 80:
    print("Notunuz: B")
elif score >= 70:
    print("Notunuz: C")
elif score >= 60:
    print("Notunuz: D")
else:
    print("Notunuz: F")

# FOR Döngüleri
# Range fonksiyonu ile belirli bir aralıkta döngü örneği.
for i in range(8, 11):
    print(f"{i}'nin karesi {i ** 2}")

# Liste üzerinde döngü örneği.
for num in [8, 9, 10]:
    print(f"{num}'nin karesi {num ** 2}")

# Sözlük üzerinde döngü örnekleri.
# Anahtarlar üzerinde dönülüyor.
for i in my_dict:
    print(i)

# Değerler üzerinde dönülüyor.
for i in my_dict.values():
    print(i)

# Anahtar ve değer çiftleri üzerinde dönülüyor.
for key, value in my_dict.items():
    print(f"{key}'ın sıcaklık değeri: {value}")

# Bir liste üzerinde iterasyon yaparak toplam ve sayacı güncelleme.
toplam = 0
sayac = 0

import time

for i in [1, 4, 10, 20]:
    sayac += 1
    toplam += i
    print(f"{sayac}. iterasyonda toplam değer {toplam}")
    time.sleep(5)
else:
    print("Döngü sona erdi.")

# Döngü içinde koşul kontrolü ve 'break' kullanımı.
toplam = 0
sayac = 0

for i in [1, 4, 10, 20]:
    sayac += 1
    toplam += i
    if toplam < 10:
        print(f"{sayac}. iterasyonda toplam değer {toplam}")
    elif toplam == 15:
        break
    time.sleep(5)
else:
    print(f"Döngü sona erdi. Toplam değer {toplam}")

# WHILE Döngüleri
# Basit bir while döngüsü örneği.
my_bool = True

sayac = 0
while my_bool:
    sayac += 1
    print(f"{sayac}. iterasyonda while döngüsü çalışıyor.")
    time.sleep(2)
    if sayac == 3:
        my_bool = False
        print("my_bool False olarak değiştirildi.")

# Sonsuz bir while döngüsü içinde not kontrolü ve 'break' ile döngüden çıkma.
while True:
    score = int(input("Notunuzu giriniz: "))
    if 0 <= score <= 100:
        print("Geçerli bir not girdiniz.")
        break
    print("Geçersiz bir not girdiniz.")

# 'pass' anahtar kelimesi ile boş bir döngü/durum oluşturma.
# Bu kod bloğu, belirli bir koşul altında herhangi bir işlem yapmadan geçmek için kullanılır.
while a < b:
    pass

if 10 > 9:
    pass
