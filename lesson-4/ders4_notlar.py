# 'continue' Anahtar Kelimesi Kullanımı
for i in range(9):
    if i > 3:
        continue  # Döngünün bir sonraki iterasyonuna geçer.
    print(i)
else:
    print("Döngü sonlandı!")

# 'break' Anahtar Kelimesi Kullanımı
active = True
while active:
    user_input = input("Sayı giriniz, çıkış için 'q' giriniz: ")
    if user_input == "q":
        break
    user_input = int(user_input)
    if user_input > 1:
        for i in range(2, user_input):
            if user_input % i == 0:
                print(f"{user_input} bir asal sayı değildir. Çünkü {i}'ye bölünebilir.")
                break
        else:
            print(f"{user_input} bir asal sayıdır.")
    else:
        print(f"{user_input} bir asal sayı değildir.")

# Fonksiyon Tanımlamaları ve Kullanımları
def my_function():
    print("Hello from a function")
    print("This is 2nd line")

my_function()

def name_of_func(arg1, arg2):
    """
    Bu fonksiyon örnek amaçlıdır ve herhangi bir işlem yapmaz.
    :param arg1: İlk argüman
    :param arg2: İkinci argüman
    :return: None
    """
    pass

def say_hello(name: str):
    """Bu fonksiyon hello print eder."""
    print("Hello", name)

say_hello("Michael")
print(type(say_hello))
print(say_hello)
print(say_hello("Jane"))

def squared(num: int):
    """Verilen sayının karesini döndürür."""
    return num * num

x = squared(9)
print(x)
print(type(x))

def carpanlar(num: int):
    """Bu fonksiyon girilen sayının çarpanlarını verir."""
    my_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            my_list.append(i)
    return my_list

x = carpanlar(84)
print(type(x))
print(x)

def topla(*args):
    """Verilen argümanların toplamını döndürür."""
    return sum(args)

x = topla(2, 5, 3, 8, 5, 6, 7, 8, 11)
print(x)

def power(base, expon=2):   # base: positional argumant, expon: keyword argument
    """Verilen tabanı ve üssü alarak sonucu hesaplar."""
    return base ** expon

x = power(3, 4)
print(x)

# Liste İşlemleri ve Fonksiyonlar
numbers = [1, 2, 4, 5, 7, 8, 11, 12]
numbers2 = [1, 3, 5, 7]

def even_check(num_list):
    """Verilen listede çift sayı olup olmadığını kontrol eder."""
    for num in num_list:
        if num % 2 == 0:
            return True
    return False

print(even_check(numbers))
print(even_check(numbers2))
