# Encapsulation (Kapsülleme)
# Bir sınıfın içi yapısını dış dünyadan saklamak için kullanılan bir mekanizmadır.
# Hatalı ya da kötü amaçlı kullanımları minimize etme

class Car:
    def __init__(self, make="", model=""):
        self.make = make
        self.model = model

        # Private attribute
        self.__fuel_level = 0


camry = Car("Toyota", "Camry")
camry.make
camry.__fuel_level # AttributeError: 'Car' object has no attribute '__fuel_level'


class Car:
    def __init__(self, make="", model=""):
        self.make = make
        self.model = model

        # Private attribute
        self.__fuel_level = 0

    def set_fuel_level(self, level):
        if 0 <= level <= 100:
            self.__fuel_level += level
        else:
            print("Geçersiz yakıt seviyesi")

    def get_fuel_level(self):
        return self.__fuel_level

    def drive(self, distance):
        if self.__fuel_level > 0:
            self.__fuel_level -= 0.1 * distance
        else:
            print("No fuel!")

camry = Car("Toyota", "Camry")
camry.make
camry.__fuel_level
camry.get_fuel_level()
camry.drive(10)

camry.set_fuel_level(10)
camry.get_fuel_level()
camry.drive(10)
camry.get_fuel_level()