# Başlık: String ve Integer
print("Hello World!")  # Bu bir string
print(8)               # Bu bir integer

# Başlık: Float, Bool ve Complex
print(8.0)  # Bu bir float
print(True) # Bu bir bool
print(1j)   # Bu bir complex
print(None) # Bu bir Nonetype

# Keywords (Anahtar Kelimeler)
# Built-in (yerleşik) fonksiyonlar

# help fonksiyonu içine bir fonksiyon alır.
help(print)
help(len)

# Başlık: Değişkenler
number = 8
number + 1

# type fonksiyonu nesnenin (değişkenin) veri tipini verir.
# Değişken 'number' tanımı ve tipinin kontrolü
number = 8
print(type(number))  # <class 'int'>

# Değişken 'text' tanımı ve tipinin kontrolü
text = "12"
print(type(text))    # <class 'str'>

# Değişken 'weight' tanımı ve tipinin kontrolü
weight = 76.5
print(type(weight))  # <class 'float'>

# Değişken 'is_admin' tanımı ve tipinin kontrolü
is_admin = True
print(type(is_admin))  # <class 'bool'>

# Mantıksal İşlemler (and or operators)
print(True and True)    # Çıktı: True
print(True and False)   # Çıktı: False
print(False and True)   # Çıktı: False
print(False and False)  # Çıktı: False

print(True or True)     # Çıktı: True
print(True or False)    # Çıktı: True
print(False or True)    # Çıktı: True
print(False or False)   # Çıktı: False

# Başlık: Temel Aritmetik İşlemler
# İki sayının toplamı ve yazdır
print(2 + 2)  # Çıktı: 4

# İki sayının farkı ve yazdır
print(2 - 2)  # Çıktı: 0

# İki sayının çarpımı ve yazdır
print(2 * 2)  # Çıktı: 4

# İki sayının bölümü (sonuç float) ve yazdır
print(2 / 2)  # Çıktı: 1.0

# Bir sayının diğer sayıya bölümünden kalan (mod) ve yazdır
print(3 % 2)  # Çıktı: 1

# Bir sayının diğer sayıya bölümünden kalan (mod) ve yazdır
print(7 % 3)  # Çıktı: 1

# Bir sayının üssü ve yazdır
print(2 ** 2)   # Çıktı: 4

# Floor division (taban bölme) sonuçları ve yazdır
print(5 // 2)  # Çıktı: 2

# Başlık: Çoklu Değişken Atama
# x ve y değişkenlerine sırasıyla 2 ve 3 değerlerini atama
x, y = 2, 3

# Değişken x'i yazdır
print(x)  # Çıktı: 2

# Değişken y'yi yazdır
print(y)  # Çıktı: 3

# Başlık: Değişken Güncelleme
# Değişken x'in değerini 1 artır ve yeni değeri yazdır
x = x + 1
print(x)  # Şu anki x değeri + 1

# Kısa gösterim: Değişken x'in değerini 1 artır ve yeni değeri yazdır
x += 1
print(x)  # Şu anki x değeri + 1


# Başlık: Assignment Operators
# x değişkenine 5 değerini atama
x = 5

# x değişkenine 3 ekleyerek güncelle
x += 3  # x = x + 3

# x değişkeninden 3 çıkararak güncelle
x -= 3  # x = x - 3

# x değişkenini 3 ile çarpıp güncelle
x *= 3  # x = x * 3

# x değişkenini 3'e bölerek güncelle
x /= 3  # x = x / 3

# x değişkenini 3'e bölümünden kalanı alarak güncelle
x %= 3  # x = x % 3

# x değişkenini 3'e bölerken taban bölme yaparak güncelle
x //= 3  # x = x // 3


# Başlık: Kimlik Operatörleri
# x ve y değişkenlerine aynı değeri atama
x = 6
y = 6

# x ve y aynı nesneyi mi gösteriyor? (Kimlik kontrolü)
is_same = x is y  # x ve y aynı nesneyi gösterdiğinden True olur

# x ve y farklı nesneleri mi gösteriyor? (Kimlik kontrolü)
is_different = x is not y  # x ve y aynı nesneyi göstermediğinden True olur

# Sonuçları yazdır
print("x is y:", is_same)       # x is y: True
print("x is not y:", is_different)  # x is not y: False


# Başlık: Üyelik Operatörleri
# Bir liste oluştur
my_list = [76, 66, 78, 99, 12]

# 76 değeri, my_list içinde mi?
is_in_list = 76 in my_list  # 76, my_list içinde bulunduğu için True olur

# Sonucu yazdır
print("76 in my_list:", is_in_list)  # 76 in my_list: True


# Başlık: Tip Dönüşümü (Type Conversion)
# Integer'dan Float'a dönüşüm
x = 5
y = float(x)
print(y)  # Çıktı: 5.0 (float)

# Float'tan Integer'a dönüşüm
y = 5.6
z = int(y)
print(z)  # Çıktı: 5 (ondalık kısmı keser)

# Integer'dan String'e dönüşüm
x = 5
y = str(x)
print(y)  # Çıktı: '5' (string olarak)

# Float'tan String'e dönüşüm
a = 3.14
b = str(a)
print(b)  # Çıktı: '3.14' (string olarak)

# String'den Integer'a dönüşüm
c = '42'
d = int(c)
print(d)  # Çıktı: 42 (integer olarak)

# String'den Float'a dönüşüm
e = '2.718'
f = float(e)
print(f)  # Çıktı: 2.718 (float olarak)

# Boolean'dan Integer'a dönüşüm
g = True
h = int(g)
print(h)  # Çıktı: 1 (True, integer olarak 1'e dönüşür)

# Boolean'dan String'e dönüşüm
i = False
j = str(i)
print(j)  # Çıktı: 'False' (string olarak)

# Float'tan Boolean'a dönüşüm
k = 0.0
l = bool(k)
print(l)  # Çıktı: False (0.0, boolean olarak False'a dönüşür)

# Integer'dan Boolean'a dönüşüm
m = 42
n = bool(m)
print(n)  # Çıktı: True (0 dışındaki sayılar, boolean olarak True'ye dönüşür)
