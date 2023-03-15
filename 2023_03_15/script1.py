"""
Lab02 - Zmienne
"""

zm = 5
print(zm)

zm = 5 + 10
print(zm)

zm = "Napis"
print(zm)

# Eksperyment 1
# zm = "Eksperyment" + 1
# print(zm)
"""
TypeError: can only concatenate str (not "int") to str
"""

# Deklaracja wielu zmiennych
a, b, c = 1, "Napis", 3
print(c)
print(b)

k = (2, 4, 6)  # Krotka (tuple)
(x, y, z) = k
print(x)

# Usuwanie zmiennych
del x
# print(x)
"""
NameError: name 'x' is not defined
"""

# Dla liczb mniejszych mniejszych/równych 2^8, zachodzi optymalizacja
# (zmienne o tej samej wartosci wskazują do tej samej pamięci) <= do momentu zmiany wartości zmiennej!

# a = 0
# b = 0
#
# while (id(a) == id(b)):
#     a += 1
#     b += 1
# print("{} -> {}".format(a, id(a)))
# print("{} -> {}".format(b, id(b)))

f = 3.14
print(f)

z = 3 + 5j  # Liczba zespolona
print(z)

# Systemy liczbowe

o = 0o45  # system ósemkowy
print(o)  # auto na system dziesięty

sz = 0x45  # system szesnastkowy
print(sz)

b = 0b00101101  # system binarny
print(b)

e = 5e5  # notacja naukowa
print(5)
