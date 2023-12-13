# Polimorphism (Çok Biçimlilik) aynı arayüzü paylaşan farklı nesnelerın
# farklı davranışlar sergileyebilmesidir.

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self. height


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


shapes = [Rectangle(4, 3), Square(4), Rectangle(2, 6), Square(3), Triangle(4, 5), Rectangle(2, 8)]
type(shapes)
type(shapes[0])


for sayac, sekil in enumerate(shapes, start=1):
    print(f"{sayac}. şeklin alanı {sekil.area()}")


# Polymorphism sayesinde hangi tipte bir nesne olduğuna bakılmaksızın, her nesnenin kendi area
# metodunu çağırabilir ve amaca uygun işlem yapabiliriz.
# Farklı sınıfların aynı arayüzü (metodu) paylaşabilmesi ve aynı arayüzü kullanırkan
# farklı davranışlar sergileyebilmesidir.
# Yazdığımız kodun daha genişletilebilir, okunabilir ve bakımının daha rahat yapılabilmesini sağlarız.

