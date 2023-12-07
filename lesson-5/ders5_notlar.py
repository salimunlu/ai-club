# Nested Functions (İç İçe Fonksiyonlar)
def outer_func(x):
    def inner_func(y):
        def third_func(z):
            return x + y + z

        return third_func

    return inner_func


a = outer_func(5)
print(type(a))  # 'a' değişkeninin tipini yazdır
b = a(4)
print(type(b))  # 'b' değişkeninin tipini yazdır

print(b(3))  # İç içe fonksiyonları sırayla çağır ve sonucu yazdır

print(outer_func(5)(6))  # İç içe fonksiyonları sırasıyla çağır
print(outer_func(5)(6)(3))  # İç içe fonksiyonların tümünü çağır ve sonucu yazdır

# Çalışan-Ast İlişkisini Tanımlayan Sözlükler
calisan_hiyerarsi1 = {
    'CEO': ['CTO', 'CFO', 'CMO'],
    'CTO': ['Dev1', 'Dev2'],
    'CFO': ['Acc1', 'Acc2', 'Acc3'],
    'Dev1': ['Intern1', 'Intern2', 'Intern3', 'Intern4']
}

calisan_hiyerarsi2 = {
    'CEO': ['CTO', 'CFO'],
    'CTO': ['Dev1', 'Dev2', 'Dev3'],
    'CFO': ['Acc1', 'Acc2', 'Acc3'],
    'Dev1': ['Intern1', 'Intern2', 'Intern3', 'Intern4'],
    'Dev2': ['Intern1', 'Intern2', 'Intern3', 'Intern4']
}

# Toplam Alt Çalışan Sayısını Bulan Fonksiyon
import time


def toplam_ast_sayisi(hiyerarsi, calisan):
    toplam = 0
    if calisan not in hiyerarsi:
        return 0

    astlar = hiyerarsi[calisan]
    toplam += len(astlar)
    print(f"{calisan} kişisinin {toplam} alt çalışanı hesaplandı.")
    time.sleep(2)

    for ast in astlar:
        toplam += toplam_ast_sayisi(hiyerarsi, ast)
        print(f"{ast} kişisine bakıldı ve toplam çalışan güncellendi: {toplam}")
        time.sleep(2)

    return toplam


# Çeşitli pozisyonlardaki çalışanların toplam alt çalışan sayısını hesapla
print(toplam_ast_sayisi(calisan_hiyerarsi2, "CTO"))
print(toplam_ast_sayisi(calisan_hiyerarsi1, "CTO"))
print(toplam_ast_sayisi(calisan_hiyerarsi2, "CEO"))


# Recursive Functions (Özyinelemeli Fonksiyonlar)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # 5'in faktöriyelini hesapla ve yazdır


# Local Variables (Yerel Değişkenler)
def example():
    a = 10
    print(f"Fonksiyon içi değişken: {a}")


example()
# print(a)  # Bu satır hata verecektir. Yerel değişken 'a' fonksiyon dışında tanımlı değil.


# Global Variables (Küresel Değişkenler)
b = 5


def example_global():
    global b
    b *= 2
    print(f"Fonksiyon içi değişken: {b}")


example_global()
print(b)  # 'b' değişkeninin güncellenmiş değerini yazdır


# Class Definition (Sınıf Tanımı)
class Dog:
    # __init__ metodu özel (special) metottur ve sınıfın yapıcı (constructor) metodudur.
    def __init__(self, name, age):   # Constructor
        self.name = name
        self.age = age
        self.food = ["meat", "bread", "fish"]

    def description(self):      #Instance Method
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"

dog1 = Dog("Miles", 5)
dog2 = Dog("Mike", 6)

dog1.age
dog1.food
dog1.speak("Hav")
dog1.description()



class Car:
    def __init__(self, color: str, mileage: int):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

car1 = Car("blue", 20000)
car2 = Car("red", 30000)
car3 = Car(color="purple", mileage=25_000)
car4 = Car("orange", 20)

print(f"The {car1.color} car has {car1.mileage} miles.")
print(car1)

for car in (car1, car2, car3, car4):
    print(f"The {car.color} car has {car.mileage} miles.")

for car in (car1, car2, car3, car4):
    print(car)




