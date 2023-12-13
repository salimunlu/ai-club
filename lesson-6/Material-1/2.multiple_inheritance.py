class Memeli:
    def memeli_bilgi(self):
        print("Memeliler doğum yapabilir.")


class Kanatli:
    def kanatli_bilgi(self):
        print("Kanatlı hayvanlar uçabilir.")


class Yarasa(Memeli, Kanatli):
    def yarasa_bilgi(self):
        print("Yarasalar kanatlı memelilerdir.")


class NewClass:
    pass

yarasa1 = Yarasa()
yarasa1.yarasa_bilgi()
yarasa1.kanatli_bilgi()
yarasa1.memeli_bilgi()


# isinstance() fonksiyonu
isinstance(yarasa1, Yarasa)
isinstance(yarasa1, Memeli)
isinstance(yarasa1, Kanatli)
isinstance(yarasa1, NewClass)

# issubclass() fonksiyonu
issubclass(Yarasa, Kanatli)  # True
issubclass(Yarasa, Memeli)   # True
issubclass(Kanatli, Yarasa)  # False




# Ana sınıf: Creature, constructor oluşturun, "isim" adında bir argüman alsın.
# 2 metodu olsun. attack(), defence() pass

# FlyingCreature adında bir alt sınıf oluşturun. Creature'dan inheritance alsın.
# fly() metodu tanımlayın. self.isim uçuyor çıktısı versin.

# AquaticCreature adında bir alt sınıf oluşturun. Creature'dan inheritance alsın.
# swim() metodu tanımlayın. self.isim yüzüyor çıktısı versin.

# Dragon adında bir alt sınıf oluşturun.
# FlyingCreature, AquaticCreature sınıflarından miras alsın.
# Constructor oluşturun. Yeni özellik olarak color ekleyin.
# attack() ve defence() metodlarını override edin.
# isim ateş püskürterek saldırıyor
# isim kanatlarıyla kendini savunuyor.

class Creature:
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def defence(self):
        pass


class FlyingCreature(Creature):
    def fly(self):
        print(f"{self.name} uçuyor.")


class AquaticCreature(Creature):
    def swim(self):
        print(f"{self.name} yüzüyor.")


class Dragon(FlyingCreature, AquaticCreature):
    def __init__(self, name, color):
        super().__init__(name)
        self.color =color

    def attack(self):
        print(f"{self.name} ateş püskürerek saldırıyor.")

    def defence(self):
        print(f"{self.name} kanatlarıyla kendini savunuyor.")


dragon = Dragon("Big Dra", "orange")
dragon.attack()
dragon.defence()
dragon.swim()
dragon.fly()
