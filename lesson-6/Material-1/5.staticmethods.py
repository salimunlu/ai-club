class Mathematics:
    @staticmethod   # decorator (süsleyici)
    def add5(x):
        return x + 5
    @staticmethod
    def add10(x):
        return x + 10
    @staticmethod
    def subtract(x, y):
        return x - y
    @staticmethod
    def show_smth():
        print("This is a static method")


x = 5
Mathematics.add5(x)
Mathematics.add10(x)

m1 = Mathematics()
m1.add5(x)
m1.add10(x)
m1.subtract(10, 6)

# Şu ana kadar 3 tip metot gördük
#Instance Method: Bir örnek üzerinden çağrılabilir. self kelimesi kullanılır.
#Class Method: Bir sınıfa bağlı olarak çağrılabilir. cls kelimesi kullanılır.
#Static Method: Ne örneğe ne de sınıfa bağlı olarak çağrılır. self ya da cls almaz.

class Dikdortgen:
    sayac = 0  #sınıf özelliği
    def __init__(self, en, boy):   # constructor
        self.en = en    # örnek özelliği
        self.boy = boy
        Dikdortgen.sayac += 1

    def alan_hesapla(self):  # instance method
        return self.en * self.boy

    @classmethod             # class method (sınıf metodu)
    def dikdortgen_sayisi(cls):
        return cls.sayac

    @staticmethod
    def gecerli_olcu(width, height):
        return width >= 0 and height >= 0


d1 = Dikdortgen(4, 5)
d2 = Dikdortgen(10, 16)

d1.alan_hesapla()  # instance üzerinden instance methoda erişim
Dikdortgen.dikdortgen_sayisi()  # sınıf adı üzerinden class method'a erişim
d1.dikdortgen_sayisi()  # instance üzerinden class method'a erişim
d1.sayac

d1.gecerli_olcu(-5, 4)    # instance üzerinden static methoda erişim
Dikdortgen.gecerli_olcu(4, 8)   #sınıf adı static methoda erişim

