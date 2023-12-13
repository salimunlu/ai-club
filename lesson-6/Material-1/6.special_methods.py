# Special Methods, Magic Methods, Dunder (Double Underscore) Methods, Özel Metotlar


#__str__() Method: Yazdırılabilir (informal, resmi olmayan)
num = 12
str(num)
num.__str__()

# __repr__() method: Geliştiricelere yönelik resmi stringi temsil eder
repr(num)
num.__repr__()

# __add__() Method
num1 = 10
num2 = 5

num1 + num2
num1.__add__(num2)

# __lt__() Method: Less Than
x = 5
y = 6
x < y

x.__lt__(y)

# + __add__
# - __sub__
# * __mul__
# / __truediv__
# // __floordiv__
# % __mod__
# ** __pow__
# == __eq__
# != __ne__
# >= __ge__
# [] __getitem__
# len() __len__
# in __contains__

# __len__() method
my_list = list(range(5))
len(my_list)

my_list.__len__()

# __getitem__() method
my_list = list(range(3,9))
my_list[0]
my_list.__getitem__(0)

# For more information, please visit: https://diveintopython3.net/special-method-names.html

