# Kullanıcıdan bir sayı alınıyor.
number = int(input("Bir sayı giriniz:"))

# String Indexing
text = "Hacettepe"

# Pozitif indexleme
text[9]  # Bu, IndexError verecektir çünkü index sınırların dışında.

# Negatif indexleme
text[-1]  # Son karakteri verir.

# String Slicing
text[0:5]  # İlk 5 karakteri alır.
text[-1:-5:-1]  # Son 5 karakteri tersten alır.
text[-4:]  # Son 4 karakteri alır.
text[:5]  # İlk 5 karakteri alır.
text[2:5:2]  # 2'den başlayarak her 2. karakteri alır.

text[-1:-6:-2]  # Son karakterden başlayarak her 2. karakteri alır.

# String Concatenation
'Hello' + " " + 'World!'  # İki string'i birleştirir.
'Hello' + ' World!'  # İki string'i birleştirir.
'Hello\n' + ' World!'  # İki string'i yeni satır karakteriyle birleştirir.
print('Hello\n' + 'World!')  # İki string'i yeni satır karakteriyle yazdırır.
print('Hello\t' + 'World!')  # İki string'i tab karakteriyle yazdırır.

"a" * 5  # 'a' karakterini 5 kez yanyana yazdırır.

# String Formatting
math = float(input("Matematik notunuzu giriniz:\n> "))
python = float(input("Python notunuzu giriniz:\n> "))

print("Matematik notunuz:", math, "\nPython notunuz:", python)  # Eski formatlama yöntemiyle.
print(f"Matematik notunuz: {math}\nPython notunuz: {python}")  # f-string ile formatlama.
print("Matematik notunuz: {}".format(math))  # .format() ile formatlama.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {0} dollars for {2} pieces of item {1}."
print(myorder.format(price, itemno, quantity))  # .format() fonksiyonu ile sıralı biçimlendirme.

# String Methods
"hello".upper()  # Tüm karakterleri büyük harfe çevirir.
"HELLO".lower()  # Tüm karakterleri küçük harfe çevirir.
"hacettepe university".title()  # Her kelimenin ilk harfini büyük yapar.
"hacettepe university".capitalize()  # Sadece cümlenin ilk harfini büyük yapar.

# 'is' metotları
password = input("Pin numarasını giriniz: ")
print(password.isdigit())  # Girilen ifadenin sadece rakamlardan oluşup oluşmadığını kontrol eder.

password = input("Pin numarasını giriniz: ")
print(password.isalnum())  # Girilen ifadenin alfanümerik (harf veya sayı) olup olmadığını kontrol eder.

text = "    Hacettepe   "
text.strip()  # String'in başında ve sonundaki boşluk karakterlerini siler.

# Listeler, Demetler, Sözlükler, Küme
mixed_list = []
type(mixed_list)  # List türünü döner.

mixed_list = [1, 2, 3, "a", "b", 5.2, True, None, [35, 34, [1, 2, "abc"]]]
type(mixed_list)  # List türünü döner.
len(mixed_list)  # List uzunluğunu döner.
my_list = mixed_list[8]  # List içindeki listeyi alır.
type(my_list)  # List türünü döner.
my_list[2]  # İç içe listelerden eleman seçimi.
my_list[2][2]  # Daha da iç içe eleman seçimi.
my_list[2][2][1]  # En içteki listeden eleman seçimi.

type(my_list[2][2][1])  # Seçilen elemanın türünü döner.

my_list  # Listeyi gösterir.
my_list[:2][1]  # Slicing sonrası eleman seçimi.

for i in my_list:
    print(i)  # Listeyi döngü ile yazdırır.

# append(): Eleman ekleme
my_list = [0, 1, 2, 3, 4]
my_list.append(5)
print(my_list)

# extend(): Liste uzatma
new_list = [5, 6, 7]
my_list.extend(new_list)
print(my_list)

# insert(): Belirli bir indekse eleman ekleme
my_list.insert(3, "iki")
print(my_list)

# remove(): Eleman silme
my_list.remove("iki")
print(my_list)

my_list.remove(5)
print(my_list)

# pop(): İndeks ile eleman silme
popped = my_list.pop()
print(popped)
print(my_list)

popped = my_list.pop(0)
print(popped)
print(my_list)

id(my_list)
second_list = my_list
type(second_list)
second_list.pop()
print(second_list)
print(my_list)

third_list = my_list.copy()
id(my_list)
id(second_list)
id(third_list)


# index(): Elemanın indeksini bulma
print(my_list.index(4))

# count(): Eleman tekrar etme sayısını bulma
my_list.append(3)
print(my_list)

print(my_list.count(3))
print(my_list.count(1))

# sort(): Liste sıralama
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.append(5)

# reverse(): Listeyi ters çevirme
print(my_list)
my_list.append(10)
print(my_list)
my_list.reverse()
print(my_list)

a = my_list.sort(reverse=True)
print(a)

print(my_list)

# copy(): Liste kopyalama
print(my_list)

copied_list = my_list.copy()
print(copied_list)

copied_list.append("a")
print(copied_list)

print(my_list)


my_list2 = my_list
print(my_list2)
my_list2.append("a")
print(my_list2)

print(my_list)

# sorted(): Elemanları sıralayıp yeni bir liste döner.
print(my_list)
my_list.pop()
my_list.append(7)
print(my_list)
sorted(my_list)  # Kalıcı bir sıralama değil
print(my_list)

my_list = sorted(my_list)  # Kalıcı sıralama

# Veri analizi için temel istatistik hesaplamaları
my_list = [23, 34, 56, 45]
average = sum(my_list) / len(my_list)

import numpy as np

mean = np.mean(my_list)
minimum = np.min(my_list)
std_dev = np.std(my_list, ddof=1)

# Set (Küme) oluşturma ve işlemler
my_list = [2, 4, 2, 3, 3, 3, 6, 6, 4]
my_set = set(my_list)  # Liste elemanlarından küme oluşturur.
print(my_set)


# Tuple Oluşturma

empty_tuple = ()
print(empty_tuple)
print("Type of this variable:", type(empty_tuple))

my_tuple = (1, 2, 3, 1, 2, 3)
print(my_tuple)

# Tuple'ın uzunluğu
len(my_tuple)

# Tuple Elemanlarına Erişim
my_tuple[0]

# Slicing ile Sub-tuple Oluşturma
my_tuple[1:5]

# Bir Elemanın İçerisinde Olduğunu Öğrenme
3 in my_tuple
6 in my_tuple

############################ Tuple Methods ############################
# count()
my_tuple.count(2)

# index()
my_tuple.index(1)
my_tuple.index(4)

try:
    print(my_tuple.index(4))
except:
    print("The numbered you entered is not this tuple.")

# Tuple'lerı Birleştirme
second_tuple = (6, 7)
third_tuple = my_tuple + second_tuple
print(third_tuple)

# Tuple Elemanlarını Değişkenlere Atama
ttest = (2.5, 0.045)
a, b = ttest
print(a)
print(b)

a, b, c = ttest  # ValueError

# Dictionary (Sözlük) Oluşturma
# {"key":"value"}

my_dict = {"Ankara":25, "İstanbul":23, "Agri":20}
my_city = ["Ankara", "İstanbul", "Agri"]
my_list = [25, 23, 20]
print(my_dict)
print(type(my_dict))

# Sözlükten değer (value) çağırma
print(my_dict["Ankara"])

# Ornek
fruits = dict(apple = 5, banana = 3, pear = 2)
print(fruits)
type(fruits)

total_weight = fruits["apple"] + fruits["banana"] + fruits["pear"]
print(total_weight)

type(fruits["apple"])
