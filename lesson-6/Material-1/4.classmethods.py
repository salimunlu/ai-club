class Person:
    number_of_people = 0       # class attribute (sınıf özelliği)

    def __init__(self, name):  # constructor (yapıcı) method
        self.name = name       # instance attribute (örnek özelliği)

    def person_info(self):     # instance method
        return f"My name is {self.name}"

    @classmethod               # Bir metodu sınıf metoduna dönüştürür.
    def add_person(cls):       # class method
        cls.number_of_people += 1

    @classmethod
    def num_of_people(cls):    # class method
        return cls.number_of_people

person1 = Person("Tim")
person2 = Person("Jill")


# Class attribute'a hem sınıf hem de bir örnek üzerinden erişilebilir.
Person.number_of_people
person1.number_of_people

# Bir sınıf adı üzerinden bir instance metod'a erişilemez.
Person.person_info()

# Bir sınıf adı üzerinden bir class method'a erşilebilir
Person.add_person()
Person.number_of_people
Person.num_of_people()

# Bir örnek (instance) üzerinden class method'a erişilebilir.
person1.add_person()
person1.num_of_people()

