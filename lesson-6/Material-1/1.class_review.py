# Temel (Ana) telefon sınıfı (BasePhone) oluşturun.
# Yapıcı metodunda phone_id, brand, model, price olsun.
# show_information() metodu ile telefon bilgilerini yazdırın.
# phone_ring_sound() metodunu oluşturun. "Common phone ring"

# BasePhone'dan miras alan Samsung isimli bir alt sınıf oluşturun.
# Yapıcı metodunu genişletin. operating_system ekleyin.
# show_information() metodunu genişletin. OS bilgisini de yazdırın.
# phone_ring_sound() metodunu override edin. Bu metod sound argümanı alsın ve yazdırsın.
from uuid import uuid4


class BasePhone:
    def __init__(self, phone_id, brand, model, price):
        self.phone_id = phone_id
        self.brand = brand
        self.model = model
        self.price = price

    def show_information(self):
        return f"Phone ID: {self.phone_id}\nBrand: {self.brand}\nModel: {self.model}\nPrice: {self.price}"

    def phone_ring_sound(self):
        print("Common phone ring")

# Alt sınıf
class Samsung(BasePhone):
    def __init__(self, phone_id, brand, model, price, operating_system):
        super().__init__(phone_id, brand, model, price)
        self.os = operating_system
    def show_information(self):
        print(super().show_information(), f"\nOS: {self.os}")
    def phone_ring_sound(self, sound):
        print(f"Samsung Ringtone: {sound}")


samsung1 = Samsung(uuid4(), "Samsung", "Note 2", 700, "Android")
samsung2 = Samsung("abc123", "Samsung", "Note 3", 850, "Android")
samsung1.show_information()
samsung1.phone_ring_sound("Over the horizon")
